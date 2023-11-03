from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('hello_world_dag', default_args=default_args, schedule_interval=None)

def say_hello():
    print("Hello, World!")

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=say_hello,
    dag=dag,
)

hello_task
