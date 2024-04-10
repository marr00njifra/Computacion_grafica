import string

def contar(cadena):

    cadena = cadena.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def main():
    texto = input("Ingrese una cadena de texto: ")
    resultado = contar(texto)
    print("Conteo de palabras:")
    for palabra, cantidad in resultado.items():
        print(f"{palabra}: {cantidad}")

main()
