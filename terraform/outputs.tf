output "s3_bucket_name" {
  description = "Name of the CloudLatch S3 bucket."
  value       = aws_s3_bucket.cloudlatch.bucket
}

output "sqs_queue_url" {
  description = "URL of the CloudLatch SQS queue."
  value       = aws_sqs_queue.cloudlatch.url
}