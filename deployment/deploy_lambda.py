#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

lambda_client = boto3.client('lambda')

functions = ['data_collection.py', 'lambda_trigger_sagemaker.py']

for function in functions:
    with open(f'lambda_functions/{function}', 'rb') as f:
        lambda_client.create_function(
            FunctionName=function.split('.')[0],
            Runtime='python3.8',
            Role='arn:aws:iam::your-account-id:role/lambda-ex',
            Handler=f'{function.split(".")[0]}.lambda_handler',
            Code={'ZipFile': f.read()},
            Timeout=300  
        )

