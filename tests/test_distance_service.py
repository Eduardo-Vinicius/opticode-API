import pytest
from src.services.distance_service import calcular_distancias

def test_calcular_distancias():
    locais = [
        "Av. Paulista, 1578 - São Paulo, SP",
        "Rua Augusta, 2000 - São Paulo, SP",
        "Praça da Sé - São Paulo, SP"
    ]
    distancias = calcular_distancias(locais)
    
    assert 'Av. Paulista, 1578 - São Paulo, SP' in distancias
    assert 'Rua Augusta, 2000 - São Paulo, SP' in distancias['Av. Paulista, 1578 - São Paulo, SP']
    assert len(distancias['Av. Paulista, 1578 - São Paulo, SP']) > 0  # Assegura que há alguma distância calculada
