# ===================== FP_extract.py =====================
# Tahap EXTRACT: scrape halaman CTDC -> download CSV -> validasi raw (GX) -> simpan raw.parquet

import io
import logging
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
import great_expectations as gx
from great_expectations.data_context import EphemeralDataContext
from great_expectations.data_context.types.base import DataContextConfig, InMemoryStoreBackendDefaults

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ctdc_extract")

# ================= CONFIG =================
CTDC_PAGE_URL = "https://www.ctdatacollaborative.org/dataset/global-synthetic-data-and-resources/resource/microdata"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ETL-bot/1.0)"}

# Path absolut di dalam container (folder ./data di-mount ke /opt/airflow/data)
RAW_PATH = "/opt/airflow/data/raw.parquet"

# Kolom flag: nilai "1" = terjadi, missing = tidak terjadi
FLAG_COLUMNS = [
    "meansDebtBondageEarnings", "meansThreats", "meansAbusePsyPhySex",
    "meansFalsePromises", "meansDrugsAlcohol", "meansDenyBasicNeeds",
    "meansExcessiveWorkHours", "meansWithholdDocs",
    "isForcedLabour", "isSexualExploit", "isOtherExploit",
    "sectorOfLabourAgriculture", "sectorOfLabourConstruction",
    "sectorOfLabourDomesticWork", "sectorOfLabourHospitality",
    "sectorOfSexProstitution", "sectorOfSexPornography",
    "recruiterRelationIntimatePartner", "recruiterRelationFriend",
    "recruiterRelationFamily", "recruiterRelationOther",
]

# Kolom kategorikal: missing akan diisi 'Unknown' di tahap transform
CATEGORICAL_UNKNOWN_COLUMNS = [
    "gender", "ageBroad", "citizenship", "CountryOfExploitation", "traffickMonths",
]

# Struktur kolom yang diharapkan ada di CSV mentah
ALL_RAW_COLUMNS = ["yearOfRegistration"] + CATEGORICAL_UNKNOWN_COLUMNS + FLAG_COLUMNS
GENDER_SET = ["Man", "Woman", "Trans/Transgender/NonConforming"]


# ================= EXTRACT =================
def get_csv_download_url(page_url: str = CTDC_PAGE_URL) -> str:
    # Scrape halaman CTDC untuk mencari link download CSV terbaru
    resp = requests.get(page_url, timeout=30, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Cari tombol download utama
    link = soup.find("a", class_="btn-download")

    # Fallback: cari link apa pun yang berakhiran .csv
    if link is None or not link.get("href"):
        link = soup.find("a", href=lambda h: h and h.lower().endswith(".csv"))

    if link is None:
        raise RuntimeError(f"Link download CSV tidak ditemukan di {page_url}")

    # Ubah href relatif jadi URL absolut
    csv_url = urljoin(page_url, link["href"])
    logger.info("CSV ditemukan: %s", csv_url)
    return csv_url


def extract() -> pd.DataFrame:
    # Download CSV dan baca jadi DataFrame (semua kolom dibaca sebagai string dulu)
    csv_url = get_csv_download_url()
    resp = requests.get(csv_url, timeout=120, headers=HEADERS)
    resp.raise_for_status()

    df = pd.read_csv(io.BytesIO(resp.content), dtype=str)
    logger.info("Extract selesai: %d baris, %d kolom", len(df), len(df.columns))
    return df


# ================= VALIDATE (Great Expectations) =================
def _force_ephemeral_context():
    # Context GX in-memory, tidak menulis file konfigurasi apa pun ke disk
    project_config = DataContextConfig(store_backend_defaults=InMemoryStoreBackendDefaults())
    return EphemeralDataContext(project_config=project_config)


def _get_validator(df, suite_name: str):
    # Siapkan validator GX untuk satu DataFrame
    context = _force_ephemeral_context()
    datasource = context.sources.add_pandas(f"{suite_name}_src")

    # dataframe di-pass saat add_dataframe_asset (API GX 0.16.x ke atas)
    data_asset = datasource.add_dataframe_asset(name=f"{suite_name}_asset", dataframe=df)
    batch_request = data_asset.build_batch_request()

    context.add_expectation_suite(expectation_suite_name=suite_name)
    return context.get_validator(batch_request=batch_request, expectation_suite_name=suite_name)


def validate_raw(df) -> None:
    # Gate 1: cek struktur & isi CSV mentah SEBELUM masuk tahap transform
    validator = _get_validator(df, "raw_ctdc_suite")

    # Struktur kolom harus persis sesuai ekspektasi
    validator.expect_table_columns_to_match_set(column_set=ALL_RAW_COLUMNS, exact_match=True)

    # Minimal 100 ribu baris, sebagai penanda file tidak korup/terpotong
    validator.expect_table_row_count_to_be_between(min_value=100_000)

    # Kolom flag hanya boleh berisi "1" (selain itu missing)
    for col in FLAG_COLUMNS:
        validator.expect_column_values_to_be_in_set(column=col, value_set=["1"])

    # Gender harus salah satu dari nilai yang dikenal
    validator.expect_column_values_to_be_in_set(column="gender", value_set=GENDER_SET)

    result = validator.validate()
    if not result.success:
        failed = [r.expectation_config.expectation_type for r in result.results if not r.success]
        raise RuntimeError(f"Validasi RAW gagal: {failed}")
    logger.info("Validasi raw lulus.")


# ================= RUN =================
if __name__ == "__main__":
    df_raw = extract()
    validate_raw(df_raw)

    # Handoff ke tahap transform lewat file parquet
    df_raw.to_parquet(RAW_PATH, index=False)
    logger.info("Raw disimpan ke: %s (%d baris)", RAW_PATH, len(df_raw))