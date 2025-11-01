# terraform config for Amazon S3....
resource "awss3" "awss3-0" {
  name = "Suhel-awss3-0"
}

# Operation: events (Source (S3) sends events to target (Lambda). Need S3 bucket notification and lambda permission. Lambda needs basic execution role.)..

