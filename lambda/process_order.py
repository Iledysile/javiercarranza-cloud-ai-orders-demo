import json
import boto3

def lambda_handler(event, context):
    order_description = event.get("order_description", "")
    
    # Aquí iría la llamada a AWS Bedrock (simulada por ahora)
    ai_summary = f"AI summary for: {order_description}"
    
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket="javiercarranza-cloud-ai-orders-demo-bucket",
        Key="order_summary.txt",
        Body=ai_summary
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"summary": ai_summary})
    }
