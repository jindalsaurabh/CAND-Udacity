terraform {
  backend "s3" {
    bucket = "udacity-terraform-backend-sj"
    key = "terraform.tfstate"
    region = "us-east-1"
  }
}
