from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def add_two_numbers():
    x = 6 + 10
    return x


dag = DAG('add_num',
          description='Add two integers',
          schedule_interval='0 12 * * *',
          start_date=datetime(2022, 6, 23),
          catchup=False)

add_operator = PythonOperator(task_id='add_num_task',
                              python_callable=add_two_numbers,
                              dag=dag)

add_operator