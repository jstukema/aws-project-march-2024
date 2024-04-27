import boto3
import os


class S3Connection:
    def __init__(self):
        pass

    def get_all_buckets(self):
        # Initialize the S3 resource
        s3 = boto3.resource('s3', aws_access_key_id=os.getenv("access_Key"),
                            aws_secret_access_key=os.getenv("secret_access_key"))

        # Retrieve all buckets
        buckets = [bucket.name for bucket in s3.buckets.all()]
        return buckets
        # Call the method to get all buckets

    all_buckets = get_all_buckets()
    print("All Buckets:", all_buckets)

    def read_file(self):
        pass

    def upload_file(self):
        pass

    def write_df(self):
        pass
