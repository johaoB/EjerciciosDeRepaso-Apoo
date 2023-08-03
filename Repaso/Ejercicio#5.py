def main():
    grados = int(input("Ingrese la temperatura en fahrenheit: "))
    convercion(grados)

def convercion(grados):
    temperatura = (grados - 32) * 5/9 #Esta es la formula para convertir de fahrenheit a celcius
    print("La temperatura en celcius es:", round(temperatura, 1),"°")
    return

main()