def main():
    radio = int(input("Ingrese el radio del circulo: "))
    area = CalcularArea(radio)
    print("El area es de:", area)

def CalcularArea(R):
    Area = 3.14 * R**2
    return Area

main()