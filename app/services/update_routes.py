from datetime import datetime

def update_route_status(route_data, completed_stop_id):
    """
    Atualiza o status da rota, movendo as paradas concluídas para o final, 
    adicionando um timestamp no momento da finalização.

    :param route_data: Dicionário contendo a rota completa.
    :param completed_stop_id: ID da parada que foi concluída.
    :return: Rota atualizada com as paradas "done" no final, ordenadas por tempo de finalização.
    """
    best_route = route_data["best_route"]
    now = datetime.utcnow().isoformat()  # Formato ISO 8601 (ex: "2025-01-31T12:34:56.789Z")

    # Marcar a parada como "done" e adicionar o timestamp
    for stop in best_route:
        if stop["id"] == completed_stop_id:
            stop["status"] = "done"
            stop["finishedAt"] = now  # Adiciona o timestamp
            break

    # Reorganizar a lista:
    # - "starting" e "waiting" primeiro,
    # - "done" no final, ordenado pelo "finishedAt"
    sorted_route = sorted(
        best_route, 
        key=lambda x: (x["status"] == "done", x.get("finishedAt", ""))
    )

    # Garantir que a primeira parada ativa seja "starting"
    for stop in sorted_route:
        if stop["status"] == "waiting":
            stop["status"] = "starting"
            break

    route_data["best_route"] = sorted_route
    route_data["updatedAt"] = now  # Atualiza o timestamp da rota

    return route_data