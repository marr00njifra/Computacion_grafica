import random
import string

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

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32

def calificacion_a_letra(calificacion):
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80:
        return 'B'
    elif calificacion >= 70:
        return 'C'
    elif calificacion >= 60:
        return 'D'
    else:
        return 'F'

def contar_palabras(cadena):
    cadena = cadena.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def busqueda_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def validar_parentesis(secuencia):
    pila = []
    for caracter in secuencia:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

def ordenamiento_personalizado(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def gestion_agenda():
    agenda = {}
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado con éxito.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '4':
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu():
    while True:
        print("\n1. Operaciones Básicas (Calculadora)")
        print("2. Filtrado de Lista por Números Pares")
        print("3. Conversión de Temperaturas de Celsius a Fahrenheit")
        print("4. Sistema de Calificaciones a Letras")
        print("5. Conteo de Palabras en una Cadena")
        print("6. Búsqueda de Elemento en Lista")
        print("7. Validación de Secuencia de Paréntesis")
        print("8. Ordenamiento Personalizado de Lista de Tuplas")
        print("9. Generador de Contraseñas Aleatorias")
        print("10. Gestión de Agenda Telefónica")
        print("11. Salir del Programa")
        opcion = input("Seleccione una opción: ")

import random
import string

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

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32

def calificacion_a_letra(calificacion):
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80:
        return 'B'
    elif calificacion >= 70:
        return 'C'
    elif calificacion >= 60:
        return 'D'
    else:
        return 'F'

def contar_palabras(cadena):
    cadena = cadena.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def busqueda_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def validar_parentesis(secuencia):
    pila = []
    for caracter in secuencia:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

def ordenamiento_personalizado(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def gestion_agenda():
    agenda = {}
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado con éxito.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '4':
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu():
    while True:
        print("\n1. Operaciones Básicas (Calculadora)")
        print("2. Filtrado de Lista por Números Pares")
        print("3. Conversión de Temperaturas de Celsius a Fahrenheit")
        print("4. Sistema de Calificaciones a Letras")
        print("5. Conteo de Palabras en una Cadena")
        print("6. Búsqueda de Elemento en Lista")
        print("7. Validación de Secuencia de Paréntesis")
        print("8. Ordenamiento Personalizado de Lista de Tuplas")
        print("9. Generador de Contraseñas Aleatorias")
        print("10. Gestión de Agenda Telefónica")
        print("11. Salir del Programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación (suma/resta/multiplicacion/division): ")
            if operacion == 'suma':
                print(f"Resultado: {suma(a, b)}")
            elif operacion == 'resta':
                print(f"Resultado: {resta(a, b)}")
            elif operacion == 'multiplicacion':
                print(f"Resultado: {multiplicacion(a, b)}")
            elif operacion == 'division':
                print(f"Resultado: {division(a, b)}")
        elif opcion == '2':
            numeros = input("Ingrese una lista de números separados por comas: ")
            numeros = [int(num) for num in numeros.split(",")]
            print(f"Números pares: {filtrar_pares(numeros)}")
        elif opcion == '3':
            temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
            print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(temperatura)}")
        elif opcion == '4':
            calificaciones = input("Ingrese una lista de calificaciones numéricas separadas por comas: ")
            calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]
            print(f"Calificaciones en letras: {list(map(calificacion_a_letra, calificaciones))}")
        elif opcion == '5':
            texto = input("Ingrese una cadena de texto: ")
            resultado = contar_palabras(texto)
            print("Conteo de palabras:")
            for palabra, cantidad in resultado.items():
                print(f"{palabra}: {cantidad}")
        elif opcion == '6':
            lista = input("Ingrese una lista de elementos separados por comas: ").split(",")
            elemento = input("Ingrese el elemento a buscar: ")
            indice = busqueda_elemento(lista, elemento)
            if indice != -1:
                print(f"El elemento {elemento} se encuentra en el índice {indice}.")
            else:
                print(f"El elemento {elemento} no se encuentra en la lista.")
        elif opcion == '7':
            secuencia = input("Ingrese una secuencia de paréntesis: ")
            if validar_parentesis(secuencia):
                print("La secuencia de paréntesis es válida.")
            else:
                print("La secuencia de paréntesis no es válida.")
        elif opcion == '8':
            lista_tuplas = [("Juan", 25), ("María", 30), ("Carlos", 20), ("Ana", 25)]
            lista_ordenada = ordenamiento_personalizado(lista_tuplas)
            print("Lista ordenada:")
            for nombre, edad in lista_ordenada:
                print(f"{nombre}: {edad}")
        elif opcion == '9':
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            print(f"Contraseña generada: {generar_contraseña(longitud)}")
        elif opcion == '10':
            gestion_agenda()
        elif opcion == '11':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
