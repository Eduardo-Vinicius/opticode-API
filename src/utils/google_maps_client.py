import googlemaps
from src.config import GOOGLE_MAPS_API_KEY

# Inicializa o cliente do Google Maps
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_distances(origins, destinations):
    """Obtém a matriz de distâncias entre origens e destinos"""
    result = gmaps.distance_matrix(origins=origins, destinations=destinations, mode="driving")
    return result
