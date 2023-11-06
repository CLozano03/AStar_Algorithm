#Necesario métodos:

#1: Imprimir grafo "a secas"

#2: Imprimir grafo resaltando aristas de la ruta

#3: Posible método borrar, puede que solape con 1


import matplotlib.pyplot as plt     #Librería gráfica
import networkx as nx   #Librería de grafos
from backend import cargar_grafo as cg


def dibujar(g):

    pos = posicionar(g)

    #Comando genérico para dibujar el grafo.
    #Apuntados muchos parámentros útiles (hay muchos)


    nx.draw(g, pos, with_labels=True, node_size=2000, width = 2, edge_color = "r", font_size=12)

    #Dibujar algunas aristas: parámetro (edge_list = listadearistas)

    '''
    #Idea: dibujar nodos por separado y tocar solo aristas. Está por ver
    draw_networkx_nodes, draw_networkx_edges
    '''

    plt.show()




#Para dibujar antes se necesita calcular los (x,y) de cada nodo.
#La librería tiene algunos layouts, pero se pueden guardar a mano
#Luego se reescala

def posicionar(g):


    #pos = nx.kamada_kawai_layout(g, g.nodes()) #funciona

    pos = cg.coordenadas()

    return pos



