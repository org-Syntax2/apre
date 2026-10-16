from django.test import TestCase, Client
import os

class CalculadoraWebTest(TestCase):
    def test_suma_dinamica(self):
        client = Client()
        # Probamos con otros números (ej: 40 y 50 -> la suma debe ser 90)
        response = client.post('/', {'num1': '40', 'num2': '50'})
        
        self.assertEqual(response.status_code, 302)
        
        ruta_txt = 'resultado.txt'
        self.assertTrue(os.path.exists(ruta_txt))
        with open(ruta_txt, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
        
        self.assertEqual(contenido, '90')