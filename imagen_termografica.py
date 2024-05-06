import numpy as np
import matplotlib
import matplotlib.pyplot as plt

ImagenTiff=np.array(plt.imread("FLIR_00088.tiff"))
D=np.double(ImagenTiff)
TemMin=-40
TemMax=160
MBits=14
MatrizCenti=np.array((TemMax-TemMin)*D/2**MBits+TemMin) #Convierte los datos e la matriz en grados centigrados.

fig=plt.figure("Imagen termografica")
plt.imshow(MatrizCenti, cmap=plt.cm.hot_r)  #Muestra la imagen con el mapa de color "hot_r"
coordenada_max=np.argwhere(MatrizCenti==np.max(MatrizCenti))[0]
coordenada_min=np.argwhere(MatrizCenti==np.min(MatrizCenti))[0]
print(f"Coordenada Maxima:{tuple(coordenada_max)}")
print(f"Coordenada Minima:{tuple(coordenada_min)}")
plt.plot(coordenada_max[1],coordenada_max[0],'wo')
plt.plot(coordenada_min[1],coordenada_min[0],'bd')
                 
plt.colorbar(shrink=.92)    #Escala de la barra de la imagen
plt.figure("Histograma")
hist, bins =np.histogram(MatrizCenti, np.arange(0,TemMax), density=True)   #np.histogram
                                                                            #organiza los datos de la matriz en un arreglo que contiene los datos del histograma
HistoTempeBar=np.int32(MatrizCenti.round())
plt.hist(HistoTempeBar, 5, facecolor='red', alpha=0.5)  #Grafica el histograma

print(f"Promedio:{np.mean(MatrizCenti)}")
print(f"Mediana:{np.median(MatrizCenti)}")
print(f"Moda:{np.argmax(MatrizCenti)}")

print(f"Maximo:{np.max(MatrizCenti)}")
print(f"Minimo:{np.min(MatrizCenti)}")

                           



 
plt.show()



