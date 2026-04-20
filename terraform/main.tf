terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "crypto_project1"
  # credentials = file("../keys/gcp-credentials.json")  # Optional if gcloud auth
}

# GCS Bucket for Parquet
resource "google_storage_bucket" "crypto_data" {
  name                        = "crypto_project1"
  location                    = "US"
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }
}

# BigQuery Dataset
resource "google_bigquery_dataset" "crypto_dataset" {
  dataset_id = "crypto_project1"
  location   = "US"
}


