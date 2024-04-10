def buscar(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def main():
    lista = input("Ingrese una lista de elementos separados por comas: ").split(",")
    elemento = input("Ingrese el elemento a buscar: ")
    indice = buscar(lista, elemento)
    if indice != -1:
        print(f"El elemento {elemento} se encuentra en el índice {indice}.")
    else:
        print(f"El elemento {elemento} no se encuentra en la lista.")

main()
