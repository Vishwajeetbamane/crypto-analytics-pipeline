from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/5 * * * *",  # Updated to run every 5 minutes
    catchup=False,
    is_paused_upon_creation=False
) as dag:

    ingest = BashOperator(
        task_id="ingest",
        bash_command="cd /opt/airflow/ingestion && /opt/ingestion-venv/bin/python ingest/ingest.py"
    )

    upload_gcs = BashOperator(
        task_id="upload_to_gcs",
        bash_command="cd /opt/airflow/ingestion && /opt/ingestion-venv/bin/python upload_gcs/upload.py"
    )

    load_bq = BashOperator(
        task_id="load_bq",
        bash_command="cd /opt/airflow/ingestion && /opt/ingestion-venv/bin/python warehouse/load_to_bq.py"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt && /opt/dbt-venv/bin/dbt run --profiles-dir . --log-path /tmp/dbt-logs --target-path /tmp/dbt-target"

    )


    ingest >> upload_gcs >> load_bq >> dbt_run