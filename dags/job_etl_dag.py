from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id = "job_etl_dag",
    start_date = datetime(2026, 5, 31),
    schedule = "*/2 * * * *",
    catchup = False,
) as dag:

    extract = BashOperator(
        task_id = "extract",
        bash_command = "/home/althaaf/job_listing_etl_project/job_listing/bin/python /home/althaaf/job_listing_etl_project/scripts/extract.py""
    )

    transform = BashOperator(
        task_id = "transform",
        bash_command = "/home/althaaf/job_listing_etl_project/job_listing/bin/python /home/althaaf/job_listing_etl_project/scripts/transform.py"
    )

    load = BashOperator(
        task_id = "load",
        bash_command = "/home/althaaf/job_listing_etl_project/job_listing/bin/python /home/althaaf/job_listing_etl_project/scripts/load.py"
    )

    extract >> transform >> load