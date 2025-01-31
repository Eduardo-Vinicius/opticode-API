import json
from app.function.router import route_event

def lambda_handler(event, context):
    try:
        print("Evento recebido:", json.dumps(event))  # Log para debug

        # O path correto vem direto do evento no API Gateway
        path = event.get("requestContext", {}).get("http", {}).get("path", "")

        # Body pode estar codificado como string JSON, então precisa ser carregado corretamente
        body = event.get("body", "{}")
        if isinstance(body, str):
            body = json.loads(body)  # Decodifica a string JSON para dicionário

        # Roteia o evento corretamente
        response = route_event({"path": path, "body": body})

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