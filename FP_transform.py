# ===================== FP_transform.py =====================
# Tahap TRANSFORM: baca raw.parquet -> cleaning -> validasi clean (GX)
#                  -> simpan clean.parquet + pecah jadi star schema (4 dim + 1 fact)

import logging

import pandas as pd
import great_expectations as gx
from great_expectations.data_context import EphemeralDataContext
from great_expectations.data_context.types.base import DataContextConfig, InMemoryStoreBackendDefaults

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ctdc_transform")

# ================= CONFIG =================
RAW_PATH = "/opt/airflow/data/raw.parquet"
CLEAN_PATH = "/opt/airflow/data/clean.parquet"

# Output star schema (nama file mengikuti nama tabel di schema.sql)
DIM_DEMOGRAPHICS_PATH = "/opt/airflow/data/dim_demographics.parquet"
DIM_MEANS_PATH = "/opt/airflow/data/dim_means.parquet"
DIM_EXPLOITATION_PATH = "/opt/airflow/data/dim_exploitation.parquet"
DIM_RECRUITER_PATH = "/opt/airflow/data/dim_recruiter.parquet"
FACT_PATH = "/opt/airflow/data/fact_trafficking_cases.parquet"

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
CATEGORICAL_UNKNOWN_COLUMNS = [
    "gender", "ageBroad", "citizenship", "CountryOfExploitation", "traffickMonths",
]
GENDER_SET = ["Man", "Woman", "Trans/Transgender/NonConforming"]

# --- Pembagian kolom per tabel dimensi (sesuai schema.sql) ---
DEMOGRAPHICS_COLS = ["gender", "ageBroad", "citizenship", "CountryOfExploitation"]

MEANS_COLS = [
    "meansDebtBondageEarnings", "meansThreats", "meansAbusePsyPhySex",
    "meansFalsePromises", "meansDrugsAlcohol", "meansDenyBasicNeeds",
    "meansExcessiveWorkHours", "meansWithholdDocs",
]

EXPLOITATION_COLS = [
    "isForcedLabour", "isSexualExploit", "isOtherExploit",
    "sectorOfLabourAgriculture", "sectorOfLabourConstruction",
    "sectorOfLabourDomesticWork", "sectorOfLabourHospitality",
    "sectorOfSexProstitution", "sectorOfSexPornography",
]

RECRUITER_COLS = [
    "recruiterRelationIntimatePartner", "recruiterRelationFriend",
    "recruiterRelationFamily", "recruiterRelationOther",
]


# ================= TRANSFORM =================
def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Cleaning: flag missing -> False, kategori missing -> 'Unknown', tahun -> numerik
    df = df.copy()

    # Flag: "1" jadi True, sisanya (termasuk missing) jadi False
    for col in FLAG_COLUMNS:
        df[col] = df[col].fillna("0").eq("1")

    # Kategori: missing dan string kosong sama-sama jadi 'Unknown'
    for col in CATEGORICAL_UNKNOWN_COLUMNS:
        df[col] = df[col].fillna("Unknown").replace("", "Unknown")

    # Tahun registrasi jadi integer nullable (Int64)
    df["yearOfRegistration"] = pd.to_numeric(df["yearOfRegistration"], errors="coerce").astype("Int64")

    logger.info("Transform selesai: %d baris, %d kolom", len(df), len(df.columns))
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


def validate_clean(df, expected_row_count: int) -> None:
    # Gate 2: cek hasil cleaning SEBELUM dipecah jadi star schema & di-load
    validator = _get_validator(df, "clean_ctdc_suite")

    # Jumlah baris tidak boleh berubah dari raw (transform tidak memfilter baris)
    validator.expect_table_row_count_to_equal(value=expected_row_count)

    # Setelah cleaning, tidak boleh ada nilai kosong lagi
    for col in FLAG_COLUMNS:
        validator.expect_column_values_to_not_be_null(column=col)
    for col in CATEGORICAL_UNKNOWN_COLUMNS:
        validator.expect_column_values_to_not_be_null(column=col)

    # Gender kini boleh berisi 'Unknown' juga
    validator.expect_column_values_to_be_in_set(column="gender", value_set=GENDER_SET + ["Unknown"])

    # Tahun registrasi harus dalam rentang wajar
    validator.expect_column_values_to_be_between(column="yearOfRegistration", min_value=2002, max_value=2026)

    result = validator.validate()
    if not result.success:
        failed = [r.expectation_config.expectation_type for r in result.results if not r.success]
        raise RuntimeError(f"Validasi CLEAN gagal: {failed}")
    logger.info("Validasi clean lulus.")


