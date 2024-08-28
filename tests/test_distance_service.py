import pytest
from app.services.distance_service import calcular_distancias

def mock_get_distances(locais, destinos):
    """ Função mock para simular o comportamento de get_distances """
    return {
        'rows': [
            {'elements': [{'distance': {'value': 1000}}, {'distance': {'value': 2000}}, {'distance': {'value': 3000}}, {'distance': {'value': 4000}}]},
            {'elements': [{'distance': {'value': 1500}}, {'distance': {'value': 2500}}, {'distance': {'value': 3500}}, {'distance': {'value': 4500}}]},
            {'elements': [{'distance': {'value': 2000}}, {'distance': {'value': 3000}}, {'distance': {'value': 4000}}, {'distance': {'value': 5000}}]},
            {'elements': [{'distance': {'value': 2500}}, {'distance': {'value': 3500}}, {'distance': {'value': 4500}}, {'distance': {'value': 5500}}]},
        ]
    }

def test_calcular_distancias():
    origem = "Av. Paulista, 1578 - São Paulo, SP"
    destino_fixo = "Praça da Sé - São Paulo, SP"
    destinos = [
        "Rua Augusta, 2000 - São Paulo, SP",
        "Avenida 23 de Maio, 1000 - São Paulo, SP",
        "Rua da Consolação, 1234 - São Paulo, SP"
    ]

    # Substitua a função real por uma mockada para o teste
    global get_distances
    get_distances = mock_get_distances

    distancias = calcular_distancias(origem, destino_fixo, destinos)

    assert len(distancias) == len(destinos) + 1  # Inclui o destino fixo
    assert distancias["Rua Augusta, 2000 - São Paulo, SP"] > 0
    assert distancias["Avenida 23 de Maio, 1000 - São Paulo, SP"] > 0
    assert distancias["Rua da Consolação, 1234 - São Paulo, SP"] > 0
    assert distancias[destino_fixo] > 0

if __name__ == "__main__":
    test_calcular_distancias()
