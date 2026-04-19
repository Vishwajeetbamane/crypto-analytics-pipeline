FROM apache/airflow:2.9.0


USER root


# ingestion venv
RUN python -m venv /opt/ingestion-venv
COPY ingestion/requirements.txt /tmp/ingestion-requirements.txt
RUN /opt/ingestion-venv/bin/pip install -r /tmp/ingestion-requirements.txt

# dbt venv
RUN python -m venv /opt/dbt-venv
COPY dbt/requirements.txt /tmp/dbt-requirements.txt
RUN /opt/dbt-venv/bin/pip install -r /tmp/dbt-requirements.txt

USER airflow