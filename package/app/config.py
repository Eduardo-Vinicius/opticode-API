import os

# Verifica se o código está rodando localmente (se o arquivo .env existe)
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()  # Carrega o arquivo .env se existir

# Obtém a chave da API do Google Maps da variável de ambiente
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')