import boto3
from botocore.exceptions import NoCredentialsError, ClientError

s3 = boto3.client('s3') 

# Set your bucket name
BUCKET_NAME = 'preet-bucket-mobxstream'

def upload_file_to_s3(file_name, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = file_name 
    try:
        s3.upload_file(file_name, BUCKET_NAME, object_name)
        print(f"Upload successful: {file_name} → s3://{BUCKET_NAME}/{object_name}")
    except FileNotFoundError:
        print("File not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"Client error: {e}")

def download_file_from_s3(object_name, download_path=None):
    """Download a file from an S3 bucket."""
    if download_path is None:
        download_path = object_name 
    try:
        s3.download_file(BUCKET_NAME, object_name, download_path)
        print(f"Download successful: s3://{BUCKET_NAME}/{object_name} → {download_path}")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"Client error: {e}")

def delete_file_from_s3(object_name):
    """Delete a file from an S3 bucket."""
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"Deleted: s3://{BUCKET_NAME}/{object_name}")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    local_file = 'example.txt'
    s3_object_name = 'uploads/example.txt'

    upload_file_to_s3(local_file, s3_object_name)
    download_file_from_s3(s3_object_name, 'downloaded_example.txt')
    delete_file_from_s3(s3_object_name)
