import numpy as np
import matplotlib.pyplot as plt
from FuncionesA import * 


#solucion Taller 4-5
#imagenes usadas
IMG1 = plt.imread('Dog1.jpg')
IMG1 = np.array(IMG1)

IMG2 = plt.imread('Cat1.jpg')
IMG2 = np.array(IMG2)

IMG3 = plt.imread('Bike1.jpg')
IMG3 = np.array(IMG3)


#1
def punto1():
    M = np.zeros((3,3,3), dtype=int)
    print(M)
    # fila , columna, capa
    M[0,2,0]=255 #R
    M[1,2,1]=255 #G
    M[2,2,2]=255 #B

    #blanco
    M[0,1,0]=255 
    M[0,1,1]=255
    M[0,1,2]=255

    #gris
    M[1,1,0]=127
    M[1,1,1]=127
    M[1,1,2]=127

    #negro
    M[2,1,0]=0
    M[2,1,1]=0
    M[2,1,2]=0

    #cyan
    M[0,0,1]=255 #G
    M[0,0,2]=255 #B

    #magenta
    M[1,0,0]=255 #R
    M[1,0,2]=255 #B

    #amarillo
    M[2,0,0]=255 #R
    M[2,0,1]=255 #G

    plt.imshow(M)
    plt.show()
#2
def punto2():
    M = np.zeros((5,11,3), dtype=int)
    #estrutura de la matriz = fila , columna, capa 

    # Amarillo 
    M[0:4, 0, 0] = 255
    M[0:4, 0, 1] = 255

    # Cyan 
    M[0:4, 1:3, 1] = 255
    M[0:4, 1:3, 2] = 255

    # Verde 
    M[0:4, 3:5, 1] = 255

    # Magenta 
    M[0:4, 5:7, 0] = 255
    M[0:4, 5:7, 2] = 255

    # Rojo 
    M[0:4, 7:9, 0] = 255

    # Azul 
    M[0:4, 9:11, 2] = 255

    #escala de blanco a negro
    M[4,0,0] = 255
    M[4,0,1] = 255
    M[4,0,2] = 255

    M[4,1,0] = 232
    M[4,1,1] = 232
    M[4,1,2] = 232

    M[4,2,0] = 209
    M[4,2,1] = 209
    M[4,2,2] = 209

    M[4,3,0] = 186
    M[4,3,1] = 186
    M[4,3,2] = 186

    M[4, 4, 0] = 163
    M[4, 4, 1] = 163
    M[4, 4, 2] = 163

    M[4, 5, 0] = 140
    M[4, 5, 1] = 140
    M[4, 5, 2] = 140

    M[4, 6, 0] = 116
    M[4, 6, 1] = 116
    M[4, 6, 2] = 116

    M[4, 7, 0] = 93
    M[4, 7, 1] = 93
    M[4, 7, 2] = 93

    M[4, 8, 0] = 70
    M[4, 8, 1] = 70
    M[4, 8, 2] = 70

    M[4, 9, 0] = 23
    M[4, 9, 1] = 23
    M[4, 9, 2] = 23

    M[4, 10, 0] = 0
    M[4, 10, 1] = 0
    M[4, 10, 2] = 0

    plt.imshow(M)
    plt.show()     
