import unittest
from src.services.distance_service import calcular_distancias

class TestDistanceService(unittest.TestCase):
    def test_calcular_distancias(self):
        locais = [
            "Av. Paulista, 1578 - São Paulo, SP",
            "Rua Augusta, 2000 - São Paulo, SP",
            "Praça da Sé - São Paulo, SP"
        ]
        distancias = calcular_distancias(locais)
        self.assertIn('Av. Paulista, 1578 - São Paulo, SP', distancias)
        self.assertIn('Rua Augusta, 2000 - São Paulo, SP', distancias['Av. Paulista, 1578 - São Paulo, SP'])
        self.assertGreater(len(distancias['Av. Paulista, 1578 - São Paulo, SP']), 0)  # Assegura que há alguma distância calculada

if __name__ == '__main__':
    unittest.main()
