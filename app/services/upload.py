import boto3
import uuid
from botocore.client import Config
import io
from core.config import settings

BUCKET_NAME = settings.BUCKET_NAME
ACCESS_KEY_ID = settings.ACCESS_KEY_ID
SECRET_ACCESS_ID = settings.SECRET_ACCESS_ID

s3 = boto3.resource(
    "s3",
    aws_access_key_id=settings.ACCESS_KEY_ID,
    aws_secret_access_key=settings.SECRET_ACCESS_ID,
    config=Config(signature_version="s3v4"),
)


async def upload_file(data: bytes, filename: str):
    image = io.BytesIO(data)
    filename_s3 = str(uuid.uuid4()) + filename
    s3.Bucket(BUCKET_NAME).put_object(Key=filename_s3, Body=image)
    url = f"https://{BUCKET_NAME}.s3.ap-southeast-1.amazonaws.com/{filename_s3}"
    return url
