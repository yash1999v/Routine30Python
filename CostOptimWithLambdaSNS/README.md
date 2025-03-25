# AWS EBS Snapshot Cleanup

## Overview
This AWS Lambda function automates the cleanup of stale EBS snapshots to optimize AWS costs. It performs the following actions:
- Lists all EBS snapshots owned by the account.
- Deletes snapshots older than 6 months if they have no associated volume.
- Sends SNS alerts for snapshots older than 3 months if their associated volume was deleted.
- Runs bi-weekly using AWS CloudWatch Events.

## Prerequisites
Ensure you have the following:
- **AWS IAM Role:** The Lambda function needs an IAM role with permissions to access EC2, SNS, and CloudTrail.
- **AWS SNS Topic:** Create an SNS topic to receive stale snapshot alerts.
- **AWS Lambda:** An AWS Lambda function set up with Python 3.x runtime.

## Deployment Steps
### 1. Clone the Repository
```sh
git clone https://github.com/yash1999v/DevOps-Portfolio.git
cd DevOps-Portfolio
```

### 2. Install Dependencies (if required)
```sh
pip install boto3
```

### 3. Configure AWS Credentials
Ensure your AWS CLI is configured or set environment variables:
```sh
aws configure
```
Or manually set environment variables:
```sh
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1  # Change as needed
```

### 4. Create an SNS Topic
1. Go to **AWS SNS Console**.
2. Click on **Create Topic** and select **Standard**.
3. Name your topic (e.g., `StaleSnapshotAlerts`).
4. Copy the Topic ARN for later use.
5. Subscribe an email or Lambda to receive notifications.

### 5. Set Up IAM Role for Lambda
1. Go to **AWS IAM Console**.
2. Click **Roles** > **Create Role**.
3. Select **AWS Lambda** as the trusted entity.
4. Attach the following policies:
   - `AmazonEC2ReadOnlyAccess`
   - `AWSCloudTrailReadOnlyAccess`
   - `AmazonSNSFullAccess`
   - Create a custom policy for snapshot deletion with:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "ec2:DeleteSnapshot",
           "Resource": "*"
         }
       ]
     }
     ```
5. Attach this role to the Lambda function.

### 6. Deploy the Lambda Function
1. Open the **AWS Lambda Console**.
2. Click **Create Function** > **Author from Scratch**.
3. Set **Function Name** (e.g., `EBS_Snapshot_Cleanup`).
4. Select **Python 3.x** as the runtime.
5. Choose the IAM Role created earlier.
6. Upload the script as a `.zip` file or paste the code manually.
   - You can find the script here: [lambda_function.py](https://github.com/yash1999v/Routine30Python/blob/main/CostOptimWithLambdaSNS/lambda_function.py)
7. Set environment variables in the **Configuration** tab:
   ```sh
   AWS_REGION = "us-east-1"
   SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:StaleSnapshotAlerts"
   ```
8. Save and deploy the function.

### 7. Configure CloudWatch Trigger
1. Go to **AWS CloudWatch Console**.
2. Navigate to **Rules** and create a new rule.
3. Select **Event Source** as **Schedule**.
4. Set schedule expression as `rate(14 days)` (bi-weekly execution).
5. Choose **Lambda function** as the target and select the deployed function.
6. Save the rule.

### 8. Monitor and Validate
- **Check AWS CloudWatch Logs**: Monitor logs to verify execution and errors.
- **Validate SNS Alerts**: Ensure email notifications are received.
- **Review Deleted Snapshots**: Confirm snapshots older than 6 months are deleted.

## License
This project is licensed under the MIT License.

