from src.utils.google_maps_client import get_distances

def calcular_distancias(locais):
    """Calcula as distâncias entre todos os locais"""
    result = get_distances(locais, locais)
    distancias = {}

    for i, origem in enumerate(locais):
        distancias[origem] = {}
        for j, destino in enumerate(locais):
            if i != j:
                distancia_km = result['rows'][i]['elements'][j]['distance']['value'] / 1000
                distancias[origem][destino] = distancia_km

    return distancias
