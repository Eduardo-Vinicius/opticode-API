from app.utils.google_maps_client import get_distances

def calcular_distancias(origem, destino_fixo, destinos):
    """
    Calculates distances between all pairs of locations including a fixed origin and a fixed destination.
    """
    # Add the fixed origin and destination to the list of locations
    locais = [origem] + destinos + [destino_fixo]
    print(locais)
    
    # Get distances between all locations
    result = get_distances(locais, locais)  # Assuming get_distances returns a full matrix of distances
    
    # Initialize the distance matrix
    distancias = {loc: {} for loc in locais}

    # Fill the distance matrix
    for i, origem in enumerate(locais):
        for j, destino in enumerate(locais):
            if i != j:
                distancia_km = result['rows'][i]['elements'][j]['distance']['value'] / 1000
                distancias[origem][destino] = distancia_km
    
    return distancias


if __name__ == '__main__':
    origem = 'Rua Um, 10 - Jardim Tres coracoes, Sao Paulo - SP'
    destino_fixo = 'R. Roger Bacon, 87 - Jardim Morais Prado, São Paulo - SP'
    destinos = [
        "Rua Augusta, 2000 - São Paulo, SP",
        "Avenida 23 de Maio, 1000 - São Paulo, SP",
        "Rua da Consolação, 1234 - São Paulo, SP"
    ]

    print(calcular_distancias(origem, destino_fixo, destinos))