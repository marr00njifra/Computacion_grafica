import numpy as np

def crear_array_unidimensional():
    array = np.arange(1, 11)
    print("Array unidimensional:")
    print(array)

def crear_array_multidimensional():
    matriz = np.arange(1, 10).reshape(3, 3)
    print("Array multidimensional:")
    print(matriz)

def operaciones_basicas_con_arrays():
    array1 = np.arange(1, 6)
    array2 = np.arange(1, 6)
    suma = array1 + array2
    print("Resultado de la suma de arrays:")
    print(suma)

def funciones_matematicas():
    array = np.arange(1, 6)
    exponential = np.exp(array)
    print("Exponencial de cada elemento del array:")
    print(exponential)

def indexacion_y_segmentacion():
    array = np.arange(1, 11)
    pares = array[array % 2 == 0]
    print("Elementos pares del array:")
    print(pares)

def generacion_de_datos_aleatorios():
    array_aleatorio = np.random.rand(10)
    print("Array de números aleatorios:")
    print(array_aleatorio)

def funciones_de_agregacion():
    array = np.arange(1, 6)
    media = np.mean(array)
    print("Media de los elementos del array:")
    print(media)

def creacion_de_arrays_con_funciones_de_fabrica():
    array = np.full(5, 7)
    print("Array con elementos inicializados en 7:")
    print(array)

def operaciones_de_alineacion_y_broadcasting():
    array1 = np.arange(1, 4)
    array2 = np.arange(4, 7)
    suma = array1 + array2
    print("Resultado de la suma con broadcasting:")
    print(suma)

def funciones_de_transformacion_y_redimensionamiento():
    array = np.arange(1, 7)
    matriz = array.reshape(2, 3)
    print("Matriz 2x3:")
    print(matriz)

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Crear Array Unidimensional")
    print("2. Crear Array Multidimensional")
    print("3. Operaciones Básicas con Arrays")
    print("4. Funciones Matemáticas")
    print("5. Indexación y Segmentación")
    print("6. Generación de Datos Aleatorios")
    print("7. Funciones de Agregación")
    print("8. Creación de Arrays con Funciones de Fábrica")
    print("9. Operaciones de Alineación y Broadcasting")
    print("10. Funciones de Transformación y Redimensionamiento")
    print("11. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        crear_array_unidimensional()
    elif opcion == 2:
        crear_array_multidimensional()
    elif opcion == 3:
        operaciones_basicas_con_arrays()
    elif opcion == 4:
        funciones_matematicas()
    elif opcion == 5:
        indexacion_y_segmentacion()
    elif opcion == 6:
        generacion_de_datos_aleatorios()
    elif opcion == 7:
        funciones_de_agregacion()
    elif opcion == 8:
        creacion_de_arrays_con_funciones_de_fabrica()
    elif opcion == 9:
        operaciones_de_alineacion_y_broadcasting()
    elif opcion == 10:
        funciones_de_transformacion_y_redimensionamiento()
    elif opcion == 11:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
