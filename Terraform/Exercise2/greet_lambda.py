import os

def lambda_handler(event, context):
    print("Udacity Exercise to deploy an AWS Lambda Function using Terraform !")
    return "{} from Lambda!".format(os.environ['greeting'])
