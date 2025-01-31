import json
from app.services.distance_service import calculate_distances
from app.services.fuel_service import calcular_custo_combustivel
from app.services.update_routes import update_route_status

def route_event(event):
    path = event.get("path", "")
    body = event.get("body", "{}")

    print(event)
    print(path)

    # Garante que 'body' seja um dicionário válido
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return {"error": "Formato de JSON inválido"}

    # Roteamento das requisições
    if path == "/route/calculate-distance":
        return calculate_distances(
            origin=body.get("origin"),
            fixed_destination=body.get("destination"),
            destinations=body.get("destinations", [])
        )
    if path == "/route/update-stop":
        return update_route_status(
            route_data=body.get("routes"),
            completed_stop_id=body.get("id")
        )
        
    elif path == "/calcular_custo_combustivel":
        return calcular_custo_combustivel(
            distancia_total_km=body.get("distancia_total_km", 0),
            consumo_medio_km_por_litro=body.get("consumo_medio_km_por_litro", 0),
            preco_combustivel_por_litro=body.get("preco_combustivel_por_litro", 0)
        )

    return {"error": "Rota não encontrada"}
