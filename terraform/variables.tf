variable "aws_region" {
  description = "AWS region used by the local infrastructure."
  type        = string
  default     = "ap-southeast-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket used by CloudLatch."
  type        = string
  default     = "cloudlatch-local-storage"
}

variable "queue_name" {
  description = "Name of the SQS queue used by CloudLatch."
  type        = string
  default     = "cloudlatch-events"
}