# Airflow with Pyspark inside

- copy & paste .env.example, lalu rename jadi .env dan isi dengan kredensial anda
- cd `**********/CODA-020-Final_Project/airflow_spark`
- build docker using docker `docker build -t airflow-spark .`
- run docker compose using `docker compose -f airflow.yaml up -d`

# Running the python script on Airflow
- run the script by `sudo -u airflow python /opt/airflow/scripts/script.py` # kalo eror saat run, file dag.py bagian bash hapus sudo nya ( run tanpa sudo )
