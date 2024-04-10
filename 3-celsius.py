def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        t_celsius = input("Ingrese una lista de temperaturas en grados Celsius separadas por comas: ")
        t_celsius = [float(temp) for temp in t_celsius.split(",")]
        t_fahrenheit = list(map(lambda x: celsius_to_fahrenheit(x), t_celsius))
        print(f"Temperaturas en Fahrenheit: {t_fahrenheit}")
    except ValueError:
        print("Error: Ingrese temperaturas válidas separadas por comas.")

main()
