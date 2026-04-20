import os
from google.cloud import bigquery

def create_external_table():
    client = bigquery.Client()

    project_id = os.getenv('GCP_PROJECT_ID')
    dataset_id = os.getenv('BQ_DATASET')
    table_id = f"{project_id}.{dataset_id}.crypto_data_ext"

    bucket_name = os.getenv('GCS_BUCKET_NAME')

    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = [
        f"gs://{bucket_name}/parquet/*"
    ]

    # Enable Hive partitioning
    hive_partitioning_opts = bigquery.external_config.HivePartitioningOptions()
    hive_partitioning_opts.mode = "AUTO"
    hive_partitioning_opts.source_uri_prefix = f"gs://{bucket_name}/parquet/"


    external_config.hive_partitioning = hive_partitioning_opts

    
    table = bigquery.Table(table_id)
    table.external_data_configuration = external_config
  
    table = client.create_table(table, exists_ok=True)

    print(f"Created table {table.table_id}")

    

if __name__ == "__main__":
    create_external_table()