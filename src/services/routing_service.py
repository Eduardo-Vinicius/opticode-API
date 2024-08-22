from src.services.distance_service import calcular_distancias
import itertools

def calcular_melhor_rota(locais):
    """Calcula a melhor rota baseada nas distâncias entre os pontos"""
    distancias = calcular_distancias(locais)
    melhor_rota = optimize_route(locais, distancias)
    return melhor_rota

def optimize_route(locais, distancias):
    """Algoritmo para encontrar a rota mais curta (simplificado)"""
    rotas = itertools.permutations(locais)
    melhor_distancia = float('inf')
    melhor_rota = None

    for rota in rotas:
        distancia_total = 0
        for i in range(len(rota) - 1):
            origem = rota[i]
            destino = rota[i + 1]
            distancia_total += distancias[origem][destino]

        if distancia_total < melhor_distancia:
            melhor_distancia = distancia_total
            melhor_rota = rota

    return {
        "melhor_rota": melhor_rota,
        "distancia_total": melhor_distancia
    }
