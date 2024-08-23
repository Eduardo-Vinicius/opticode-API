import json
import pytest
from src.handler import lambda_handler

def test_lambda_handler_calcular_distancias():
    locais = [
    "Av. Paulista, 1578 - São Paulo, SP",
    "Rua Augusta, 2000 - São Paulo, SP",
    "Praça da Sé - São Paulo, SP",
    "Avenida 23 de Maio, 1000 - São Paulo, SP",
    "Rua da Consolação, 1234 - São Paulo, SP",
    "Parque Ibirapuera - São Paulo, SP"
    ]

    
    event = {
        'httpMethod': 'POST',
        'path': '/calcular_distancias',
        'body': json.dumps({
            'locais': locais,
            'origem': 'Rua Um, 10 Jardim Tres coracoes - Sao Paulo SP',
            'destino': 'R. Roger Bacon, 87 - Jardim Morais Prado, São Paulo - SP',
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

    context = {}  # Contexto do Lambda (não utilizado neste exemplo, mas pode ser configurado conforme necessário)

    response = lambda_handler(event, context)

    # Imprimir a resposta, garantindo que os caracteres especiais sejam exibidos corretamente
    print("Response:")
    print(json.dumps(response, ensure_ascii=False, indent=2))

    # Adicionar asserções para validar a resposta, dependendo do que espera da função lambda_handler
    assert response['statusCode'] == 200
    # Adicione mais asserções baseadas na estrutura e conteúdo esperados da resposta


def test_lambda_handler_calcular_melhor_rota():
    locais = [
    "Av. Paulista, 1578 - São Paulo, SP",
    "Rua Augusta, 2000 - São Paulo, SP",
    "Praça da Sé - São Paulo, SP",
    "Avenida 23 de Maio, 1000 - São Paulo, SP",
    "Rua da Consolação, 1234 - São Paulo, SP"
    ]

    
    event = {
        'httpMethod': 'POST',
        'path': '/calcular_distancias',
        'body': json.dumps({
            'locais': locais,
            'origem': 'Rua Um, 10 Jardim Tres coracoes - Sao Paulo SP',
            'destino': 'R. Roger Bacon, 87 - Jardim Morais Prado, São Paulo - SP',
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


    context = {}  # Contexto do Lambda (não utilizado neste exemplo, mas pode ser configurado conforme necessário)

    response = lambda_handler(event, context)

    # Imprimir a resposta, garantindo que os caracteres especiais sejam exibidos corretamente
    print("Response:")
    print(json.dumps(response, ensure_ascii=False, indent=2))

    # Adicionar asserções para validar a resposta, dependendo do que espera da função lambda_handler
    assert response['statusCode'] == 200
    # Adicione mais asserções baseadas na estrutura e conteúdo esperados da resposta

if __name__ == "__main__":
    #pytest.main()
    test_lambda_handler_calcular_distancias()
    test_lambda_handler_calcular_melhor_rota()
