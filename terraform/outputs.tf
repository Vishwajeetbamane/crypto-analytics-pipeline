output "bucket_name" {
  value = google_storage_bucket.crypto_data.name
  description = "Set GCS_BUCKET_NAME=${google_storage_bucket.crypto_data.name} in .env"
}

output "bucket_name" {
  value = google_storage_bucket.crypto_data.name
}

output "bq_dataset" {
  value = "crypto_project1.crypto_project1"
}
terraform init
terraform plan -var='gcp_project_id=your_project'
terraform apply -var='gcp_project_id=your_project' -auto-approve
cp ../keys/gcp-credentials.json ../keys/  # Update .env if needed
EOT
}
