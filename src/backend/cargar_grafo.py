#Cargar nodos y aristas

#Sería buena idea tener guardadas coordenadas (x,y) -> mirar librería GeoPy
#para estimar distancias en línea recta

#Guardar en diccionario (hashmap) de nodo -> tupla (x,y)

import networkx as nx   #Librería de grafos


def cargar_grafo():

    #Se puede introducir los valores aquí

    #Declarar
    g = nx.Graph()

    #Añadir nodos: nombre cualquier objeto hasheable (int, string etc.)
    # Se pueden añadir en listas

    g.add_node(1)
    g.add_node("Madrid")
    g.add_node("patata")
    g.add_node("hola")


    #Añadir aristas (desde, hasta, weight = peso)
    #Se pueden añadir en listas

    g.add_edge(1, "Madrid", weigth = 2)
    g.add_edge("Madrid", "patata", weigth = 4)
    g.add_edge("hola", "Madrid", weigth = 3)
    g.add_edge("hola", "patata", weigth=4)

    g = nx.florentine_families_graph()
    return g
