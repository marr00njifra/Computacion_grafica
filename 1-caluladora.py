def sum(a, b):
    return a+b

def res(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b!=0:
        return a/b
    else:
        return "Error."

def calculator():
    while True:
        try:
            opcion = input("¿Qué operación desea realizar? (suma/resta/multiplicacion/division): ")
            if opcion.lower() in ['suma', 'resta', 'multiplicacion', 'division']:
                a = float(input("Ingrese un primer número: "))
                b = float(input("Ingrese un segundo número: "))
                if opcion.lower() == 'suma':
                    print(f"Resultado: {sum(a, b)}")
                elif opcion.lower() == 'resta':
                    print(f"Resultado: {res(a, b)}")
                elif opcion.lower() == 'multiplicacion':
                    print(f"Resultado: {mul(a, b)}")
                elif opcion.lower() == 'division':
                    print(f"Resultado: {div(a, b)}")
            else:
                print("Operación inválida.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except Exception as e:
            print(f"Error: {e}")

        continuar = input("¿Desea realizar otra operación? (si/no): ")
        if continuar.lower() != 'si':
            break

calculator()
