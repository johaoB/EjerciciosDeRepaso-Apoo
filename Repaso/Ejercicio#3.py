import random

def main():
    list = []
    Cantidad = int(input("ingrese la cantidad de numeros que necesita: "))
    for i in range(Cantidad):
        Numero = random.randint(1,200)
        list.append(Numero)
    
    print(list)

main()