'''
=================================================
Final Project

Tim   : Team-CODA-020

DAG Airflow yang mengorkestrasi pipeline ETL dataset CTDC Global Synthetic Data.
Alur: extract -> transform -> load (berurutan, tiap tahap script terpisah).
=================================================
'''

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


# Konfigurasi default yang berlaku untuk semua task dalam DAG ini
default_args = {
    'owner': 'Team-CODA-020',
    'start_date': dt.datetime(2024, 11, 1),   # tanggal mulai DAG dianggap aktif
    'retries': 1,                             # jumlah percobaan ulang kalau task gagal
    'retry_delay': dt.timedelta(minutes=5),   # jeda sebelum retry dijalankan
}


with DAG('Final-Project_ETL_Pipeline',
         default_args=default_args,
         # Jadwal: menit 10-30 (kelipatan 10) pada jam 9, setiap hari Sabtu
         schedule_interval='10-30/10 9 * * 6',
         catchup=False,   # jangan jalankan ulang run yang terlewat dari masa lalu
         ) as dag:

    # Tahap 1: download CSV dari CTDC, validasi raw (Great Expectations), simpan raw.parquet
    extract_task = BashOperator(
        task_id='extract',
        bash_command='python /opt/airflow/scripts/FP_extract.py'
    )

    # Tahap 2: cleaning data, validasi clean (Great Expectations),
    #          simpan clean.parquet + pecah jadi 5 tabel star schema (parquet terpisah)
    transform_task = BashOperator(
        task_id='transform',
        bash_command='python /opt/airflow/scripts/FP_transform.py'
    )

    # Tahap 3: pastikan tabel star schema ada di Neon (DDL),
    #          load 6 tabel (staging + star schema) ke Neon, lalu sanity check jumlah baris
    load_task = BashOperator(
        task_id='load',
        bash_command='python /opt/airflow/scripts/FP_load.py'
    )

    # Urutan eksekusi: extract harus selesai dulu sebelum transform,
    # transform harus selesai dulu sebelum load
    extract_task >> transform_task >> load_task