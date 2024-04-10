def calificacion_letra(calificacion):
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

def convertir_calificaciones(calificaciones):
    return [calificacion_letra(calificacion) for calificacion in calificaciones]

def main():
    try:
        calificaciones = input("Ingrese una lista de calificaciones numéricas separadas por comas: ")
        calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]
        calificaciones_letras = convertir_calificaciones(calificaciones)
        print(f"Calificaciones en letras: {calificaciones_letras}")
    except ValueError:
        print("Error: Ingrese calificaciones válidas separadas por comas.")

main()
