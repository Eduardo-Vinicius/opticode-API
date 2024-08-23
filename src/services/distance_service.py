from src.utils.google_maps_client import get_distances

def calcular_distancias(origem, destino_fixo, destinos):
    """
    Calcula as distâncias entre uma origem fixa e vários destinos, terminando sempre em um destino fixo
    """
    # Adiciona a origem e o destino fixo à lista de locais
    locais = [origem] + destinos + [destino_fixo]
    
    # Obtém as distâncias entre todos os locais
    result = get_distances(locais, locais)
    print(result)
    distancias = {}

    # Índice da origem e do destino fixo na lista de locais
    origem_index = 0
    destino_fixo_index = len(locais) - 1

    for i, destino in enumerate(destinos):
        # Índice do destino na lista de locais
        destino_index = i + 1
        
        # Obtém a distância em km entre a origem e o destino
        distancia_km = result['rows'][origem_index]['elements'][destino_index]['distance']['value'] / 1000
        distancias[destino] = distancia_km

    # Calcula a distância entre o último destino e o destino fixo
    distancia_fim_fixo = result['rows'][destino_index]['elements'][destino_fixo_index]['distance']['value'] / 1000
    distancias[destino_fixo] = distancia_fim_fixo

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