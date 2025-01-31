import sys
import itertools
import json
sys.path.append('C:/Users/Eduardo Vinicius/Documents/Repositories/opticode-API')

from app.utils.google_maps_client import get_distances

def calculate_distances(origin, fixed_destination, destinations):
    locations = [origin] + destinations + [fixed_destination]
    result = get_distances(locations, locations)
    print(result)

    distances = {loc: {} for loc in locations}
    for i, origin in enumerate(locations):
        for j, destination in enumerate(locations):
            if i != j:
                distance_km = result['rows'][i]['elements'][j]['distance']['value'] / 1000
                distances[origin][destination] = distance_km

    result = find_best_route(distances)
    
    return result

def calculate_estimated_time(distance_km):
    average_speed_kmh = 50
    time_hours = distance_km / average_speed_kmh
    minutes = time_hours * 60
    return f"{int(minutes)} mins"

def generate_status(index, total_locations):
    if index == 0:
        return "starting"
    elif index == total_locations - 1:
        return "done"
    else:
        return "waiting"

def find_best_route(distances):
    locations = list(distances.keys())
    stops = locations[1:-1]
    
    best_distance = float('inf')
    best_route = None
    for permutation in itertools.permutations(stops):
        route = [locations[0]] + list(permutation) + [locations[-1]]
        
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += distances[route[i]][route[i + 1]]
        
        if total_distance < best_distance:
            best_distance = total_distance
            best_route = route
    
    result_json = {"best_route": [], "total_distance_km": round(best_distance, 2)}
    total_estimated_time = 0
    
    for index, location in enumerate(best_route):
        distance_to_next = 0 if index == len(best_route) - 1 else distances[location][best_route[index + 1]]
        estimated_time = calculate_estimated_time(distance_to_next)
        status = generate_status(index, len(best_route))
        
        total_estimated_time += distance_to_next / 50 * 60
        
        result_json["best_route"].append({
            "address": location,
            "distance_to_next_km": round(distance_to_next, 2),
            "estimated_time": estimated_time,
            "status": status
        })
    
    result_json["total_estimated_time"] = f"{int(total_estimated_time // 60)} hours {int(total_estimated_time % 60)} mins"

    return result_json

if __name__ == '__main__':


    # Exemplo de Teste 1

    origin = 'Rua Onze, 30 - Jardim Monte verde - Sao Paulo - SP'
    fixed_destination = 'Aeroporto de Congonhas'
    destinations = [
        "Estacao Vila Prudente - São Paulo, SP",
        "Estacao Vila Madalena - São Paulo, SP",
        "Estacao Sao Paulo Morumbi - São Paulo, SP",
        "Rua Um, 10 Jardim Tres Coracoes - São Paulo, SP",
        "Estacao Giovanni Gronchi - São Paulo, SP"
    ]

    distances = calculate_distances(origin, fixed_destination, destinations)
    # best_route_json = find_best_route(distances)

    # Exemplo de Teste 2

    # origin = 'Rua da Consolação, 1234 - Consolação - São Paulo - SP'
    # fixed_destination = 'Aeroporto Internacional de São Paulo - Guarulhos'
    # destinations = [
    #     "Estação República - São Paulo, SP",
    #     "Estação Sé - São Paulo, SP",
    #     "Estação Paulista - São Paulo, SP",
    #     "Rua Augusta, 1000 - São Paulo, SP",
    #     "Estação Brás - São Paulo, SP"
    # ]

    # distances = calculate_distances(origin, fixed_destination, destinations)
    # best_route_json = find_best_route(distances)

    # Exemplo de Teste 3

    # origin = 'Avenida Paulista, 1500 - Bela Vista - São Paulo - SP'
    # fixed_destination = 'Estádio do Morumbi - São Paulo - SP'
    # destinations = [
    #     "Estação Faria Lima - São Paulo, SP",
    #     "Estação Vila Madalena - São Paulo, SP",
    #     "Rua dos Três Irmãos, 200 - São Paulo, SP",
    #     "Avenida Rebouças, 2345 - São Paulo, SP",
    #     "Estação Tatuapé - São Paulo, SP"
    # ]

    # distances = calculate_distances(origin, fixed_destination, destinations)
    # best_route_json = find_best_route(distances)
    
    # Display the result in JSON format
    print(json.dumps(distances, indent=4))
