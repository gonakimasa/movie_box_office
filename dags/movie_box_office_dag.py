from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from movie_box_fetch import fetch_movie_data

def fetch_movie_data():
    print("映画データを取得しました（仮）")

def clean_movie_data():
    print("データを整形しました（仮）")

def load_to_duckdb():
    print("DuckDBに格納しました（仮）")

default_args = {
    'owner': 'ggakms',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='movie_box_office_pipeline',
    default_args=default_args,
    description='映画データを処理するETLパイプライン',
    schedule_interval='0 3 * * *',  # JST 03:00
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['movie', 'etl'],
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_movie_data',
        python_callable=fetch_movie_data
    )

    clean_task = PythonOperator(
        task_id='clean_movie_data',
        python_callable=clean_movie_data
    )

    load_task = PythonOperator(
        task_id='load_to_duckdb',
        python_callable=load_to_duckdb
    )

    fetch_task >> clean_task >> load_task
