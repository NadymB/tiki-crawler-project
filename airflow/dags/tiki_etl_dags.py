from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from etl.transform.transform_prod_ids import main as transform_main
from etl.extract.extract_products import main as extract_main
from etl.load.load_products import main as load_main
from src.load.notify_discord import notify_discord

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": notify_discord,
}

with DAG(
    dag_id="tiki_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["tiki", "etl"],
) as dag:

    transform = PythonOperator(
        task_id="transform_product_ids",
        python_callable=transform_main,
    )

    extract = PythonOperator(
        task_id="extract_products",
        python_callable=extract_main,
        retries=3,
        retry_delay=timedelta(minutes=5),
        on_failure_callback=notify_discord,
    )

    load = PythonOperator(
        task_id="load_products",
        python_callable=load_main,
    )

    transform >> extract >> load
