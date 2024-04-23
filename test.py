import pandas as pd
import dotenv
from dotenv import load_dotenv
import os
import boto3


env = load_dotenv()


s3 = boto3.resource('s3', aws_access_key_id=os.getenv("access_Key"),
                                 aws_secret_access_key=os.getenv("secret_access_key"))
for bucket in s3.buckets.all():
    print(bucket.name)