#3 invertir color
def punto3(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = invertir(IMG)
    plt.imshow(img)
    plt.show()
#4 retorna capa Roja
def punto4(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnR(IMG)
    plt.imshow(img)
    plt.show()
#5 retorna capa Verde
def punto5(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnG(IMG)
    plt.imshow(img)
    plt.show()
#6 retorna capa Azul
def punto6(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnB(IMG)
    plt.imshow(img)
    plt.show()
#7 retorna imagen magenta
def punto7(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnM(IMG)
    plt.imshow(img)
    plt.show()
#8 retorna imagen cyan
def punto8(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnC(IMG)
    plt.imshow(img)
    plt.show()
#9 retorna imagen amarilla
def punto9(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ReturnY(IMG)
    plt.imshow(img)
    plt.show()
#10 recibe la division de una imagen en R,G,B y la fusiona
def punto10(IMGR,IMGG,IMGB):
    plt.subplot(2,2,1)
    plt.imshow(IMGR)
    plt.subplot(2,2,2)
    plt.imshow(IMGG)
    plt.subplot(2,2,3)
    plt.imshow(IMGB)
    plt.subplot(2,2,4)
    plt.title("imagen fusionada")
    img = fusionRGB(IMGR,IMGG,IMGB)
    plt.imshow(img)
    plt.show()

""" imgR = ReturnR(IMG1)
imgG = ReturnG(IMG1)
imgB = ReturnB(IMG1)
punto10(imgR,imgG,imgB)"""

#11 funcion que recibe dos imagenes y las fusiona sin ecualizar  
def punto11(IMG1,IMG2):
    plt.subplot(2,2,1)
    plt.imshow(IMG1)
    plt.subplot(2,2,2)
    plt.imshow(IMG2)
    plt.subplot(2,2,3)
    plt.title("imagen fusionada")
    img = fusionImgsinEc(IMG1,IMG2)
    plt.imshow(img)
    plt.show()
#12 funcion que recibe dos imagenes y las fusiona con ecualizacion
def punto12(IMG1,IMG2):
    plt.subplot(2,2,1)
    plt.imshow(IMG1)
    plt.subplot(2,2,2)
    plt.imshow(IMG2)
    plt.subplot(2,2,3)
    plt.title("imagen fusionada")
    img = fusionImgconEc(IMG1,IMG2, 0.5)
    plt.imshow(img)
    plt.show() 
#13 funcion que recibe dos imagenes y las fusiona con ecualizacion segun el factor
def punto13(IMG1,IMG2,factor):
    plt.subplot(2,2,1)
    plt.imshow(IMG1)
    plt.subplot(2,2,2)
    plt.imshow(IMG2)
    plt.subplot(2,2,3)
    plt.title("imagen fusionada")
    img = fusionImgconEc(IMG1,IMG2, factor)
    plt.imshow(img)
    plt.show()
#14 funcion que recibe una imagen y retorna el promedio average
def punto14(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = average(IMG)
    plt.imshow(img)
    plt.show()
#15 funcion que recibe una imagen y retorna el promedio average con escala de grises
def punto15(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = average(IMG)
    plt.imshow(img, cmap='gray')
    plt.show()
#16 funcion que recibe una imagen y la retorna con escala de gris con la tecnica de luminosidad
def punto16(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = luminosidad(IMG)
    plt.imshow(img, cmap='gray')
    plt.show()
#17 funcion que recibe una imagen y la retorna con escala de gris con la tecnica de midgray
def punto17(IMG):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = midgray(IMG)
    plt.imshow(img, cmap='gray')
    plt.show()

def main():
    while True:
        print("Menu:")
        print("1. Punto 1")
        print("2. Punto 2")
        print("3. Punto 3")
        print("4. Punto 4")
        print("5. Punto 5")
        print("6. Punto 6")
        print("7. Punto 7")
        print("8. Punto 8")
        print("9. Punto 9")
        print("10. Punto 10")
        print("11. Punto 11")
        print("12. Punto 12")
        print("13. Punto 13")
        print("14. Punto 14")
        print("15. Punto 15")
        print("16. Punto 16")
        print("17. Punto 17")
        print("0. Exit")
        choice = input("Ingresa una opcion: ")

        if choice == '1':
            punto1()
        elif choice == '2':
            punto2()
        elif choice == '3':
            punto3(IMG1)
        elif choice == '4':
            punto4(IMG1)
        elif choice == '5':
            punto5(IMG1)
        elif choice == '6':
            punto6(IMG1)
        elif choice == '7':
            punto7(IMG1)
        elif choice == '8':
            punto8(IMG1)
        elif choice == '9':
            punto9(IMG1)
        elif choice == '10':
            imgR = ReturnR(IMG1)
            imgG = ReturnG(IMG1)
            imgB = ReturnB(IMG1)
            punto10(imgR,imgG,imgB)
        elif choice == '11':
            punto11(IMG1, IMG2)
        elif choice == '12':
            punto12(IMG1, IMG2)
        elif choice == '13':
            factor = float(input("ingrese el factor de 0 a 1: "))
            punto13(IMG1, IMG2, factor)
        elif choice == '14':
            punto14(IMG1)
        elif choice == '15':
            punto15(IMG1)
        elif choice == '16':
            punto16(IMG1)
        elif choice == '17':
            punto17(IMG1)            
        elif choice == '0':
            break
        else:
            print("opcion invalida.")

if __name__ == "__main__":
    main()