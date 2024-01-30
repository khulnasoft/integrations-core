provider "google" {
  credentials = var.account_json
  project = "khulnasoft-integrations-lab"
  region = "europe-west4"
  zone = random_shuffle.az.result[0]
}
