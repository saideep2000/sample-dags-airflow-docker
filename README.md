# Airflow

## Overview

## Steps did in this project :

To see directory : pwd

If there is any active env's : 

conda deactivate

python3 --version

run docker desktop

docker --version

docker-compose --version

docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'

see if atleast 4gb is alloted or not

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'

Now a docker-compose.yaml is created.

We don't need celery and flower things from them as we'll do it from local.

mkdir -p ./dags ./logs ./plugins ./config

docker compose up airflow-init

docker-compose up -d

docker ps

login to http://0.0.0.0:8080/home

Credentials:

airflow
airflow




python3 -m venv py_env

source py_env/bin/activate

src : https://github.com/apache/airflow?tab=readme-ov-file#installing-from-pypi

pip install 'apache-airflow==2.9.1' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.11.txt"

If error in gcc :

xcode-select --install

pip install --upgrade pip

export AIRFLOW_HOME="$(pwd)"

Create sql db: 

airflow db init

airflow webserver -p 8080

airflow users create --username admin --firstname saideep --lastname samineni --role Admin --email samineni.sa@northeastern.edu

Set the password :

saideepsamineni

Now login to the airflow

Now in different terminal we will start the scheduler :

export AIRFLOW_HOME="$(pwd)"

source py_env/bin/activate

airflow scheduler



### Installed things :




## Sample installation is done.

### Happy Coding!

---

**Note:** This is a sample airflow with docker.
