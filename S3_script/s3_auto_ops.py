import boto3
import os

#Create a bucket S3 first
bucket_name = 'mobxstream-bucket-hrishikesh'
region = 'ap-south-1'
local_upload_file = 'test_upload.txt'
s3_key = 'test-folder/test_upload.txt'
download_file_name = 'downloaded_test.txt'

s3 = boto3.client('s3', region_name=region)

def create_test_file():
    with open(local_upload_file, 'w') as f:
        f.write("This file was uploaded using Boto3 Python script.")
    print(f"Created file: {local_upload_file}")

def upload_file():
    s3.upload_file(local_upload_file, bucket_name, s3_key)
    print(f"Uploaded '{local_upload_file}' to S3 as '{s3_key}'")

def list_files():
    print(f"Listing files in bucket '{bucket_name}':")
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']} ({obj['Size']} bytes)")
    else:
        print("Bucket is empty.")

def download_file():
    s3.download_file(bucket_name, s3_key, download_file_name)
    print(f"Downloaded '{s3_key}' to '{download_file_name}'")

def delete_file():
    s3.delete_object(Bucket=bucket_name, Key=s3_key)
    print(f"Deleted '{s3_key}' from bucket")

def cleanup_local():
    for file in [local_upload_file, download_file_name]:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed local file: {file}")

if __name__ == "__main__":
    create_test_file()
    upload_file()
    list_files()
    download_file()
    delete_file()
    cleanup_local()
    print("Done with upload → list → download → delete")
