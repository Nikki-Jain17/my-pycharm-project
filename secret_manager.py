import boto3
import os
import base64
from cryptography.fernet import Fernet
import json

CONFIG_FILE_PATH = 'config.json'

# Fetch the encrypted values from GitHub secrets
encrypted_access_key = os.getenv('ENCRYPTED_AWS_ACCESS_KEY_ID')
encrypted_secret_key = os.getenv('ENCRYPTED_AWS_SECRET_ACCESS_KEY')
encrypted_region = os.getenv('ENCRYPTED_AWS_REGION')
encrypted_topic_arn = os.getenv('ENCRYPTED_SNS_TOPIC_ARN')


def load_key_from_config():
    # Load the privacy_key (derived key) from the config file
    if not os.path.exists(CONFIG_FILE_PATH):
        raise FileNotFoundError(f"Config file '{CONFIG_FILE_PATH}' not found.")

    with open(CONFIG_FILE_PATH, 'r') as file:
        config = json.load(file)
        # The key in the config file is already base64-encoded, no need to decode
        if 'privacy_key' not in config:
            raise KeyError("'privacy_key' is missing from config.json.")
        privacy_key = config['privacy_key'].encode()  # Convert it to bytes
        return privacy_key


def decrypt_value(encrypted_text, key):
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(base64.b64decode(encrypted_text.encode())).decode()
        return decrypted
    except Exception as e:
        raise ValueError(f"Error decrypting the value: {str(e)}")


def send_notification():
    if not all([encrypted_access_key, encrypted_secret_key, encrypted_region, encrypted_topic_arn]):
        raise Exception("Missing one or more environment variables needed for decryption.")

    # Step 1: Decrypt the secrets
    #encryption_key = load_key_from_config()
    encryption_key = os.getenv('ENCRYPTION_KEY')

    try:
        decrypted_access_key = decrypt_value(encrypted_access_key, encryption_key)
        decrypted_secret_key = decrypt_value(encrypted_secret_key, encryption_key)
        decrypted_region = decrypt_value(encrypted_region, encryption_key)
        decrypted_topic_arn = decrypt_value(encrypted_topic_arn, encryption_key)
    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")

    # Step 2: Send SNS notification using decrypted values
    try:
        client = boto3.client(
            'sns',
            region_name=decrypted_region,
            aws_access_key_id=decrypted_access_key,
            aws_secret_access_key=decrypted_secret_key
        )

        response = client.publish(
            TopicArn=decrypted_topic_arn,
            Message='Test execution completed. Allure report is generated and published.',
            Subject='Test Report Notification'
        )
        print("✅ SNS Notification Sent Successfully:", response)
    except Exception as e:
        raise Exception(f"Failed to send SNS notification: {str(e)}")


if __name__ == "__main__":
    try:
        send_notification()
    except Exception as e:
        print(f"Error: {e}")
