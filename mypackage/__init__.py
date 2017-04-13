import sys
import boto3

def foo():
    bar(boto3.resource('dynamodb', region_name='us-east-2'))
    sys.exit(0)


def bar(dynamodb):
    import mypackage.justtyping

    dynamodb.Table('sigsegv').get_item(Key={'pkey': 'xxx'})
    boto3.resource('dynamodb', region_name='us-east-2').Table('sigsegv').get_item(Key={'pkey': 'xxx'})
