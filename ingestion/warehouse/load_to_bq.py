from google.cloud import bigquery

def create_external_table():
    client = bigquery.Client()

    table_id = "dtc-course-486211.crypto_project1.crypto_data_ext"

    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = [
        "gs://crypto_project1/parquet/*"
    ]

    # Enable Hive partitioning
    hive_partitioning_opts = bigquery.external_config.HivePartitioningOptions()
    hive_partitioning_opts.mode = "AUTO"
    hive_partitioning_opts.source_uri_prefix = "gs://crypto_project1/parquet/"

    external_config.hive_partitioning = hive_partitioning_opts

    table = bigquery.Table(table_id)
    table.external_data_configuration = external_config

    table = client.create_table(table, exists_ok=True)

    print(f"Created table {table.table_id}")

    

if __name__ == "__main__":
    create_external_table()