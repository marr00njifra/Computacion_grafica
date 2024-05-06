import numpy as np
import matplotlib.pyplot as plt
from FuncionesA import * 
import cv2

#solucion Taller 5-5
#imagenes usadas
IMG1 = plt.imread('Dog1.jpg')
IMG1 = np.array(IMG1)

IMG2 = plt.imread('Cat1.jpg')
IMG2 = np.array(IMG2)

IMG3 = plt.imread('Bike1.jpg')
IMG3 = np.array(IMG3)


#1
def punto1(IMG, factor):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ajustebrillo(IMG, factor)
    plt.imshow(img)
    plt.show()
    
#punto1(IMG1, 0.5)

#2
def punto2(IMG, canal, factor):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ajustecanal(IMG, canal, factor)
    plt.imshow(img)
    plt.show()
    
#punto2(IMG1, 0, 0.5)


#3
def punto3(IMG, factorcontraste):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = ajustecontraste(IMG, factorcontraste)
    plt.imshow(img)
    plt.show()

#punto3(IMG1, 0.5)

#4 
def punto4(IMG, factor):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = zoom(IMG, factor)
    plt.imshow(img)
    plt.show()
    
#punto4(IMG1, 0.5)

#5
def punto5(IMG, factor):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = binarizar(IMG, factor)
    plt.imshow(img)
    plt.show()
    
#punto5(IMG1, 2)

#6
def punto6(IMG, angulo):
    plt.subplot(2,2,1)
    plt.imshow(IMG)
    plt.subplot(2,2,2)
    img = rotate_image(IMG, angulo)
    plt.imshow(img)
    plt.show()
    
#punto6(IMG1, 60)

#7
def punto7(IMG):
    plt.subplot(2, 2, 1)
    plt.imshow(IMG)
    plt.title('Imagen Original')

    plt.subplot(2, 2, 2)
    imgcapaR = histograma(IMG, color=2)  # 0: Azul, 1: Verde, 2: Rojo
    plt.bar(np.arange(256), imgcapaR[:,0], width=0.1, color='r')  # Ancho de barras ajustado a 0.8
    plt.xlim([0, 256])
    plt.title('Histograma Rojo')

    plt.subplot(2, 2, 3)
    imgcapaG = histograma(IMG, color=1)
    plt.bar(np.arange(256), imgcapaG[:,0], width=0.1, color='g')
    plt.xlim([0, 256])
    plt.title('Histograma Verde')

    plt.subplot(2, 2, 4)
    imgcapaB = histograma(IMG, color=0)
    plt.bar(np.arange(256), imgcapaB[:,0], width=0.1, color='b')
    plt.xlim([0, 256])
    plt.title('Histograma Azul')

    plt.tight_layout()
    plt.show()
    
#punto7(IMG1)

