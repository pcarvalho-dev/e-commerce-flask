import boto3

from config import Config

# Simple Storage Service
s3 = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
)

# Simple Notification Service
sns = boto3.client(
    "sns",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1"
)
# Simple Email Service
ses = boto3.client(
    "ses",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1"
)