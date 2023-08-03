def main():
    numero = int(input("Ingrese el numero: "))
    Averiguar(numero)

def Averiguar(num):
    if num %2 == 0:
        print("El numero", num, "es par")
    else:
        print("El numero", num, "es impar")
    
    return

main()