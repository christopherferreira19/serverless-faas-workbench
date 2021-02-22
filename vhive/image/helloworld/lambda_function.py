
def lambda_handler(event, context):
    if 'to' in event:
        to = event['to']
    else:
        to = 'World'

    return f'Hello {to}'
