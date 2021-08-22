import json


def say_hello_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World')
    }
