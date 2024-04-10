def filtrar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

def main():
    try:
        numeros = input("Ingrese una lista de números separados por comas: ")
        numeros = [int(num) for num in numeros.split(",")]
        print(f"Números pares: {filtrar_pares(numeros)}")
    except ValueError:
        print("Error: Ingrese números válidos separados por comas.")

main()
