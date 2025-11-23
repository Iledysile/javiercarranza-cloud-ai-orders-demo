provider aws {
  region = eu-central-1
}

resource aws_s3_bucket orders_bucket {
  bucket = javiercarranza-cloud-ai-orders-demo-bucket
  acl    = private
}

resource aws_iam_role lambda_role {
  name = lambda_execution_role
  assume_role_policy = EOF
{
  Version 2012-10-17,
  Statement [
    {
      Action stsAssumeRole,
      Principal {
        Service lambda.amazonaws.com
      },
      Effect Allow,
      Sid 
    }
  ]
}
EOF
}
