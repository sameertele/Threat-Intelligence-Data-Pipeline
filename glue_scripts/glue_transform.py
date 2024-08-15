#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import tarfile
import boto3
import os
import email

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Extracting file in S3
s3 = boto3.client('s3')
bucket = 'enron-spam-detection-data'
key = 'raw/enron_mail_20150507.tar.gz'
local_tar = '/tmp/enron_mail_20150507.tar.gz'
local_extract_dir = '/tmp/enron_mail/'

s3.download_file(bucket, key, local_tar)

with tarfile.open(local_tar, 'r:gz') as tar:
    tar.extractall(path=local_extract_dir)

# Processing extracted files
data = []
for root, dirs, files in os.walk(local_extract_dir):
    for filename in files:
        if filename.endswith('.txt'):
            with open(os.path.join(root, filename), 'r', encoding='latin1') as f:
                msg = email.message_from_file(f)
                subject = msg['Subject']
                body = msg.get_payload(decode=True).decode('latin1', errors='ignore')
                
                # label
                label = 1 if 'spam' in root.lower() else 0
                
                data.append({
                    'subject': subject,
                    'message': body,
                    'label': label
                })

df = spark.createDataFrame(data)

df.write.json('s3://enron-spam-detection-data/processed/')

job.commit()

