#Necesario métodos:

#1: Imprimir grafo "a secas"

#2: Imprimir grafo resaltando aristas de la ruta

#3: Posible método borrar, puede que solape con 1


import matplotlib.pyplot as plt     #Librería gráfica
import networkx as nx   #Librería de grafos

# import tkinter as tk
import backend.ruta as ruta
from backend import cargar_grafo as cg
import pygame
import os

FICH_NODOS = "gui/coord.txt"
# FICH_NODOS = "backend/nodos.txt"

def dibujar(buscador):
    
    pygame.init()
    size = (750,724)
    screen = pygame.display.set_mode(size)

    img_path = "gui/plano.jpg" # plano del metro sobre el que dibujamos
    image = pygame.image.load(img_path).convert()
    # coordenadas = g.dict_nodos.get("Cuire") # estas coord no me sirven
    # print(coordenadas)

    coord_nodos = [
         (85, 586), (184, 539), (224, 500), (263, 460), (302, 423), (330, 358), (329, 276), (400, 255), (418, 211)
        , (206, 39), (177, 89), (198, 127), (223, 152), (226, 177), (26, 74), (24, 127), (24, 187), (167, 251)
        , (277, 358), (380, 357), (433, 358), (484, 358), (523, 388), (536, 441), (537, 507), (536, 594), (537, 710),
        (143,370),(186, 331),(217, 298),(230, 232),(226, 178),(295, 161),
        (366, 161),(437, 163),(497, 159),(555, 159),(594, 195),(627, 233),(668, 271),(728, 308)]

    # Create a font object
    font = pygame.font.Font(None, 36) # cambiar el font del texto y poner botones
    textoPartida = font.render("Elija una estación de partida.",True, (0,0,0), (255,255,255))
    textoDestino = font.render("Elija una estación de destino.",True, (0,0,0), (255,255,255))
    textoRuta = font.render("Ruta mas corta.",True, (0,0,0), (255,255,255))
    
    # Clear the screen
    screen.fill((255, 255, 255))

    # Display the image
    screen.blit(image, (0, 0))

    # Main game loop
    running = True
    pantallaInicio = True
    while running:
        if pantallaInicio:
            for pos in coord_nodos:
                pygame.draw.circle(screen, (255, 255, 255), pos, 6)  # White circle
                pygame.draw.circle(screen, (0, 0, 0), pos, 8, 2)  # Black border

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for circle_pos in coord_nodos:
                        if pygame.Rect(circle_pos[0] - 10, circle_pos[1] - 10, 20, 20).collidepoint(pos):
                            # print("Estacion de partida: ", circle_pos)
                            nodoInicio = nombreNodo(circle_pos)
                            pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # White circle
                            pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
                            estacionPartida = True
                            pantallaInicio = False

        elif estacionPartida:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # Check if the click is inside any of the circles
                    for circle_pos in coord_nodos:
                        if pygame.Rect(circle_pos[0] - 10, circle_pos[1] - 10, 20, 20).collidepoint(pos):
                            nodoDestino = nombreNodo(circle_pos)
                            pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # White circle
                            pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
                            estacionPartida = False
                            estacionLlegada = True
                        
        elif estacionLlegada:
            l = ruta.ruta(buscador, nodoInicio, nodoDestino, "distancia")
            
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
                                    # print(circle_pos)
                                    pygame.draw.circle(screen, (255, 0, 0), circle_pos, 9)  # White circle
                                    pygame.draw.circle(screen, (0, 0, 0), circle_pos, 9, 2)  # Black border
            
            
            estacionLlegada = False
            pantallaFinal =True
    
        elif pantallaFinal:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pantallaFinal = False
                    pantallaInicio = True

        if pantallaInicio:
            screen.blit(textoPartida,(370,60))
        elif estacionPartida:
            screen.blit(textoDestino,(370,60))

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