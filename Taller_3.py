import numpy as np

def ejercicio_1():
    arr = np.array(range(1, 11))
    reshaped_arr = arr.reshape(2, 5)
    print("Array original:")
    print(arr)
    print("\nArray con forma modificada:")
    print(reshaped_arr)
    print("\nPropiedades:")
    print("Dimensiones:", reshaped_arr.ndim)
    print("Forma:", reshaped_arr.shape)
    print("Tamaño:", reshaped_arr.size)

def ejercicio_2():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Producto elemento a elemento:", a * b)
    print("Suma de todos los elementos en a:", np.sum(a))

def ejercicio_3():
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("Quinto elemento:", data[4])
    print("Subsección:", data[2:7])

def ejercicio_4():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("A + 10:")
    print(A + 10)
    print("Raíz cuadrada de A:")
    print(np.sqrt(A))

def ejercicio_5():
    M = np.array([[1, 2], [3, 4], [5, 6]])
    print("Forma original de M:")
    print(M)
    print("Forma modificada de M:")
    print(M.reshape(3, 2))
    print("Producto punto de M y su transpuesta:")
    print(np.dot(M, M.T))

def ejercicio_6():
    data = np.array([1, 2, np.nan, 4, 5])
    print("Array original con valores faltantes:")
    print(data)
    data_filled = np.nan_to_num(data, nan=0)
    print("Array con valores faltantes reemplazados por 0:")
    print(data_filled)
    print("Media del array resultante:")
    print(np.mean(data_filled))

def ejercicio_7():
    data = np.array([1, 2, 3, 4, 5])
    np.save('mi_array.npy', data)
    loaded_data = np.load('mi_array.npy')
    print("Array cargado desde el archivo:")
    print(loaded_data)

def main():
    while True:
        print("\nMenu:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Salir")
        choice = input("\nSeleccione un ejercicio (1-8): ")

        if choice == '1':
            ejercicio_1()
        elif choice == '2':
            ejercicio_2()
        elif choice == '3':
            ejercicio_3()
        elif choice == '4':
            ejercicio_4()
        elif choice == '5':
            ejercicio_5()
        elif choice == '6':
            ejercicio_6()
        elif choice == '7':
            ejercicio_7()
        elif choice == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