# ================= SPLIT KE STAR SCHEMA =================
def _build_dimension(df: pd.DataFrame, cols: list, id_name: str) -> pd.DataFrame:
    # Ambil kombinasi unik dari kolom-kolom dimensi, lalu beri surrogate key berurutan (1..n)
    dim = df[cols].drop_duplicates().reset_index(drop=True)
    dim.insert(0, id_name, range(1, len(dim) + 1))
    return dim


def build_star_schema(df: pd.DataFrame):
    # Pecah data clean (flat) jadi 4 tabel dimensi + 1 tabel fakta
    df = df.copy()


    # --- Bangun tiap tabel dimensi ---
    dim_demographics = _build_dimension(df, DEMOGRAPHICS_COLS, "demographic_id")
    dim_means = _build_dimension(df, MEANS_COLS, "means_id")
    dim_exploitation = _build_dimension(df, EXPLOITATION_COLS, "exploitation_id")
    dim_recruiter = _build_dimension(df, RECRUITER_COLS, "recruiter_id")

    # --- Bangun tabel fakta: merge balik ke tiap dimensi untuk ambil foreign key-nya ---
    fact = df.merge(dim_demographics, on=DEMOGRAPHICS_COLS, how="left")
    fact = fact.merge(dim_means, on=MEANS_COLS, how="left")
    fact = fact.merge(dim_exploitation, on=EXPLOITATION_COLS, how="left")
    fact = fact.merge(dim_recruiter, on=RECRUITER_COLS, how="left")

    # Ambil hanya kolom yang ada di tabel fact sesuai schema.sql
    fact_trafficking_cases = fact[[
        "yearOfRegistration", "traffickMonths",
        "demographic_id", "means_id", "exploitation_id", "recruiter_id",
    ]].reset_index(drop=True)

    # Primary key tabel fakta
    fact_trafficking_cases.insert(0, "case_id", range(1, len(fact_trafficking_cases) + 1))

    # Nama kolom ageBroad -> agebroad, mengikuti penamaan di schema.sql
    dim_demographics = dim_demographics.rename(columns={"ageBroad": "agebroad"})

    logger.info(
        "Star schema selesai: demographics=%d, means=%d, exploitation=%d, recruiter=%d, fact=%d",
        len(dim_demographics), len(dim_means), len(dim_exploitation),
        len(dim_recruiter), len(fact_trafficking_cases),
    )

    return dim_demographics, dim_means, dim_exploitation, dim_recruiter, fact_trafficking_cases


# ================= RUN =================
if __name__ == "__main__":
    # Baca hasil extract
    df_raw = pd.read_parquet(RAW_PATH)

    # Cleaning + validasi
    df_clean = transform(df_raw)
    validate_clean(df_clean, expected_row_count=len(df_raw))

    # Simpan versi flat (clean.parquet)
    df_clean.to_parquet(CLEAN_PATH, index=False)
    logger.info("Clean disimpan ke: %s (%d baris)", CLEAN_PATH, len(df_clean))

    # Pecah jadi star schema lalu simpan tiap tabel
    dim_demographics, dim_means, dim_exploitation, dim_recruiter, fact_trafficking_cases = build_star_schema(df_clean)

    dim_demographics.to_parquet(DIM_DEMOGRAPHICS_PATH, index=False)
    dim_means.to_parquet(DIM_MEANS_PATH, index=False)
    dim_exploitation.to_parquet(DIM_EXPLOITATION_PATH, index=False)
    dim_recruiter.to_parquet(DIM_RECRUITER_PATH, index=False)
    fact_trafficking_cases.to_parquet(FACT_PATH, index=False)

    logger.info("5 tabel star schema disimpan ke data/")