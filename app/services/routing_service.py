from app.services.distance_service import calcular_distancias
import itertools


def calcular_melhor_rota(origem, destino_fixo, locais):
    """Calcula a melhor rota baseada nas distâncias entre os pontos"""
    distancias = calcular_distancias(origem, destino_fixo, locais)
    print(distancias)
    melhor_rota = optimize_route(locais, distancias)
    melhor_rota['ways'].append(destino_fixo)
    return melhor_rota


def optimize_route(locais, distancias):
    """Algorithm to find the shortest route starting from the first location and ending at the last location"""
    
    # Extract fixed origin and destination from locais
    origem = locais[0]
    destino_fixo = locais[-1]
    
    # Extract delivery addresses (intermediate points)
    destinos = locais[1:-1]
    
    melhor_distancia = float('inf')
    melhor_rota = None

    # Generate all permutations of delivery addresses
    for rota in itertools.permutations(destinos):
        rota_completa = [origem] + list(rota) + [destino_fixo]
        print(rota_completa)
        print(locais)
        
        distancia_total = 0
        # Calculate the total distance of the current route
        for i in range(len(rota_completa) - 1):
            origem = rota_completa[i]
            destino = rota_completa[i + 1]
            distancia_total += distancias[origem][destino]
        
        if distancia_total < melhor_distancia:
            melhor_distancia = distancia_total
            melhor_rota = rota_completa

    return {
        "ways": melhor_rota,
        "totalDistance": melhor_distancia
    }
