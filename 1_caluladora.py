def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def calculadora():
    while True:
        try:
            opcion = input("¿Qué operación desea realizar? (suma/resta/multiplicacion/division): ")
            if opcion.lower() in ['suma', 'resta', 'multiplicacion', 'division']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                if opcion.lower() == 'suma':
                    print(f"Resultado: {suma(num1, num2)}")
                elif opcion.lower() == 'resta':
                    print(f"Resultado: {resta(num1, num2)}")
                elif opcion.lower() == 'multiplicacion':
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                elif opcion.lower() == 'division':
                    print(f"Resultado: {division(num1, num2)}")
            else:
                print("Operación inválida. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except Exception as e:
            print(f"Error: {e}")

        continuar = input("¿Desea realizar otra operación? (si/no): ")
        if continuar.lower() != 'si':
            break

calculadora()
