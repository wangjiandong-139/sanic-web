import io
import logging
import os
from datetime import timedelta
from minio import Minio
import traceback
from sanic import Request
from constants.code_enum import SysCodeEnum as SysCode

from common.exception import MyException


class MinioUtils:
    """
    上传文件工具类
    """

    _client = None

    def __init__(self):
        pass

    @staticmethod
    def _build_client():
        """初始化MinIO客户端"""
        if os.getenv("ENV") == "test":
            minio_endpoint = os.getenv("MINIO_ENDPOINT_TEST")
        else:
            minio_endpoint = os.getenv("MINIO_ENDPOINT_DEV")

        access_key = os.getenv("MINIO_ACCESS_KEY")
        secret_key = os.getenv("MiNIO_SECRET_KEY")
        return Minio(endpoint=minio_endpoint, access_key=access_key, secret_key=secret_key, secure=False)

    def ensure_bucket(self, bucket_name):
        """确保bucket存在，不存在则创建"""
        client = self._build_client()
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
        else:
            print(f"Bucket '{bucket_name}' already exists.")

    def upload_file_from_request(self, request: Request, bucket_name="filedata", expires=timedelta(days=7)):
        """
        从请求中读取文件数据并上传到MinIO服务器，返回预签名URL。

        参数:
        - request: Sanic请求对象
        - bucket_name: 存储桶名称
        - expires: 链接过期时间（秒），默认为3600秒

        返回:
        - 预签名URL链接
        """
        try:
            client = self._build_client()
            # 获取文件数据
            file_data = request.files.get("file")  # 假设表单数据中的文件字段名为 'file'
            if not file_data:
                raise MyException(SysCode.c_9999)

            # 确保 file_data 是一个包含文件信息的列表
            file_stream = io.BytesIO(file_data.body)
            file_length = len(file_data.body)
            object_name = file_data.name  # 获取文件名作为对象名

            # 上传文件
            client.put_object(bucket_name, object_name, file_stream, file_length, file_data.type)
            logging.info(f"File successfully uploaded as {object_name}.")

            return {"object_key": object_name}
        except Exception as err:
            traceback.print_exception(err)
            raise MyException(SysCode.c_9999)

    def get_file_url_by_key(self, bucket_name="filedata", object_key=None):
        """
        通过object_key获取文件url
        """
        try:
            client = self._build_client()
            # 生成预签名URL
            resigned_url = client.presigned_get_object(bucket_name, object_key, expires=timedelta(days=7))
            return resigned_url
        except Exception as err:
            traceback.print_exception(err)
            raise MyException(SysCode.c_9999)  # 假设 SysCode.c_9999 是通用错误代码
