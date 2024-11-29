# charfun.py

"""
Programa que determina si una cadena proporcionada por el usuario es palíndroma. 
Para ello se preguntará por teclado al usuario tantas veces como quiera hasta que escriba la palabra salir.

Última Modificación: 21/11/2024
Autor: Gregorio Coronado Morón
Dependencias: Unicodedata, Re
"""

import unicodedata
import re

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es un palíndromo.
    Ignora espacios, mayúsculas, tildes y caracteres especiales.
    """
    if not isinstance(cadena, str):  # Validar que la entrada es una cadena
        raise TypeError("La entrada debe ser una cadena.")
    
    # Comprobar si la cadena está vacía o solo contiene espacios
    if not cadena.strip():
        return False

    # Normalizar Unicode para eliminar tildes y caracteres combinados
    cadena_normalizada = unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode('utf-8')

    # Eliminar caracteres no alfanuméricos (incluyendo puntuación y espacios), convertir a minúsculas
    cadena_limpia = ''.join(char.lower() for char in cadena_normalizada if char.isalnum())

    # Comparar los caracteres desde los extremos (para optimizar en cadenas largas)
    i, j = 0, len(cadena_limpia) - 1
    while i < j:
        if cadena_limpia[i] != cadena_limpia[j]:
            return False
        i += 1
        j -= 1

    return True

