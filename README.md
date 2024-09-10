# Threat Intelligence Data Pipeline

## Overview

The Threat Intelligence Data Pipeline is a robust data pipeline designed to collect, process, and analyze threat intelligence data from various sources. This project utilizes the PhishTank dataset to automate the data ingestion and analysis process, implementing machine learning algorithms to classify and prioritize threat indicators.

## Features

- **Data Collection**: Automated collection of phishing data from the PhishTank dataset.
- **Data Processing**: Uses AWS Glue for data transformation and cleaning.
- **Data Storage**: Stores processed data in Amazon S3 for further analysis.
- **Data Analysis**: Utilizes Amazon Athena for querying the data.
- **Machine Learning**: Implements machine learning models to classify phishing indicators and prioritize threats.
- **Automation**: Automated pipeline triggered using AWS Lambda functions.

## Dataset

This project utilizes the **PhishTank** dataset, which provides a comprehensive list of phishing URLs reported by users.

- **Dataset Link**: [PhishTank Dataset](https://www.phishtank.com/developer_info.php)
- **Files Used**: 
  - `phishTank_data.csv` (download the latest dataset)

### Dataset Preparation

1. Download the latest phishing data from the PhishTank website.
2. Save the CSV file in the `data/` directory as `phishTank_data.csv`.
