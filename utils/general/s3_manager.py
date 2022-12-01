import warnings
import boto3
warnings.filterwarnings("ignore")
import json
import sys


class S3Manager:
    def __init__(self) -> None:
        self.endpoint_url = "s3.amazonaws.com"
        self.access_key_url = "AKIA2GA5YBIEWQ24PNXN"
        self.secret_access_key = "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"
        self.region = "us-east-1"

        # self.bucket = bucket

        self.s3_resource = boto3.resource(
            "s3",
            # endpoint_url = self.endpoint_url,
            aws_access_key_id = self.access_key_url,
            aws_secret_access_key = self.secret_access_key,
            region_name = self.region
        )

    def upload_object_file_to_bucket(self, bucket, content_name, content, file_path):
        self.s3_resource.Bucket(bucket).put_object(Key=f"{file_path}/{content_name}", Body=content)

    def upload_file_to_bucket(self, bucket, file_path, destination_path):
        self.s3_resource.Bucket(bucket).upload_file(file_path, destination_path)

    def download_file_from_bucket(self, bucket, remote_path, destination_path):
        self.s3_resource.Bucket(bucket).download_file(remote_path, destination_path)