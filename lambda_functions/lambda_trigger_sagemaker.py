#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

def lambda_handler(event, context):
    client = boto3.client('sagemaker')
    
    response = client.create_model(
        ModelName='enron-spam-detection-model',
        PrimaryContainer={
            'Image': '123456789012.dkr.ecr.us-west-2.amazonaws.com/linear-learner:latest',
            'ModelDataUrl': 's3://enron-spam-detection-data/models/model.tar.gz'
        },
        ExecutionRoleArn='arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole-20200101T000001'
    )
    
    client.create_endpoint_config(
        EndpointConfigName='EnronSpamDetectionEndpointConfig',
        ProductionVariants=[
            {
                'VariantName': 'AllTraffic',
                'ModelName': 'enron-spam-detection-model',
                'InstanceType': 'ml.m4.xlarge',
                'InitialInstanceCount': 1
            }
        ]
    )
    
    client.create_endpoint(
        EndpointName='EnronSpamDetectionEndpoint',
        EndpointConfigName='EnronSpamDetectionEndpointConfig'
    )
    
    return {
        'statusCode': 200,
        'body': 'Model deployed successfully'
    }

