import matplotlib.pyplot as plt     #Librería gráfica
import networkx as nx   #Librería de grafos

import backend.ruta as ruta
from backend import cargar_grafo as cg
import pygame
import os
import time

FICH_NODOS = "gui/coord.txt"

def dibujar(g):
    
    pygame.init()
    size = (800,724)
    screen = pygame.display.set_mode(size)

    img_path = "gui/plano.jpg" # plano del metro sobre el que dibujamos
    image = pygame.image.load(img_path).convert()

    coord_nodos = [
         (85, 586), (184, 539), (224, 500), (263, 460), (302, 423), (330, 358), (329, 276), (400, 255), (418, 211)
        , (206, 39), (177, 89), (198, 127), (223, 152), (226, 177), (26, 74), (24, 127), (24, 187), (167, 251)
        , (277, 358), (380, 357), (433, 358), (484, 358), (523, 388), (536, 441), (537, 507), (536, 594), (537, 710),
        (143,370),(186, 331),(217, 298),(230, 232),(226, 178),(295, 161),
        (366, 161),(437, 163),(497, 159),(555, 159),(594, 195),(627, 233),(668, 271),(728, 308)]

    coord_botones = [(705, 575),(729, 575)]
    
    # creo los txts de mensajes que van saliendo por pantalla
    font = pygame.font.Font(None, 36)
    textoPartida = font.render("Elija una estación de partida.",True, (0,0,0), (255,255,255))
    textoDestino = font.render("Elija una estación de destino.",True, (0,0,0), (255,255,255))
    textoModo = font.render("Elija el modo que desee:         ",True, (0,0,0), (255,255,255))
    textoFin = font.render("¡Buen viaje!",True, (0,0,0), (255,255,255))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Display the image
    screen.blit(image, (0, 0))

    # Main game loop
    running = True
    pantallaInicio = True

    botonDist = Boton(654, 439, 100, 40, (123, 175, 212), (255, 0, 0), "Distancia")
    botonTras = Boton(654, 513, 100, 40, (123, 175, 212), (255, 0, 0), "Trasbordo")
    botonRein = Boton(654, 587, 100, 40, (123, 175, 212), (255, 0, 0), "Reiniciar")

    while running:
        if pantallaInicio: # es la pantalla pp, en la que escoges estacionInicio
            
            # si reinicio la pantalla, vuelvo a dibujar el plano y empiezo de nuevo (sino se pinta encima del otro)
            screen.fill((255, 255, 255))
            screen.blit(image, (0, 0))

            for pos in coord_nodos:
                pygame.draw.circle(screen, (255, 255, 255), pos, 6)  # White circle
                pygame.draw.circle(screen, (0, 0, 0), pos, 8, 2)  # Black border

            # restablecer el color de los botones, cuando pulsas uno se vuelve rojo
            botonDist.color_normal = (123, 175, 212)
            botonTras.color_normal = (123, 175, 212)
            botonRein.color_normal = (123, 175, 212)
            botonDist.dibujar(screen)
            botonTras.dibujar(screen)
            botonRein.dibujar(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for circle_pos in coord_nodos:
                        if pygame.Rect(circle_pos[0] - 10, circle_pos[1] - 10, 20, 20).collidepoint(pos):
                            nodoInicio = nombreNodo(circle_pos)
                            pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # White circle
                            pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
                            estacionPartida = True
                            pantallaInicio = False

        elif estacionPartida: # ya se ha elegido la estacPartida, ahora escoger la de destino
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for circle_pos in coord_nodos:
                        if pygame.Rect(circle_pos[0] - 10, circle_pos[1] - 10, 20, 20).collidepoint(pos):
                            if (nombreNodo(circle_pos)!= nodoInicio):
                                nodoDestino = nombreNodo(circle_pos)
                                pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # White circle
                                pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
                                estacionPartida = False
                                botonRuta = True
        elif botonRuta: # una vez elegidas ambas estaciones, escoges el modo (distancia o trasbordos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if botonDist.pulsado():
                        botonDist.color_normal = botonDist.color_pulsado
                        botonDist.dibujar(screen)
                        l = ruta.ruta(g, nodoInicio, nodoDestino, "distancia")
                        botonRuta = False
                        dibujaRuta= True
                    if botonTras.pulsado():
                        botonTras.color_normal = botonTras.color_pulsado
                        botonTras.dibujar(screen)
                        l = ruta.ruta(g, nodoInicio, nodoDestino, "trasbordo")
                        botonRuta = False
                        dibujaRuta= True
                    if botonRein.pulsado():
                        botonRuta = False
                        pantallaInicio = True

        elif dibujaRuta: # dibuja la ruta en el mapa
            posiciones_deseadas = {}
            for nodo in l:
            # Leo el archivo y pongo las coordenadas
                with open(FICH_NODOS, 'r') as archivo:
                    for linea in archivo:
                        if '#' not in linea:
                            # Divide la línea en palabras
                            palabras = linea.split()
                            
                            if len(palabras) >= 3: # para saltarse las lineas vacias
                                nombre = palabras[0]
                                if nombre == nodo:
                                    x = int(palabras[1])
                                    y = int(palabras[2])
                                    circle_pos = (x, y)
                                    pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # Red circle
                                    pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
                                    pygame.display.flip() 
                                    time.sleep(0.1)
                                    
            
            dibujaRuta= False
            pantallaFinal =True
    
        elif pantallaFinal: # puedes pulsar reiniciar y volver a empezar
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if botonRein.pulsado():
                        pantallaFinal = False
                        pantallaInicio = True

        if pantallaInicio:
            screen.blit(textoPartida,(370,60))
        elif estacionPartida:
            screen.blit(textoDestino,(370,60))
        elif botonRuta:
            screen.blit(textoModo,(370,60))
        elif dibujaRuta:
            pygame.draw.rect(screen, (255, 255, 255), (370, 60, 800, 50))
            screen.blit(textoFin,(500,60))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def nombreNodo (coord):
    # Leo el archivo y busco el nombre del nodo que tenga esas coord
        with open(FICH_NODOS, 'r') as archivo:
            for linea in archivo:
                if '#' not in linea:
                    # Divide la línea en palabras
                    palabras = linea.split()
                    
                    if len(palabras) >= 3: # para saltarse las lineas vacias
                        x = int(palabras[1])
                        y = int(palabras[2])
                        if x == coord[0] and y == coord[1]:
                            nombre = palabras[0]
                            return nombre
                        
class Boton:
    def __init__(self, x, y, ancho, alto, color_normal, color_pulsado, texto, font_size=25):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_pulsado = color_pulsado
        self.texto = texto
        self.font = pygame.font.Font(None, font_size)

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color_normal, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1) 

        text_surface = self.font.render(self.texto, True, (255,255,255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def pulsado(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
