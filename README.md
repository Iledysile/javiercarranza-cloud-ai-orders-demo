\# Cloud AI Orders Demo



Author: Javier Carranza Nalvaiz  

Contact: carranzaragoza@gmail.com  

LinkedIn: https://linkedin.com/in/jcarranza1988



\## Description

This is a mini demo simulating an order microservice using \*\*AWS Bedrock\*\* and \*\*Terraform\*\*.  

The service receives an order, generates an AI-based summary, and stores the result in an S3 bucket.  

It demonstrates cloud-native development, infrastructure as code (IaC), and serverless architectures.



\## Project Structure

\- `terraform/` → Defines AWS infrastructure (S3 bucket, IAM roles, Lambda) using Terraform  

\- `lambda/` → Lambda function code interacting with AWS Bedrock  

\- `README.md` → Project documentation  



\## Features

\- Cloud-native microservice for order processing  

\- AI integration with AWS Bedrock for text summarization  

\- Infrastructure as code with Terraform  

\- Serverless deployment using AWS Lambda  

\- Results storage in S3  

\- Easily extendable for other AI-driven cloud workflows  



\## Getting Started



\### Prerequisites

\- AWS account with permissions for S3, Lambda, and IAM  

\- Terraform installed locally  

\- Python 3.11+ for Lambda packaging  



\### Setup

1\. Navigate to the Terraform folder:

```bash

cd terraform

2\. Initialize Terraform:

terraform init

3\. Preview changes:

terraform plan

4\. Apply infrastructure:

terraform apply



\### Testing the Lambda



1. Go to AWS Console → Lambda → process\_order\_demo

2\. Create a test event JSON:

{

&nbsp; "order\_description": "Order for t-shirt and pants"

}

3\. Invoke the function and check results in the S3 bucket defined by Terraform.



\### Cleanup

terraform destroy





\### Notes



* This project demonstrates cloud infrastructure automation, serverless computing, and AI integration.
* Can be used as a reference or expanded for other cloud AI applications.
