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


g_dist, g_tras, dict_nodos, dict_por_lineas = cg.cargar_grafo()


l = ruta.ruta(g_dist, "Perrache", "OullinsGare", "distancia", dict_por_lineas)
print(l)

l = ruta.ruta(g_tras, "Perrache", "OullinsGare", "trasbordo", dict_por_lineas)
print(l)

#print(f"Ruta: {l}")
#print(f"Longitud de nuestra ruta: {ruta.long_ruta(g_dist, l)}")

#l2 = ruta.ruta_deprecated(g_dist, "Gare_de_Venissieux", "Vaulx-en-Velin_La_Sole")
#print(l2)
#print(f"Longitud de ruta de la librería: {ruta.long_ruta(g_dist, l2)}")


#print(ruta.ruta_deprecated(g_dist, "Cuire", "Gare_de_Venissieux"))
#gui.dibujar(g_dist)



#
# for i in g_dist.nodes():
#     for j in g_dist.nodes():
#         print(f"Ruta de {i} hasta {j}:")
#
#         l1 = ruta.ruta(g_dist, i, j, "distancia", dict_por_lineas)
#
#         l2 = ruta.ruta(g_tras, i, j, "trasbordo", dict_por_lineas)
#
#         l3 = ruta.ruta_deprecated(g_dist, i, j)
#
#         if l1 != l2:
#             print("Ruta diferente por trasbordos que por distancias:")
#             print(f"{ruta.long_ruta(g_dist, l1)} frente a {ruta.long_ruta(g_dist, l2)}")
#
#         print(f"Ruta por distancias: {l1}")
#         print(f"Ruta por trasbordos: {l2}")
#         print(f"Ruta de librería: {l3}")
#
#     print()
#


#Bucle: selección inicio y fin, calcular ruta e imprimir.

