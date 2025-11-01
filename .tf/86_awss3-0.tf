# Terraform config for Amazon S3
resource "awss3" "awss3-0" {
  name = "madatcloud-awss3-0"
}

# Operation: events (Source (S3) sends events to target (Lambda). Need S3 bucket notification and lambda permission. Lambda needs basic execution role.)
# Operation: read (Target (EC2 or Lambda) reads objects from S3.)
