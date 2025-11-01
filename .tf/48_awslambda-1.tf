# terraform config for AWS Lambda
resource "awslambda" "awslambda-1" {
  name = "madatcloud-awslambda-1"
}

# operation: events (Source (S3) sends events to target (Lambda). Need S3 bucket notification and lambda permission. Lambda needs basic execution role.)
