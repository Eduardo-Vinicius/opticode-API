import json
from app.services.distance_service import calculate_distances
from app.services.fuel_service import calcular_custo_combustivel
from app.services.update_routes import update_route_status
from app.services.vehicle_service import atualizar_veiculo, buscar_veiculo, criar_veiculo, deletar_veiculo, listar_veiculos

def route_event(event):
    path = event.get("path", "")
    body = event.get("body", "{}")
    method = event.get("method", "{}")
    queryParams = "" # Pegar um exemplo de onde vem a query Params

    print(event)
    print(path)
    print(method)

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
    
    elif path == "/veiculos":
        if method == "POST":
            return criar_veiculo(
                placa=body.get("placa"), 
                modelo=body.get("modelo"), 
                capacidade=body.get("capacidade", 0), 
                status=body.get("status", "INATIVO"), # ATIVO/INATIVO
                total_km=body.get("total_km", 0), 
                km_litro=body.get("km_litro", 0)
            )
        elif method == "GET":
            return listar_veiculos()
        elif method == "PUT":
            return atualizar_veiculo(
                id=body.get("id"), 
                placa=body.get("placa"), 
                modelo=body.get("modelo"), 
                capacidade=body.get("capacidade", 0), 
                status=body.get("status", "INATIVO"), # ATIVO/INATIVO
                total_km=body.get("total_km", 0), 
                km_litro=body.get("km_litro", 0)
            )
    elif queryParams != None and path == "/veiculos/{id}": #TODO(): Validar no event como vem o queryParams
        if method == "GET":
            return buscar_veiculo(id)
        elif method == "DELETE":
            return deletar_veiculo(id)

    return {"error": "Rota não encontrada"}
