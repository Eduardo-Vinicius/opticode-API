def calcular_custo_combustivel(distancia_total_km, consumo_medio_km_por_litro, preco_combustivel_por_litro):
    """Calcula o custo total de combustível para uma distância dada"""
    consumo_combustivel_litros = distancia_total_km / consumo_medio_km_por_litro
    custo_total = consumo_combustivel_litros * preco_combustivel_por_litro
    return {
        "distancia_total_km": distancia_total_km,
        "custo_total_combustivel": custo_total
    }
