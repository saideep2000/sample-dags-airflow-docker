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

Now let's remove the example volumes that we have in our airflow:

docker-compose down -v

Now change the airflow_core_load_examples to 'false'

docker-compose up airflow-init

docker-compose up -d

Now again login and see if examples are there or not

Let's create our first DAG.

In the DAG folder create the dag.




### Installed things :




## Sample installation is done.

### Happy Coding!

---

**Note:** This is a sample airflow with docker.
