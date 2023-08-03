def main():
    list = [8, 6, 12, 54, 31, 47]
    mayor = num_mayor(list)
    menor = num_menor(list)
    print("El numero mayor en la lista es:", mayor, ", Y el menor es:", menor)


def num_mayor(list):
    mayor = list[0]
    for i in range(len(list)):
        if list[i] > mayor:
            mayor = list[i]
    return mayor

def num_menor(list):
    menor = list[0]
    for i in range(len(list)):
        if list[i] < menor:
            menor = list[i]
    return menor

main()