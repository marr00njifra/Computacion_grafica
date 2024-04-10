def validar(sec):
    pila = []
    for caracter in sec:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

def main():
    sec = input("Ingrese una secuencia de paréntesis: ")
    if validar(sec):
        print("La secuencia de paréntesis es válida.")
    else:
        print("La secuencia de paréntesis no es válida.")

main()
