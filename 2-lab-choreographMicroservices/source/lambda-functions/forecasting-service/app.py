import time
import boto3
import os
import json
from datetime import datetime
'''
Lambda func for forecasting service
'''


def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_forecasting_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })


def lambda_handler(event, context):
    print(event)
    print('forecasting_service is called')
    data = event['detail']['data']
    save_to_db(data['ID'])
    response = {'status': 200}
    return response
