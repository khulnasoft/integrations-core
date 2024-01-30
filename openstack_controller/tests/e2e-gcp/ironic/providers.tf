provider "google" {
  credentials = var.credentials_file
  project = "khulnasoft-integrations-lab"
  region = "europe-west4"
  zone = "europe-west4-a"
}
