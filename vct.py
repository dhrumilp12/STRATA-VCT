import requests
import json
import gzip
import io
import time
import os
from io import BytesIO
import re
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

S3_BUCKET_URL = "https://vcthackathon-data.s3.us-west-2.amazonaws.com"
TARGET_S3_BUCKET = "vct-data-challengers-2024"  # Replace with your target S3 bucket name
AWS_REGION = "us-east-2"  # Replace with your target region

# (game-changers, vct-international, vct-challengers)
LEAGUE = "vct-challengers"

# (2022, 2023, 2024)
YEAR = 2024

# Initialize S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION)

# Function to sanitize filenames
def sanitize_filename(filename):
    # Remove or replace characters that are invalid in Windows filenames
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def upload_to_s3(file_content, s3_key):
    try:
        s3_client.put_object(
            Bucket=TARGET_S3_BUCKET,
            Key=s3_key,
            Body=file_content,
            ContentType='application/json'
        )
        logging.info(f"Uploaded {s3_key} to S3.")
        return True
    except (NoCredentialsError, ClientError) as e:
        logging.error(f"Failed to upload {s3_key} to S3: {e}")
        return False

def download_gzip_and_upload_to_s3(file_name):
    remote_file = f"{S3_BUCKET_URL}/{file_name}.json.gz"
    response = requests.get(remote_file, stream=True)

    if response.status_code == 200:
        gzip_bytes = BytesIO(response.content)
        try:
            with gzip.GzipFile(fileobj=gzip_bytes, mode="rb") as gzipped_file:
                file_content = gzipped_file.read()
                
                # Split the file path into directory and base file name
                directory, base_file_name = os.path.split(file_name)
                
                # Sanitize only the base file name for uploading (optional)
                sanitized_file_name = sanitize_filename(base_file_name)
                
                # Reconstruct the S3 key with sanitized file name
                s3_key = f"{directory}/{sanitized_file_name}.json"
                
                upload_success = upload_to_s3(file_content, s3_key)
                return upload_success
        except gzip.BadGzipFile:
            logging.error(f"Error: The file {file_name}.json.gz is not a valid gzip file.")
            return False
        except Exception as e:
            logging.error(f"Unexpected error while processing {file_name}: {e}")
            return False
    elif response.status_code == 404:
        # Log missing files with detailed information
        logging.warning(f"File not found at {remote_file}. Expected at: {file_name}.json.gz")
        return False
    else:
        logging.error(f"Failed to download {file_name}: Status code {response.status_code}")
        return False


def download_esports_files():
    directory = f"{LEAGUE}/esports-data"

    esports_data_files = ["leagues", "tournaments", "players", "teams", "mapping_data"]
    for file_name in esports_data_files:
        logging.info(f"Processing file: {file_name}")
        download_gzip_and_upload_to_s3(f"{directory}/{file_name}")

def download_games():
    start_time = time.time()

    # Define the S3 key for the mapping file
    mapping_s3_key = f"{LEAGUE}/esports-data/mapping_data.json"

    try:
        # Download the mapping_data.json from S3
        mapping_response = s3_client.get_object(Bucket=TARGET_S3_BUCKET, Key=mapping_s3_key)
        mappings_data = json.loads(mapping_response['Body'].read())
        logging.info(f"Retrieved mapping data from S3: {mapping_s3_key}")
    except ClientError as e:
        logging.error(f"Failed to retrieve mapping data from S3: {e}")
        return

    game_counter = 0

    for esports_game in mappings_data:
        original_game_id = esports_game.get("platformGameId")
        if not original_game_id:
            logging.warning("Missing 'platformGameId' in esports_game entry. Skipping.")
            continue

        # Use the original_game_id without sanitization for downloading
        s3_game_file = f"{LEAGUE}/games/{YEAR}/{original_game_id}"

        logging.info(f"Processing game: {original_game_id}")
        response = download_gzip_and_upload_to_s3(s3_game_file)
        
        if response:
            game_counter += 1
            if game_counter % 10 == 0:
                elapsed_minutes = round((time.time() - start_time)/60, 2)
                logging.info(f"----- Processed {game_counter} games, current run time: {elapsed_minutes} minutes")


if __name__ == "__main__":
    download_esports_files()
    download_games()
