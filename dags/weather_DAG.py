from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from weather_info import curr_weather_data
from create_table import insert_column_header
from insert_into_table import insert_values

default_args = {
    "owner": "Shobhit",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 15),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

dag = DAG("Dag", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='create_csv', python_callable=curr_weather_data, dag=dag)
t2 = PythonOperator(task_id='create_table', python_callable=insert_column_header, dag=dag)
t3 = PythonOperator(task_id='insert_value', python_callable=insert_values, dag=dag)



t1 >> t2 >> t3