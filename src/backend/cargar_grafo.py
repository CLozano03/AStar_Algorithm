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

def estaciones_por_linea():

    #Devolver una lista de diccionarios nodo -> (x, y)
    #Un diccionario por línea de metro

    #El cargar grafo usa esto automáticamente

    dA = dict()

    lista = []

    #Línea A:
    dA["Perrache"] = (-2, -1)
    dA["Ampere Victor Hugo"] = (-2, 0)
    dA["Bellecour"] = (-2, 2)
    dA["Cordeliers"] = (-2, 3)
    dA["Hotel de Ville Louis Pradel"] = (-2, 4)
    dA["Foch"] = (-1, 4)
    dA["Massena"] = (0, 4)
    dA["Charpennes Charles Henau"] = (1, 4)
    dA["Republique Villeurbanne"] = (2, 4)
    dA["Gratte-Ciel"] = (3, 3)
    dA["Fiachet"] = (4, 3)
    dA["Cusset"] = (5, 2)
    dA["Laurent Bonnevay Astroballe"] = (6, 2)
    dA["Vaulx-en-Velin La Sole"] = (7, 2)

    lista.append(dA)

   #Línea B:

    dB = dict()

    dB["Oullins Gare"] = (-4, -7)
    dB["Stade de Gerland"] = (-3, -6)
    dB["Debourg"] = (-2, -5)
    dB["Place Jean Jaures"] = (-1.5, -3)
    dB["Jean Mace"] = (-1, -2)
    dB["Saxe Gambetta"] = (0, 0)
    dB["Place Guichard Bourse du Travail"] = (0, 1)
    dB["Gare Part Dieu Vivier Merle"] = (1, 2)
    dB["Brotteaux"] = (1, 3)
    dB["Charpennes Charles Henau"] = (1, 4)

    lista.append(dB)

    dC = dict()

    dC["Cuire"] = (-2, 8)
    dC["Henon"] = (-3, 7)
    dC["Croix-Rousse"] = (-2, 6)
    dC["Croix-Paquet"] = (-2, 5)
    dC["Hotel de Ville Louis Pradel"] = (-2, 4)

    lista.append(dC)

    dD = dict()

    dD["Gare de Vaise"] = (-5, 6)
    dD["Valmy"] = (-5, 5)
    dD["Gorge de Loup"] = (-5, 4)
    dD["Vieux Lyon Cathedrale St. Jean"] = (-3, 3)
    dD["Bellecour"] = (-2, 2)
    dD["Guillotiere"] = (-1, 1)
    dD["Saxe Gambetta"] = (0, 0)
    dD["Garibaldi"] = (1, -1)
    dD["Sans-Souci"] = (2, -2)
    dD["Monplaisir-Lumiere"] = (3, -3)
    dD["Grange Blanche"] = (4, -4)
    dD["Laennec"] = (5, -5)
    dD["Mermoz Pinel"] = (5, -6)
    dD["Parrilly"] = (5, -7)
    dD["Gare de Venissieux"] = (5, -8)

    lista.append(dD)

    #Cuidado: las estructuras son inmutables.

    return lista



def latitud_longitud():

    d = dict()


    # Línea A:
    d["Perrache"] = (45.74960, 4.82701)
    d["Ampere Victor Hugo"] = (45.75290, 4.82909)
    d["Bellecour"] = (45.75782, 4.83356)
    d["Cordeliers"] = (45.76325, 4.83569)
    d["Hotel de Ville Louis Pradel"] = (45.76741, 4.83628)
    d["Foch"] = (45.76866, 4.84425)
    d["Massena"] = (45.76936, 4.85294)
    d["Charpennes Charles Henau"] = (45.77054, 4.86306)
    d["Republique Villeurbanne"] = (45.77052, 4.87452)
    d["Gratte-Ciel"] = (45.76905, 4.88251)
    d["Fiachet"] = (45.76765, 4.88976)
    d["Cusset"] = (45.76570, 4.90040)
    d["Laurent Bonnevay Astroballe"] = (45.76481, 4.90892)
    d["Vaulx-en-Velin La Sole"] = (45.76102, 4.92214)


    # Línea B:


    d["Oullins Gare"] = (45.71682, 4.81469)
    d["Stade de Gerland"] = (45.72704, 4.83081)
    d["Debourg"] = (45.73133, 4.83356)
    d["Place Jean Jaures"] = (45.73800, 4.83751)
    d["Jean Mace"] = (45.74586, 4.84236)
    d["Saxe Gambetta"] = (45.75386, 4.84689)
    d["Place Guichard Bourse du Travail"] = (45.75937, 4.84754)
    d["Gare Part Dieu Vivier Merle"] = (45.76145, 4.85783)
    d["Brotteaux"] = (45.76680, 4.85940)
    d["Charpennes Charles Henau"] = (45.77054, 4.86306)

    #Línea C:
    d["Cuire"] = (45.78589, 4.83331)
    d["Henon"] = (45.77920, 4.82738)
    d["Croix-Rousse"] = (45.77431, 4.83174)
    d["Croix-Paquet"] = (45.77089, 4.83595)
    d["Hotel de Ville Louis Pradel"] = (45.76741, 4.83628)

    #Línea D:
    d["Gare de Vaise"] = (45.78040, 4.80504)
    d["Valmy"] = (45.77462, 4.80550)
    d["Gorge de Loup"] = (45.76602, 4.80512)
    d["Vieux Lyon Cathedrale St. Jean"] = (45.75992, 4.82521)
    d["Bellecour"] = (45.75784, 4.83337)
    d["Guillotiere"] = (45.75536, 4.86235)
    d["Saxe Gambetta"] = (45.75386, 4.84689)
    d["Garibaldi"] = (45.75160, 4.85398)
    d["Sans-Souci"] = (45.74793, 4.86433)
    d["Monplaisir-Lumiere"] = (45.74980, 4.86285)
    d["Grange Blanche"] = (45.74298, 4.87892)
    d["Laennec"] = (45.73839, 4.88560)
    d["Mermoz Pinel"] = (45.73039, 4.88668)
    d["Parrilly"] = (45.71943, 4.88687)
    d["Gare de Venissieux"] = (45.70521, 4.88791)


    # Cuidado: las estructuras son inmutables.

    return d

def coordenadas():

    #Devuelve un dict con ciudad -> coordenadas

    #ld = estaciones_por_linea()
    ld = latitud_longitud()

    coord = dict()

    for i in ld:    #Cada diccionario:

        coord.update(i)

    return coord

def cargar_grafo():

    #Se puede introducir los valores aquí

    #Declarar
    g = nx.Graph()

    #Añadir nodos: nombre cualquier objeto hasheable (int, string etc.)
    # Se pueden añadir en listas

    estaciones = estaciones_por_linea()

    for d in estaciones:
        lista = []

        for elem in d.keys():

            g.add_node(elem)
            lista.append(elem)

        #Añadir aristas auto para vértices adyacentes
        for i in range(0, len(lista) - 1):

            n1 = lista[i]
            n2 = lista[i + 1]

            coord1 = d[n1]
            coord2 = d[n2]

            # Añadir aristas (desde, hasta, weight = peso)
            g.add_edge(n1, n2, weigth = distancia(coord1, coord2))
            #Por cambiar: peso de las aristas (según tiempo, distancia...)

        lista.clear()


    #Por hacer: trasbordos

   #Se pueden añadir en listas

    return g

