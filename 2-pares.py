def filtrar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

def main():
    try:
        x = input("Ingrese una lista de números separados por comas: ")
        x = [int(num) for num in x.split(",")]
        print(f"Números pares: {filtrar_pares(x)}")
    except ValueError:
        print("Error: Ingrese números válidos separados por comas.")

main()
