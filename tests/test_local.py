import json
from src.handler import lambda_handler

def test_lambda_handler_calcular_distancias():
    locais = [
        "Av. Paulista, 1578 - São Paulo, SP",
        "Rua Augusta, 2000 - São Paulo, SP",
        "Praça da Sé - São Paulo, SP"
    ]
    # Simulação de um evento típico da API Gateway
    event = {
        'httpMethod': 'POST',
        'path': '/calcular_distancias',
        'body': json.dumps({
            'locais': locais
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

    context = {}  # Contexto do Lambda (não utilizado neste exemplo, mas pode ser configurado conforme necessário)

    # Chama a função lambda_handler com o evento simulado
    response = lambda_handler(event, context)

    print("Response:")
    print(response)


def test_lambda_handler_calcular_melhor_rota():
    locais = [
        "Av. Paulista, 1578 - São Paulo, SP",
        "Rua Augusta, 2000 - São Paulo, SP",
        "Praça da Sé - São Paulo, SP"
    ]
    # Simulação de um evento típico da API Gateway
    event = {
        'httpMethod': 'POST',
        'path': '/calcular_melhor_rota',
        'body': json.dumps({
            'locais': locais
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

    context = {}  # Contexto do Lambda (não utilizado neste exemplo, mas pode ser configurado conforme necessário)

    # Chama a função lambda_handler com o evento simulado
    response = lambda_handler(event, context)

    print("Response:")
    print(response)


if __name__ == "__main__":
    test_lambda_handler_calcular_distancias()
    test_lambda_handler_calcular_melhor_rota()
