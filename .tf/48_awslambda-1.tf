# Terraform config for AWS Lambda
resource "awslambda" "awslambda-1" {
  name = "example-awslambda-1"
}

# Operation: events (Source (S3) sends events to target (Lambda). Need S3 bucket notification and lambda permission. Lambda needs basic execution role.)
