#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import pandas as pd
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri
from sagemaker.estimator import Estimator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Loading data from S3
s3 = boto3.client('s3')
bucket = 'enron-spam-detection-data'
key = 'processed/enron_spam_data.json'

obj = s3.get_object(Bucket=bucket, Key=key)
data = pd.read_json(obj['Body'])

# Feature extraction
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['message'])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Uploading data to S3 for SageMaker
train_location = 's3://enron-spam-detection-data/models/train.csv'
test_location = 's3://enron-spam-detection-data/models/test.csv'

pd.DataFrame(X_train.toarray()).to_csv(train_location, index=False)
pd.DataFrame(X_test.toarray()).to_csv(test_location, index=False)

# SageMaker Estimator
role = get_execution_role()
container = get_image_uri(boto3.Session().region_name, 'linear-learner')

estimator = Estimator(
    container,
    role,
    instance_count=1,
    instance_type='ml.m4.xlarge',
    output_path='s3://enron-spam-detection-data/models/'
)

# Train the model
estimator.fit({'train': train_location, 'test': test_location})

