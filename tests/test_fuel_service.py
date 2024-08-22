import pytest
from src.services.fuel_service import calcular_custo_combustivel


def test_calcular_custo_combustivel():
    # Dados de teste
    distancia_total_km = 100  # 100 km
    consumo_medio_km_por_litro = 10  # 10 km por litro
    preco_combustivel_por_litro = 5.0  # R$ 5.00 por litro

    # Esperado: Custo total = (100 km / 10 km/litro) * R$ 5.00 = R$ 50.00
    resultado_esperado = {
        "distancia_total_km": 100,
        "custo_total_combustivel": 50.0
    }

    # Calcula o custo
    resultado = calcular_custo_combustivel(distancia_total_km, consumo_medio_km_por_litro,
                                           preco_combustivel_por_litro)

    # Verifica se o resultado está correto
    assert resultado == resultado_esperado
