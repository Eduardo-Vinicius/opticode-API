import os

from app.clients.dynamodb_client import DynamoDBClient

client = DynamoDBClient()
TABLE_NAME = os.getenv("DYNAMODB_VEICULOS_TABLE", "veiculos_table")

def criar_veiculo(placa, modelo, capacidade, status, total_km, km_litro):
    return client.create_item(TABLE_NAME, {
        "placa": placa,
        "modelo": modelo,
        "capacidade": capacidade,
        "status": status,
        "total_km": total_km,
        "km_litro": km_litro
    })

def listar_veiculos():
    return client.get_all_items(TABLE_NAME)

def buscar_veiculo(id):
    veiculo = client.get_item(TABLE_NAME, id)
    if not veiculo:
        return {"message": "Veículo não encontrado"}, 404
    return veiculo

def atualizar_veiculo(id, placa, modelo, capacidade, status, total_km, km_litro):
    return client.update_item(TABLE_NAME, id, {
        "placa": placa,
        "modelo": modelo,
        "capacidade": capacidade,
        "status": status,
        "total_km": total_km,
        "km_litro": km_litro
    })

def deletar_veiculo(id):
    return client.delete_item(TABLE_NAME, id)
