import unittest
from app.scripts.charfun import esPalindromo


class TestEsPalindromo(unittest.TestCase):
    """Clase para probar la función esPalindromo."""

    def test_palindromos_simples(self):
        self.assertTrue(esPalindromo("ana"))  # Palíndromo simple
        self.assertTrue(esPalindromo("oso"))  # Otro palíndromo simple
        self.assertFalse(esPalindromo("hola"))  # No es palíndromo

    def test_ignorar_espacios_y_mayusculas(self):
        self.assertTrue(esPalindromo("A Santa at NASA"))  # Palíndromo con espacios y mayúsculas
        self.assertTrue(esPalindromo("Luz Azul"))  # Palíndromo con mayúsculas
        self.assertFalse(esPalindromo("Esto no es"))  # No es palíndromo

    def test_caracteres_especiales(self):
        self.assertTrue(esPalindromo("Anita, lava la tina"))  # Palíndromo con puntuación
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))  # Palíndromo con tildes y símbolos
        self.assertFalse(esPalindromo("¿Esto no?"))  # No es palíndromo

    def test_entrada_vacia(self):
        self.assertFalse(esPalindromo(""))  # Cadena vacía
        self.assertFalse(esPalindromo(" "))  # Espacio vacío

    def test_entrada_invalida(self):
        with self.assertRaises(TypeError):  # Se espera que lance un error
            esPalindromo(None)  # Entrada nula
        with self.assertRaises(TypeError):
            esPalindromo(12321)  # Número en lugar de cadena

    def test_palindromo_con_tildes(self):
        """
        Prueba que palabras con tildes sean correctamente reconocidas como palíndromos.
        """
        self.assertTrue(esPalindromo("joój"))  # Palíndromo con tilde
        self.assertTrue(esPalindromo("rótor"))  # Otro palíndromo con tilde
        self.assertFalse(esPalindromo("hola"))  # No es palíndromo

    def test_comparacion_palindromo(self):
        """Test con assertEqual para comparar la cadena limpia y su reverso"""
        # Test con un ejemplo simple
        resultado = esPalindromo("anita lava la tina")
        self.assertEqual(resultado, True)  # Debería ser True, ya que es un palíndromo

        # Test con un caso que no es palíndromo
        resultado = esPalindromo("esto no es")
        self.assertEqual(resultado, False)  # Debería ser False, ya que no es un palíndromo


# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
