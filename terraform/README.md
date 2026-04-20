# Terraform Infra

Simple GCP provisioning for crypto pipeline.

## Usage
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Outputs:
- GCS: `crypto_project1-crypto-data`
- BQ Dataset: `crypto_project1.crypto_project1`
- BQ Dataset: `${gcp_project_id}.${gcp_project_id}`
- SA Key: `../keys/gcp-credentials.json` (auto-created)

Update `upload.py` bucket_name if needed. Run docker compose after.

**Destroy**: `terraform destroy -var='gcp_project_id=...'`
