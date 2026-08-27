# ===================== FP_load.py =====================
# Tahap LOAD: pastikan tabel star schema ada (DDL) -> baca 6 tabel parquet
#             -> load ke Neon (Postgres) -> sanity check jumlah baris
# Semua exception ditangkap agar output hanya menampilkan pesan error inti,
# tanpa dump SQL statement dan parameter yang panjang.

import logging
import sys

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ctdc_load")

# ================= CONFIG =================
NEON_DATABASE_URL = "{isi_dengan_url_database_neon_anda}"  # contoh: postgresql+psycopg2://username:password@host:port/dbname

# Mapping: path file parquet -> nama tabel tujuan di Neon
# Urutan penting: tabel dimensi di-load lebih dulu, tabel fakta terakhir (karena punya foreign key)
TABLES = [
    ("/opt/airflow/data/dim_demographics.parquet", "dim_demographics"),
    ("/opt/airflow/data/dim_means.parquet", "dim_means"),
    ("/opt/airflow/data/dim_exploitation.parquet", "dim_exploitation"),
    ("/opt/airflow/data/dim_recruiter.parquet", "dim_recruiter"),
    ("/opt/airflow/data/fact_trafficking_cases.parquet", "fact_trafficking_cases"),
]

# Tabel flat (hasil cleaning, di luar star schema) — di-load sebagai tabel staging
CLEAN_PATH = "/opt/airflow/data/clean.parquet"
CLEAN_TABLE = "stg_ctdc_global_synthetic_data"

# DDL star schema 
# IF NOT EXISTS supaya aman dijalankan berkali-kali (tidak error kalau tabel sudah ada).
DDL_STATEMENTS = """
CREATE TABLE IF NOT EXISTS dim_demographics (
    demographic_id SERIAL PRIMARY KEY,
    gender VARCHAR(50),
    agebroad VARCHAR(50),
    citizenship VARCHAR(100),
    CountryOfExploitation VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_means (
    means_id SERIAL PRIMARY KEY,
    meansDebtBondageEarnings BOOLEAN,
    meansThreats BOOLEAN,
    meansAbusePsyPhySex BOOLEAN,
    meansFalsePromises BOOLEAN,
    meansDrugsAlcohol BOOLEAN,
    meansDenyBasicNeeds BOOLEAN,
    meansExcessiveWorkHours BOOLEAN,
    meansWithholdDocs BOOLEAN
);

CREATE TABLE IF NOT EXISTS dim_exploitation (
    exploitation_id SERIAL PRIMARY KEY,
    isForcedLabour BOOLEAN,
    isSexualExploit BOOLEAN,
    isOtherExploit BOOLEAN,
    sectorOfLabourAgriculture BOOLEAN,
    sectorOfLabourConstruction BOOLEAN,
    sectorOfLabourDomesticWork BOOLEAN,
    sectorOfLabourHospitality BOOLEAN,
    sectorOfSexProstitution BOOLEAN,
    sectorOfSexPornography BOOLEAN
);

CREATE TABLE IF NOT EXISTS dim_recruiter (
    recruiter_id SERIAL PRIMARY KEY,
    recruiterRelationIntimatePartner BOOLEAN,
    recruiterRelationFriend BOOLEAN,
    recruiterRelationFamily BOOLEAN,
    recruiterRelationOther BOOLEAN
);

CREATE TABLE IF NOT EXISTS fact_trafficking_cases (
    case_id SERIAL PRIMARY KEY,
    yearOfRegistration INT,
    traffickMonths VARCHAR(50),
    demographic_id INT REFERENCES dim_demographics(demographic_id),
    means_id INT REFERENCES dim_means(means_id),
    exploitation_id INT REFERENCES dim_exploitation(exploitation_id),
    recruiter_id INT REFERENCES dim_recruiter(recruiter_id)
);
"""


# ================= HELPER: print pesan error  =================
def _short_error(e: Exception) -> str:
    if isinstance(e, SQLAlchemyError) and getattr(e, "orig", None) is not None:
        return f"{type(e.orig).__name__}: {e.orig}"
    return str(e).splitlines()[0]


def _fail(step_name: str, e: Exception):
    logger.error("GAGAL pada tahap '%s': %s", step_name, _short_error(e))
    sys.exit(1)


# ================= DDL =================
def create_tables(engine) -> None:
    try:
        with engine.begin() as conn:
            conn.execute(text(DDL_STATEMENTS))
    except Exception as e:
        _fail("create_tables (DDL)", e)
    logger.info("[OK] create_tables: tabel star schema dipastikan ada.")


# ================= LOAD =================
def load_table(engine, df: pd.DataFrame, table_name: str, if_exists: str = "append") -> None:
    try:
        df.to_sql(table_name, engine, if_exists=if_exists, index=False, method="multi", chunksize=5000)
    except Exception as e:
        _fail(f"load_table -> {table_name}", e)
    logger.info("[OK] load_table -> '%s': %d baris berhasil di-load.", table_name, len(df))


def truncate_tables(engine) -> None:
    table_names = ", ".join(name for _, name in TABLES)
    try:
        with engine.begin() as conn:
            conn.execute(text(f"TRUNCATE TABLE {table_names} RESTART IDENTITY CASCADE;"))
    except Exception as e:
        _fail("truncate_tables", e)
    logger.info("[OK] truncate_tables: tabel star schema dikosongkan (%s).", table_names)


def sanity_check(engine, table_name: str, expected_count: int) -> None:
    try:
        with engine.connect() as conn:
            n = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
    except Exception as e:
        _fail(f"sanity_check -> {table_name}", e)

    if n != expected_count:
        logger.error(
            "[GAGAL] sanity_check -> '%s': di Neon=%d, diharapkan=%d (tidak cocok!)",
            table_name, n, expected_count,
        )
        sys.exit(1)

    logger.info("[OK] sanity_check -> '%s': %d baris cocok.", table_name, n)


# ================= RUN =================
if __name__ == "__main__":
    engine = create_engine(NEON_DATABASE_URL)

    # --- 1. Load tabel flat (staging), pakai replace karena tabel ini berdiri sendiri ---
    df_clean = pd.read_parquet(CLEAN_PATH)
    load_table(engine, df_clean, CLEAN_TABLE, if_exists="replace")
    sanity_check(engine, CLEAN_TABLE, len(df_clean))

    # --- 2. Pastikan tabel star schema ada (DDL, aman diulang) ---
    create_tables(engine)

    # --- 3. Kosongkan tabel star schema (struktur tabel & foreign key tetap dipertahankan) ---
    truncate_tables(engine)

    # --- 4. Load tabel star schema sesuai urutan: dimensi dulu, fakta terakhir ---
    for path, table_name in TABLES:
        df = pd.read_parquet(path)

        df.columns = [c.lower() for c in df.columns]
        load_table(engine, df, table_name, if_exists="append")
        sanity_check(engine, table_name, len(df))

    logger.info("[SELESAI] Semua tabel berhasil di-load ke Neon.")