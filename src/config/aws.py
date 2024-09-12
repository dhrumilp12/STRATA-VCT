import boto3
import os

# Configure AWS credentials
boto3.setup_default_session(
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_REGION')
)

# Create a Bedrock client
bedrock = boto3.client('bedrock')

# Now you can use the bedrock object for operations