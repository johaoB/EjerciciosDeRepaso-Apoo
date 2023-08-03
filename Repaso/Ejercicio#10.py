def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= 1
    return resultado

def main():
    numero = int(input("Ingrese el numero: "))
    resultado_factorial = factorial(numero)
    print("El factorial de", numero, "es:", resultado_factorial)

main()