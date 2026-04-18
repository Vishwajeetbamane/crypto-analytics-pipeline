
from google.cloud import storage
from pathlib import Path
from datetime import datetime, timezone
import os


year = datetime.now(timezone.utc).strftime("%Y")
month = datetime.now(timezone.utc).strftime("%m")
day = datetime.now(timezone.utc).strftime("%d")
hour = datetime.now(timezone.utc).strftime("%H")

project_path = Path(__file__).resolve().parent.parent.parent
source = Path(f"{project_path}/parquet/data.parquet")

def upload_blob(source):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    bucket_name = "crypto_project1"

    # The path to your file to upload

    source_file_name = source

    # The ID of your GCS object
    destination_blob_name = f"parquet/year={year}/month={month}/day={day}/hour={hour}/data.parquet"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)


    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )



# Delete unwanted file
def del_raw(source):
    os.remove(source)
    


if __name__ == "__main__":   
    upload_blob(source)
    del_raw(source)