from app.scripts.charfun import esPalindromo

def main():
    """Función principal del programa."""
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es un palíndromo.")
            else:
                print("La frase no es un palíndromo.")

if __name__ == "__main__":
    main()
