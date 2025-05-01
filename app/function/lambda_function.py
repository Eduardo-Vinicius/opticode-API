import json
from app.function.router import route_event

def extract_params(event: dict) -> dict:
    path_params = event.get("pathParameters", {})
    query_params = event.get("queryStringParameters", {})
    return {
        "pathParameters": path_params,
        "queryStringParameters": query_params
    }


def lambda_handler(event, context):
    try:
        print("Evento recebido:", json.dumps(event))  # Log para debug

        path = ""
        method = ""
        # O path correto vem direto do evento no API Gateway
        if event.get('origin') == 'lambda':
            path = event.get("path", "")
            method = event.get("method", "")
        else:
            path = event.get("requestContext", {}).get("http", {}).get("path", "")
            method = event.get("requestContext", {}).get("http", {}).get("method", "")

        # Body pode estar codificado como string JSON, então precisa ser carregado corretamente
        body = event.get("body", "{}")
        if isinstance(body, str):
            body = json.loads(body)  # Decodifica a string JSON para dicionário

        params = extract_params(event)
        # Roteia o evento corretamente
        response = route_event({"path": path, "body": body, "method": method, "params": params})

        return {
            "statusCode": 200,
            "body": json.dumps(response),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }