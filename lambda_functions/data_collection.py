#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import requests
import zipfile
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    url = "https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz"
    response = requests.get(url)
    
    local_path = '/tmp/enron_mail_20150507.tar.gz'
    with open(local_path, 'wb') as f:
        f.write(response.content)
    
    s3.upload_file(local_path, 'enron-spam-detection-data', 'raw/enron_mail_20150507.tar.gz')
    
    return {
        'statusCode': 200,
        'body': 'Enron Email data collected and uploaded to S3.'
    }

