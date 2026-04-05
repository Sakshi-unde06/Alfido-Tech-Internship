import json
from datetime import datetime

def lambda_handler(event, context):
    
    response = {
        "message": "Hello from Serverless Cloud 🚀",
        "project": "Cloud Computing Internship - Task 3",
        "technology": "AWS Lambda + API Gateway",
        "status": "success",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "data": {
            "language": "Python",
            "architecture": "Serverless",
            "response_type": "JSON"
        }
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
