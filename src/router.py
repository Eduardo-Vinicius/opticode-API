import json

from src.services.distance_service import calcular_distancias
from src.services.routing_service import calcular_melhor_rota
from src.services.fuel_service import calcular_custo_combustivel

def route_event(event):
    body = event.get('body', {})
    if event['path'] == '/calcular_distancias':
        if isinstance(body, str):
            body = json.loads(body)
        locais = body.get('locais', [])
        return calcular_distancias(locais)
    elif event['path'] == '/calcular_melhor_rota':
        if isinstance(body, str):
            body = json.loads(body)
        locais = body.get('locais', [])
        return calcular_melhor_rota(locais)
    elif event['path'] == '/calcular_custo_combustivel':
        if isinstance(body, str):
            body = json.loads(body)
        distancia_total_km = body.get('distancia_total_km', 0)
        consumo_medio_km_por_litro = body.get('consumo_medio_km_por_litro', 0)
        preco_combustivel_por_litro = body.get('preco_combustivel_por_litro', 0)
        return calcular_custo_combustivel(distancia_total_km, consumo_medio_km_por_litro, preco_combustivel_por_litro)
    else:
        raise ValueError("Rota não encontrada.")
