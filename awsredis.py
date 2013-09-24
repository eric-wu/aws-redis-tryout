#!/usr/bin/python

import boto
import os

conn = boto.connect_s3()
bucket = conn.get_bucket('prod.access.record.sagebase.org')
resultset = bucket.list(prefix='000000010/')

for key in resultset:
    file_name = 'data/'+ key.name
    dir_name = os.path.dirname(file_name)
    print(dir_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    log_file = open(file_name, 'w+')
    key.get_contents_to_filename(file_name)
    key.close()
    log_file.close()

