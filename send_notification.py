# send_sns.py
import boto3
import sys
import os

status = sys.argv[1]
subject = f"Test Pipeline {status.upper()}"
message = f"The GitHub Actions test pipeline has {status}."

sns = boto3.client('sns', region_name=os.environ['AWS_REGION'],
                   aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                   aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

sns.publish(
    TopicArn=os.environ['SNS_TOPIC_ARN'],
    Subject=subject,
    Message=message
)
