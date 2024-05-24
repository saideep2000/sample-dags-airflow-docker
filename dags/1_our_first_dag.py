from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner" : "saideep samineni",
    "retries" : 5,
    "retry_delay" : timedelta(minutes = 1)
}

with DAG(
    dag_id = "our_first_dag_V1",
    default_args = default_args,
    description = "This is our first dag that we write",
    start_date = datetime(2024, 5, 23, 6, 47),
    schedule_interval = "@daily"
)as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo 'Hey, this is the first task'"
    )
    task1


with DAG(
    dag_id = "our_first_dag_V2",
    default_args = default_args,
    description = "This is our first dag that we write",
    start_date = datetime(2024, 5, 23, 6, 47),
    schedule_interval = "@daily"
)as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo 'Hey, this is the first task'"
    )
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo 'Hey, this is the second task'"
    )
    task1.set_downstream(task2)

with DAG(
    dag_id = "our_first_dag_V3",
    default_args = default_args,
    description = "This is our first dag that we write",
    start_date = datetime(2024, 5, 23, 6, 47),
    schedule_interval = "@daily"
)as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo 'Hey, this is the first task'"
    )
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo 'Hey, this is the second task'"
    )
    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "echo 'Hey, this is the third task'"
    )
    # Task dependency method 1
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # we can also write them as..
    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    # task1 >> [task2, task3]


