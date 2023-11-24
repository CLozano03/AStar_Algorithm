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
import backend.cargar_grafo as cg
import backend.ruta as ruta


g_dist, g_tras, dict_nodos = cg.cargar_grafo()

print(ruta.ruta(g_dist, "Hotel_de_Ville_Louis_Pradel_A", "Grange_Blanche"))
#print(ruta.ruta_deprecated(g_dist, "Cuire", "Gare_de_Venissieux"))
gui.dibujar(g_dist)


'''

for i in g_dist.nodes():
    for j in g_dist.nodes():
        print(f"Ruta de {i} hasta {j}:")

        l1 = ruta.ruta(g_dist, i, j)

        l2 = ruta.ruta_deprecated(g_dist, i, j)

        if l1 == l2:
            print(l1)
        else:
            print("error: ")
            print(l1)
            print(l2)
        print()
'''


#Bucle: selección inicio y fin, calcular ruta e imprimir.

