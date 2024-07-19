
import boto3

from mypy_boto3_s3.client import S3Client


def upload(path: str) -> None:
    """
    Uploads the file at the provided 'path' to S3.

    Args:
        path (str): The absolute path to the file to be uploaded.
    """

    s3_bucket = 'wheelerrecommends-scraper-data'
    s3_object = path[len('/tmp/scraper/')::]

    print(f'scraper-B657EF81s0617s4BA0s95B: upload {path} to {s3_bucket}/{s3_object}')

    try:
        __create_s3_client().upload_file(path, s3_bucket, s3_object)

    except Exception as e:
        print(f"scraper-0B04122Fs466Ds468As9F3: exception: '{e}'")


def __create_s3_client() -> S3Client:
    return boto3.client('s3')

