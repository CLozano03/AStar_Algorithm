#Cargar nodos y aristas

#Sería buena idea tener guardadas coordenadas (x,y) -> mirar librería GeoPy
#para estimar distancias en línea recta

#Guardar en diccionario (hashmap) de nodo -> tupla (x,y)

import networkx as nx   #Librería de grafos
import math as m        #Matemática



def distancia(n1, n2):
#Desde las coordenadas
    x1, y1 = n1
    x2, y2 = n2

    return m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def coordenadas():

    #Devolver un diccionario nodo -> (x, y)

    #El cargar nodo usa esto automáticamente
    #Se podría devolver lista de diccionarios

    d = dict()

    d["Perrache"] = (1, 2)
    d["Ampere Victor Hugo"] = (1, 2)
    d["Perrache"] = (1, 3)
    d["Ampere Victor Hugo"] = (1, 4)
    d["Bellecour"] = (2, 4)
    d["Cordeliers"] = (2, 3)
    d["Hotel de Ville Louis Pradel"] = (2, 2)
    d["Foch"] = (2, 1)
    d["Massena"] = (3, 1)
    d["Charpennes Charles Henau"] = (3, 2)
    d["Republique Villeurbanne"] = (3, 3)
    d["Gratte-Ciel"] = (3, 4)
    d["Fiachet"] = (4, 4)
    d["Cusset"] = (4, 3)
    d["Laurent Bonnevay Astroballe"] = (4, 2)
    d["Vaulx-en-Velin La Sole"] = (4, 1)

    return d




def cargar_grafo():

    #Se puede introducir los valores aquí

    #Declarar
    g = nx.Graph()

    #Añadir nodos: nombre cualquier objeto hasheable (int, string etc.)
    # Se pueden añadir en listas

        #Línea A:

    d = coordenadas()
    lista = list(d.keys())

    for elem in lista:

        g.add_node(elem)

    for i in range(0, len(lista) - 1):

        n1 = lista[i]
        n2 = lista[i + 1]

        coord1 = d[n1]
        coord2 = d[n2]

        g.add_edge(n1, n2, weigth = distancia(coord1, coord2))


    #Añadir aristas (desde, hasta, weight = peso)
    #Se pueden añadir en listas

#    g.add_edge(1, "Madrid", weigth = 2)
 #   g.add_edge("Madrid", "patata", weigth = 4)
  #  g.add_edge("hola", "Madrid", weigth = 3)
   # g.add_edge("hola", "patata", weigth=4)

    #g = nx.florentine_families_graph()
    return g

