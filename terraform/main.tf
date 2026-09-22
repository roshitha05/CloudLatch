terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "cloudlatch" {
  bucket = var.bucket_name

  tags = {
    Project     = "CloudLatch"
    Environment = "local"
    ManagedBy   = "Terraform"
  }
}

resource "aws_sqs_queue" "cloudlatch" {
  name = var.queue_name

  visibility_timeout_seconds = 30
  message_retention_seconds  = 86400

  tags = {
    Project     = "CloudLatch"
    Environment = "local"
    ManagedBy   = "Terraform"
  }
}