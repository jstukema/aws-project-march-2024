import pandas as pd
from dotenv import load_dotenv
import os
import boto3


env = load_dotenv()


# s3 = boto3.resource('s3', aws_access_key_id=os.getenv("access_Key"),
#                                  aws_secret_access_key=os.getenv("secret_access_key"))
# for bucket in s3.buckets.all():
#     print(bucket.name)

client = boto3.client('s3', aws_access_key_id=os.getenv("access_Key"),
                                 aws_secret_access_key=os.getenv("secret_access_key"))


response = client.get_object(Bucket="data-analytics-p", Key="DWP Pension Regulator/Data Analyst Interview Task - 2024.csv")

print(response.keys())

status = response.get('ResponseMetadata', {}).get('HTTPStatusCode', {})

if status == 200:

    print(f"Successfully pulled the data: status - {status}")
    # Read the CSV using different encodings
    encodings_to_try = ['utf-8', 'latin-1', 'unicode_escape']
    for encoding in encodings_to_try:
        try:
            df = pd.read_csv(response['Body'], encoding=encoding)
            print("Successfully decoded using encoding:", encoding)
            break  # Stop trying encodings if successful
        except UnicodeDecodeError:
            print("Failed to decode using encoding:", encoding)
else:
    print(f"Unable to pull the data: status - {status}")
