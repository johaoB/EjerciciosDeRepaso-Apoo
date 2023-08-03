def main():
    list = [4, 18, 6, 7, 9, 24]
    Acumulado = sum_list(list)
    print("El acumulado de la lista es de:", Acumulado)

def sum_list(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

main()