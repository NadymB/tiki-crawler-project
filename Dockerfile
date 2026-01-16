FROM apache/airflow:2.5.1

USER root
RUN apt-get update && apt-get install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY airflow/dags/ /opt/airflow/dags/
COPY src/ /opt/airflow/src/
COPY etl/ /opt/airflow/etl/
COPY resources/ /opt/airflow/resources/
COPY config/ /opt/airflow/config/
