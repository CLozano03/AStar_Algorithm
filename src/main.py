#1º: Se crea el grafo: (backend.cargar_grafo)

#2: Se imprime el grafo: (GUI.interfaz)

    #3º El usuario selecciona clickeando en el grafo la ruta a calcular (GUI.?) ->revisar librería tkinter

    #4º: Se calcula la ruta más corta (backend.ruta)

    #5º: Se dibuja la ruta (GUI.interfaz)

    #6º opcional: el usuario elimina la ruta (se imprime el grafo "a secas")    (GUI.interfaz)

#Bucle. Sigue iterando hasta acabar


import networkx as nx   #Librería de grafos
import matplotlib.pyplot as plt     #Librería gráfica

import gui.interfaz as gui
import backend.cargar_grafo as ini
import backend.ruta as ruta


g = ini.cargar_grafo()

#print(g.degree("Madrid"))
#print(ruta.ruta(g, "hola", 1))

print(ruta.ruta(g, "Barbadori", "Lamberteschi"))


gui.dibujar(g)

