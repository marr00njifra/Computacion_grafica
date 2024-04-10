def metodo_ordenamiento(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))

def main():
    lista = [("Juan", 25), ("María", 30), ("Santiago", 20), ("Ana", 25)]
    lista_ordenada = metodo_ordenamiento(lista)
    print("Lista ordenada:")
    for name, age in lista_ordenada:
        print(f"{name}: {age}")

main()
