#Cargar nodos y aristas
import math

#Sería buena idea tener guardadas coordenadas (x,y) -> mirar librería GeoPy
#para estimar distancias en línea recta

#Guardar en diccionario (hashmap) de nodo -> tupla (x,y)

import networkx as nx   #Librería de grafos
import math as m        #Matemática

#VARIABLES GLOBALES
FICH_NODOS = "nodos.txt"
FICH_ARISTAS_DISTANCIAS = "aristas_distancia.txt"
RADIO = 6371
dict_nodos = dict()

def distancia(n1, n2):
#Recibe 2 nombres de estaciones


    x1, y1 = dict_nodos[n1]
    x2, y2 = dict_nodos[n2]

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




def coordenadas():

    #Se va a borrar en nada, pero todavía no

    #Devuelve un dict con ciudad -> coordenadas

    ld = estaciones_por_linea()
    #ld = latitud_longitud()

    coord = dict()

    for i in ld:    #Cada diccionario:

        coord.update(i)

    return coord


def cargar_aristas_distancia(g):
    file = open(FICH_ARISTAS_DISTANCIAS)
    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#"):
            continue

        linea = linea.strip()
        estaciones = linea.split()

        # #Formato: estacion1, est2, distancia
        estacion1, estacion2, peso = estaciones

        dist_euclidea = distancia(estacion1, estacion2)

        #Añadir la arista con el peso
        g.add_edge(estacion1, estacion2, weight = peso)


def cargar_aristas_transbordo(g):
    #TODO
    pass

def cargar_nodos(g):
    #parsear el fichero nodos.txt

    PERRACHE = (45.7496, 4.82701)

    file = open(FICH_NODOS)
    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#"):
            continue

        linea = linea.strip()
        partes = linea.split()

        # Coordenadas (phi, tetha) Altitud y longitud
        nombre, phi, tetha = partes

        diff_tetha = PERRACHE[0] - tetha
        diff_phi = PERRACHE[1] - phi

        #Calculo geodesico de las coordenadas
        x = math.pi * RADIO * diff_tetha / 180
        y = math.pi * RADIO * diff_phi / 180

        dict_nodos[nombre] = (x, y)
        g.add_node(nombre)

def cargar_grafo():

    g_distancias = nx.Graph()

    cargar_nodos(g_distancias)
    cargar_aristas_distancia(g_distancias)

    g_transbordos = nx.Graph()
    cargar_nodos(g_distancias)
    cargar_aristas_transbordo(g_transbordos)

    return (g_distancias, g_transbordos)




def cargar_grafo_deprecated():

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
