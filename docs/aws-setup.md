# AWS Setup Guide

This guide will help you set up AWS CLI configuration on your local machine.

## Step 1: Create AWS Configuration Directory

First, create a directory to store your AWS configuration files.

```sh
mkdir -p .aws
```

## Step 2: Set Environment Variables

Set the environment variables to point to your AWS configuration and credentials files.

```sh
export AWS_CONFIG_FILE=$(pwd)/.aws/config
export AWS_SHARED_CREDENTIALS_FILE=$(pwd)/.aws/credentials
```

## Step 3: Configure AWS CLI

Run the following command to configure your AWS CLI. You will be prompted to enter your AWS Access Key, Secret Key, region, and output format.

```sh
aws configure
```

## Step 4: Verify Configuration

To verify that your AWS CLI is configured correctly, run:

```sh
aws configure list
```

This command will list the configuration values that are currently set.
