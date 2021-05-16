def lambda_handler(event, context):

    if 'Item' in event['DynamoDB']:
        item = event['DynamoDB']['Item']

    else:
        item = None

    return item