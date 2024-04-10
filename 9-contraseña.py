import random
import string

def generar_contraseña(long):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(long))
    return contraseña

def main():
    long = int(input("Ingrese la longitud de la contraseña: "))
    contraseña = generar_contraseña(long)
    print(f"Contraseña generada: {contraseña}")

main()
