'''
Universidad Tecnologica de Pereira
Materia: COMPUTACION GRAFICA
Taller: Graficador basico
ESTUDIANTE: Andres Mejia Vergara
'''

import pygame
import math
import os

def Dibujar():
    pygame.init()
    Ventana = pygame.display.set_mode((801,521))
    Tablero = pygame.image.load(os.path.join("Tablero.png"))
    Exit = False    

    x = 0
    y = 0  

    Figura = 0

    color = 0
    ColorElegido = (255,255,255)
    ColorLinea = (255,255,255)
    ColorRelleno = (255,255,255)
    lineaColor = 0
    rellenoColor = 0

    VecesPulsado = 0
    puntoX1 = 0
    puntoY1 = 0
    puntoX2 = 0
    puntoY2 = 0
    pintar = 0

    Comenzar = 0
    Rayar = 0
    xRayar = 0
    yRayar = 0

    Ventana.blit(Tablero, (0,0))

    while not Exit:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                exit()
            if Eventos.type == pygame.MOUSEBUTTONDOWN:
                x,y = Eventos.pos
                Comenzar = 1
            if Comenzar == 1:
                if Eventos.type == pygame.MOUSEMOTION:
                   xRayar,yRayar = Eventos.pos
                   Rayar = 1
            if Eventos.type == pygame.MOUSEBUTTONUP:
                Rayar = 0
                Comenzar = 0
            #Clicks de las Figuras
            if (x >= 0 and y >= 30 and x <= 54 and y <= 77):
                Figura = 0
                VecesPulsado = 0
                puntoX1 = 0
                puntoY1 = 0
                puntoX2 = 0
                puntoY2 = 0
                pintar = 0
            if (x >= 70 and y >= 30 and x <= 125 and y <= 77):
                Figura = 1
                VecesPulsado = 0
                puntoX1 = 0
                puntoY1 = 0
                puntoX2 = 0
                puntoY2 = 0
                pintar = 0
            if (x >= 144 and y >= 30 and x <= 198 and y <= 77):
                Figura = 2
                VecesPulsado = 0
                puntoX1 = 0
                puntoY1 = 0
                puntoX2 = 0
                puntoY2 = 0
                pintar = 0
            if (x >= 0 and y >= 93 and x <= 55 and y <= 140):
                Figura = 3
                VecesPulsado = 0
                puntoX1 = 0
                puntoY1 = 0
                puntoX2 = 0
                puntoY2 = 0
                pintar = 0
            if (x >= 70 and y >= 93 and x <= 125 and y <= 140):
                Figura = 4
                VecesPulsado = 0
                puntoX1 = 0
                puntoY1 = 0
                puntoX2 = 0
                puntoY2 = 0
                pintar = 0
            
            #Clicks en los colores
            #Primera Fila
            if (x >= 265 and y >= 30 and x <= 320 and y <= 77):
                color = 0
                ColorElegido = (255,255,255)
            if (x >= 340 and y >= 30 and x <= 400 and y <= 77):
                color = 1
                ColorElegido = (153,153,153)
            if (x >= 420 and y >= 30 and x <= 480 and y <= 77):
                color = 2
                ColorElegido = (0,0,0)
            if (x >= 500 and y >= 30 and x <= 557 and y <= 77):
                color = 3
                ColorElegido = (255,255,0)

            #Segunda Fila     
            if (x >= 260 and y >= 93 and x <= 320 and y <= 140):
                color = 4
                ColorElegido = (255,153,0)
            if (x >= 340 and y >= 93 and x <= 400 and y <= 140):
                color = 5
                ColorElegido = (255,0,0)
            if (x >= 420 and y >= 93 and x <= 480 and y <= 140):
                color = 6
                ColorElegido = (100,159,255)
            if (x >= 500 and y >= 93 and x <= 558 and y <= 140):
                color = 7
                ColorElegido = (121,210,83)
            #Sin relleno
            if (x >= 646 and y >= 59 and x <= 723 and y <= 85):
                lineaColor = color
                ColorLinea = ColorElegido
            #Con relleno
            if (x >= 645 and y >= 120 and x <= 721 and y <= 146):
                rellenoColor = color
                ColorRelleno = ColorElegido
            #Dibujar
            if (x >= 2 and y >= 162 and x <= 798 and y <= 518):
                if VecesPulsado == 0:
                    puntoX1 = x
                    puntoY1 = y
                    VecesPulsado+=1
                elif VecesPulsado == 1:
                    puntoX2 = x
                    puntoY2 = y
                    VecesPulsado-=1
                    pintar = 1
                x=1
                y=1
                # Click para redibujar el tablero
            if( pygame.key.get_pressed()[pygame.K_b]):
                Ventana.blit(Tablero, (0,0))
                
                    
            
        #Sin relleno color que se utiliza
        if lineaColor == 0:
            pygame.draw.rect(Ventana,(255,255,255),(648,60,73,24))
        if lineaColor == 1:
            pygame.draw.rect(Ventana,(153,153,153),(648,60,73,24))
        if lineaColor == 2:
            pygame.draw.rect(Ventana,(0,0,0),(648,60,73,24))
        if lineaColor == 3:
           pygame.draw.rect(Ventana,(255,255,0),(648,60,73,24))
        if lineaColor == 4:
            pygame.draw.rect(Ventana,(255,153,0),(648,60,73,24))
        if lineaColor == 5:
            pygame.draw.rect(Ventana,(255,0,0),(648,60,73,24))
        if lineaColor == 6:
            pygame.draw.rect(Ventana,(100,159,255),(648,60,73,24))
        if lineaColor == 7:
            pygame.draw.rect(Ventana,(121,210,83),(648,60,73,24))

        #Con relleno color que se utiliza
        if rellenoColor == 0:
            pygame.draw.rect(Ventana,(255,255,255),(646,121,73,24))
        if rellenoColor == 1:
            pygame.draw.rect(Ventana,(153,153,153),(646,121,73,24))
        if rellenoColor == 2:
            pygame.draw.rect(Ventana,(0,0,0),(646,121,73,24))
        if rellenoColor == 3:
           pygame.draw.rect(Ventana,(255,255,0),(646,121,73,24))
        if rellenoColor == 4:
            pygame.draw.rect(Ventana,(255,153,0),(646,121,73,24))
        if rellenoColor == 5:
            pygame.draw.rect(Ventana,(255,0,0),(646,121,73,24))
        if rellenoColor == 6:
            pygame.draw.rect(Ventana,(100,159,255),(646,121,73,24))
        if rellenoColor == 7:
            pygame.draw.rect(Ventana,(121,210,83),(646,121,73,24))
            # Botón para redibujar el tablero
         # pygame.draw.rect(Ventana, (255,255,255), (700,15,65,30))
        font = pygame.font.Font(None, 22)
        text = font.render("PRESS B TO CLEAN", True, (0,0,0))
        Ventana.blit(text, (630, 10))

        #Figura que se esta utilizando
        if Figura == 0:
            if pintar == 1:
                rect_x = min(puntoX1,puntoX2)
                rect_y = min(puntoY1, puntoY2)
                rect_width = abs(puntoX2 - puntoX1)
                rect_height = abs(puntoY2 - puntoY1)
                pygame.draw.rect(Ventana, ColorLinea, (rect_x, rect_y, rect_width, rect_height))
                pygame.draw.rect(Ventana, ColorRelleno, (rect_x + 5, rect_y + 5, rect_width - 10, rect_height - 10))
                pintar = 0
        if Figura == 1:
            if pintar == 1:
                if puntoX1+puntoX2>puntoY1+puntoY2:
                    if puntoX1 > puntoX2:
                        radio = (puntoX1-puntoX2)/2
                    else:
                        radio = (puntoX2-puntoX1)/2
                if puntoX1+puntoX1<puntoY1+puntoY2:
                    if puntoY1 > puntoY2:
                        radio = (puntoY1-puntoY2)/2
                    else:
                        radio = (puntoY2-puntoY1)/2

                if puntoX1 < puntoX2 and puntoY1 < puntoY2:
                    pygame.draw.circle(Ventana, ColorLinea, (((puntoX2-puntoX1)/2)+puntoX1, ((puntoY2-puntoY1)/2)+puntoY1), radio)
                    pygame.draw.circle(Ventana, ColorRelleno, (((puntoX2-puntoX1)/2)+puntoX1, ((puntoY2-puntoY1)/2)+puntoY1), radio-5)
                if puntoX1 < puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.circle(Ventana, ColorLinea, (((puntoX2-puntoX1)/2)+puntoX1, ((puntoY1-puntoY2)/2)+puntoY2), radio)
                    pygame.draw.circle(Ventana, ColorRelleno, (((puntoX2-puntoX1)/2)+puntoX1, ((puntoY1-puntoY2)/2)+puntoY2), radio-5)
                if puntoX1 > puntoX2 and puntoY1 < puntoY2:
                    pygame.draw.circle(Ventana, ColorLinea, (((puntoX1-puntoX2)/2)+puntoX2, ((puntoY2-puntoY1)/2)+puntoY1), radio)
                    pygame.draw.circle(Ventana, ColorRelleno, (((puntoX1-puntoX2)/2)+puntoX2, ((puntoY2-puntoY1)/2)+puntoY1), radio-5)
                if puntoX1 > puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.circle(Ventana, ColorLinea, (((puntoX1-puntoX2)/2)+puntoX2, ((puntoY1-puntoY2)/2)+puntoY2), radio)
                    pygame.draw.circle(Ventana, ColorRelleno, (((puntoX1-puntoX2)/2)+puntoX2, ((puntoY1-puntoY2)/2)+puntoY2), radio-5)
                pintar = 0
        if Figura == 2:
            if Rayar == 1 and xRayar > 2 and xRayar < 987 and yRayar > 2 and yRayar < 673:
                pygame.draw.circle(Ventana, ColorLinea, (xRayar, yRayar), 3)
        if Figura == 3:
            if pintar == 1:
                if puntoX1 < puntoX2 and puntoY1 < puntoY2: 
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY1),(((puntoX2-puntoX1)/2)+puntoX1,puntoY2)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1+5,puntoY1+5),(puntoX2-5,puntoY1+5),(((puntoX2-puntoX1)/2)+puntoX1,puntoY2-5)])
                if puntoX1 < puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY1),(((puntoX2-puntoX1)/2)+puntoX1,puntoY2)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1+5,puntoY1-5),(puntoX2-5,puntoY1-5),(((puntoX2-puntoX1)/2)+puntoX1,puntoY2+5)])
                if puntoX1 > puntoX2 and puntoY1 < puntoY2:
                   pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY1),(((puntoX1-puntoX2)/2)+puntoX2,puntoY2)])
                   pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1-5,puntoY1+5),(puntoX2+5,puntoY1+5),(((puntoX2-puntoX1)/2)+puntoX1,puntoY2-5)])
                if puntoX1 > puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY1),(((puntoX1-puntoX2)/2)+puntoX2,puntoY2)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1-5,puntoY1-5),(puntoX2+5,puntoY1-5),(((puntoX1-puntoX2)/2)+puntoX2,puntoY2+5)])
                pintar = 0
        if Figura == 4:
            if pintar == 1:
                if puntoX1 < puntoX2 and puntoY1 < puntoY2:
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY2),(puntoX2,puntoY1)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1+5,puntoY1+5),(puntoX2-5,puntoY2-5),(puntoX2-5,puntoY1+5)])
                if puntoX1 < puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY2),(puntoX1,puntoY2)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1+5,puntoY1-5),(puntoX2-5,puntoY2+5),(puntoX1+5,puntoY2+5)])
                if puntoX1 > puntoX2 and puntoY1 < puntoY2:
                   pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX1,puntoY2),(puntoX2,puntoY2)])
                   pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1-5,puntoY1+5),(puntoX1-5,puntoY2-5),(puntoX2+5,puntoY2-5)])
                if puntoX1 > puntoX2 and puntoY1 > puntoY2:
                    pygame.draw.polygon(Ventana, ColorLinea,[(puntoX1,puntoY1),(puntoX2,puntoY1),(puntoX2,puntoY2)])
                    pygame.draw.polygon(Ventana, ColorRelleno,[(puntoX1-5,puntoY1-5),(puntoX2+5,puntoY1-5),(puntoX2+5,puntoY2+5)])
                pintar = 0

        pygame.display.update()

Dibujar()
