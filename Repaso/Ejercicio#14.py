def main():
    lista = [14, 25, 7, 31, 28]
    acumulado = MediaArimetrica(lista)
    print(f"la media arimetrica de la lista: {round(acumulado, 1)}")

def MediaArimetrica(list):
    suma = 0
    contador = 0
    for i in range(len(list)):
        suma += list[i]
        contador += 1
    total = suma / contador
    return total

main()