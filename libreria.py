import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, Sumar dos imagenes
def SumarIMG (img1, img2):
    img1=np.array(img1)/255
    img2=np.array(img2)/255
    img=img1+img2
    return img     

#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, fusionar dos imagenes
def FusionarIMG (img1, img2, factor):
    img1=np.array(img1)/255
    img2=np.array(img2)/255
    img=img1*factor+img2*(1-factor)
    return img

#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, ajustar el brillo de una imagen
def AjustarBrillo (img, factor):
    img=np.array(img)/255
    img=img*factor
    return img

#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, ajustar el brillo de un canal de una imagen
def AjustarBrilloCanal (img, canal, factor):
    img=np.array(img)/255
    img[:,:,canal]=img[:,:,canal]*factor
    return img

#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, invertir los colores de una imagen
def InvertirColores (img):
    img=np.array(img)/255
    img=255-img
    return img

#--------------------------------------------------------------------------------------------------------------------------------
#Funcion, convertir una imagen a escala de grises
def EscalaGrises (img):
    img=np.array(img)/255
    img=img[:,:,0]*0.255+img[:,:,1]*0.587+img[:,:,2]*0.114
    return img




import numpy as np
import matplotlib.pyplot as plt
import Procesamiento as Proc

#--------------------------------------------------------------------------------------------------------------------------------
#Programa principal
img1=plt.imread('img1.jpg')
img2=plt.imread('img2.jpg')

plt.figure(1)

plt.subplot(2,2,1)
plt.imshow(img1)

plt.subplot(2,2,2)
plt.imshow(img2)

img=Proc.SumarIMG(img1, img2)
plt.subplot(2,2,3)
plt.imshow(img)

img=Proc.FusionarIMG(img1, img2, 0.5)
plt.subplot(2,2,4)
plt.imshow(img)

#--------------------------------------------------------------------------------------------------------------------------------
plt.figure(2)
plt.subplot(2,2,1)
img=Proc.AjustarBrillo(img1, 0.5)
plt.imshow(img)

plt.subplot(2,2,2)
img=Proc.AjustarBrilloCanal(img1, 0, 0.5)
plt.imshow(img)

plt.subplot(2,2,3)
img=Proc.InvertirColores(img1)
plt.imshow(img)

plt.subplot(2,2,4)
img=Proc.EscalaGrises(img1)
plt.imshow(img)


plt.show()

