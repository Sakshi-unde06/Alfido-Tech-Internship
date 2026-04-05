# ☁️ Task 3: Serverless Function using AWS Lambda

## 📌 Objective
The goal of this task is to create a serverless function that returns JSON output and make it publicly accessible using API Gateway.

---

## 🛠️ Technologies Used
- AWS Lambda
- API Gateway
- Python

---

## 🚀 Steps Performed

1. Created a Lambda function using Python
2. Wrote code to return structured JSON response
3. Tested the function using AWS console
4. Created an HTTP API using API Gateway
5. Connected Lambda function with API Gateway
6. Generated a public API endpoint

---

## 💻 Function Code

```python
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
