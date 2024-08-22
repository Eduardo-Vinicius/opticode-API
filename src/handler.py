import json
from src.router import route_event

def lambda_handler(event, context):
    try:
        if isinstance(event, str):
            event = json.loads(event)

        response = route_event(event)
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
