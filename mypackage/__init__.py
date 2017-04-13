import sys
import boto3

def foo():
    bar(boto3.resource('dynamodb', region_name='us-east-2'))
    sys.exit(0)


# Unable to reproduce if merge this function with foo()
def bar(dynamodb):
    import mypackage.justtyping  # Unable to reproduce without this line

    # Unable to reproduce if do not get item twice, or use `dynamodb` in both
    # cases, or create new resource in both cases.
    # Note that the table must exist, but it does not need to have the item.
    dynamodb.Table('sigsegv').get_item(Key={'pkey': 'xxx'})
    boto3.resource('dynamodb', region_name='us-east-2').Table('sigsegv').get_item(Key={'pkey': 'xxx'})
