#5.push to s3 part
import logging
import boto3
from botocore.exceptions import ClientError
import os
from string import Template


session = boto3.Session(
    aws_access_key_id='AKIA2NK3YLUJZ2PEE4T4',
    aws_secret_access_key='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',
)


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Get the list of all files and directories
path = "/home/amitha/PycharmProjects/bigdataproject/output"
dir_list = os.listdir(path)


fileToUpload = []
# prints all files
for file in dir_list:
    if file.endswith(".json"):
        fileToUpload.append(file)

print(fileToUpload)

for f in fileToUpload:
    fullPath = Template('/home/amitha/PycharmProjects/bigdataproject/output/$f')
    print("Uploading",f, upload_file(fullPath.substitute(f=f), "myweatherawsbucket"))