# **Project SEC Lambda**

## **About The Project**

This project involves creating two AWS Lambda functions in Python to automate the retrieval and processing of SEC Edgar data. By leveraging AWS services like Lambda, S3, and EventBridge, we aim to efficiently handle SEC filings for company financial documents.

### **Use Cases**

- **Lambda Function 1**: Automates the daily download of SEC Edgar JSON files and uploads them to an S3 bucket.
- **Lambda Function 2**: Processes user requests for 10-K (annual) and 10-Q (quarterly) financial documents and retrieves the content.

## **Built With**

- **Python**
- **AWS Lambda**
- **AWS S3**
- **AWS EventBridge**
- **Boto3 (AWS SDK for Python)**
- **Requests library**

## **Usage**

### **Lambda Function 1: Download and Upload SEC Edgar JSON Files**

**Purpose**: Automatically download the latest `company_tickers.json` file from the SEC website and upload it to an S3 bucket daily.

**How AWS Works with It**:

- **AWS Lambda**: Runs the Python script without managing servers.
- **Amazon S3**: Stores the JSON file with versioning enabled.
- **AWS EventBridge**: Schedules the Lambda function to run daily.

### **Lambda Function 2: Process Requests for 10-K and 10-Q Documents**

**Purpose**: Respond to user requests by retrieving the specified financial documents from the SEC and returning the content.

**How AWS Works with It**:

- **AWS Lambda**: Processes incoming requests and executes the logic.
- **Amazon S3**: Stores necessary data files for lookup (e.g., `company_tickers.json`).
- **Boto3**: AWS SDK used to interact with S3 within the Lambda function.

## **Roadmap**

- **Enhancements**:

  - Implement error handling and logging for better monitoring.
  - Optimize the functions for performance and cost-efficiency.
  - Secure the S3 bucket and Lambda functions with proper IAM roles and policies.

- **Potential Features**:

  - Integrate with AWS API Gateway to expose the Lambda functions as APIs.
  - Add a front-end interface for user interactions.
  - Expand support for additional SEC filings and data processing.

## **Contact**

- **Sean Onamade**
- **Email**: sean.d.onamade@vanderbilt.edu

## **Acknowledgments**

- **AWS Documentation**
- **SEC Edgar**
- **Open-Source Libraries**
- **Gerard Spivey w/ MLT**
