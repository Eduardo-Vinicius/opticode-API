# Cálculo de Custo de Combustível com Google Maps API

Este projeto calcula o custo de combustível para percursos usando a API do Google Maps. Ele é implementado em Python e pode ser executado localmente ou implantado em um serviço de cloud computing como AWS Lambda.

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Execução Local](#execução-local)
4. [Publicação no AWS Lambda](#publicação-no-aws-lambda)
5. [Referências](#referências)

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes pré-requisitos:

- [Python 3.6 ou superior](https://www.python.org/downloads/)
- [Conta no Google Cloud Platform](https://cloud.google.com/)
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/) (para deployment no AWS Lambda)
- [Google Maps API Key](https://developers.google.com/maps/gmp-get-started)

## Configuração do Ambiente

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um Ambiente Virtual e Instale as Dependências**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure a Chave da API do Google Maps**

Crie um arquivo config.py na raiz do projeto com o seguinte conteúdo:

   ```python
   GOOGLE_MAPS_API_KEY = 'SUA_CHAVE_DE_API_AQUI'
   ```

Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave da API do Google Maps.

## Execução Local

Para rodar o código localmente e testar o cálculo de custo de combustível:

1. **Executar o Script**
2. **Verifique a Saída**

## Publicação no AWS Lambda

Para publicar o projeto no AWS Lambda usando o Serverless Framework:

1. **Instale o Serverless Framework**

    ```bash
    npm install -g serverless
    ```

2. **Configure o Serverless Framework**

Crie um arquivo serverless.yml na raiz do projeto com o seguinte conteúdo:

   ```yaml
   service: calculo-combustivel

    provider:
      name: aws
      runtime: python3.9
      region: us-east-1
      environment:
        GOOGLE_MAPS_API_KEY: ${env:GOOGLE_MAPS_API_KEY}
      iamRoleStatements:
        - Effect: "Allow"
          Action:
            - "dynamodb:*"
          Resource: "arn:aws:dynamodb:us-east-1:*:table/my-dynamodb-table"
    
    functions:
      calcularCustoCombustivel:
        handler: src/handlers/calcular_custo.handler
        events:
          - http:
              path: calcular-custo
              method: post
   ```

3. **Deploy no AWS Lambda**

   ```bash
   serverless deploy
   ```

Isso criará e implantará a função Lambda e configurará o API Gateway para expor o endpoint HTTP.

4. **Teste a Função Lambda**

Após o deploy, você pode testar sua função Lambda usando o endpoint HTTP fornecido pelo API Gateway. Use ferramentas como curl, Postman ou diretamente no seu navegador para fazer uma requisição POST para o endpoint configurado.

## Referências

- [Documentação do Google Maps Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview)
- [Documentação do Serverless Framework](https://www.serverless.com/framework/docs/)
- [Documentação do AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
