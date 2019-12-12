#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: uploader.py
# Project: text-uploader
# File Created: Wednesday, 11th December 2019 10:02:48 pm
# Author: Jaseem Jas (jaseem@socialanimal.com)
# -----
# Last Modified: Wednesday, 11th December 2019 10:11:55 pm
# Modified By: Jaseem Jas (jaseem@socialanimal.com)
# -----
# Copyright 2016 - 2019 Socialanimal.com
###

from minio import Minio
from minio.error import ResponseError

from io import BytesIO

host = "localhost:9000"
access_key = "jaseem"
secret_key = "iamminio"

minioClient = Minio(host, access_key=access_key,
                    secret_key=secret_key, secure=False)

text = "My minio content"
bucket = "text"
content = BytesIO(bytes(text, 'utf-8'))
key = 'sample.text'
size = content.getbuffer().nbytes

try:
    minioClient.put_object(bucket, key, content, size)
    print("Done!")
except ResponseError as err:
    print("error:", err)
