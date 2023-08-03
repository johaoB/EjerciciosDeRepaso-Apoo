def palindromo(cadena):
    frase = input("Ingrese la frase o texto: ")
    inicio = 0
    fin = len(frase) - 1

    while frase[inicio] == frase[fin]:
        if inicio >= fin:
            print("La frase es un palindromo")
        inicio += 1
        fin -= 1
    print("La frase no es un palindromo")