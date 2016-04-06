"""
This module implement Amazon AWS S3 adapter for Flask-Imagine
"""
import boto
from flask.ext.imagine.adapters.interface import ImagineAdapterInterface


class FlaskImagineS3Adapter(ImagineAdapterInterface):
    """
    Amazon AWS S3 storage adapter
    """
    s3_conn = None
    bucket = None

    def __init__(self, access_key, secret_key, bucket_name):
        """
        Init adapter
        :param access_key: str
        :param secret_key: str
        :param bucket_name: str
        """
        self.s3_conn = boto.connect_s3(access_key, secret_key)
        self.bucket = self.s3_conn.create_bucket(bucket_name)

    def get_item(self, path):
        """
        Get resource item
        :param path: string
        :return: Image
        """
        item = self.bucket.get_key(path)

        return item.get_contents_as_string()
