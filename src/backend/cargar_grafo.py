#Cargar nodos y aristas


#Sería buena idea tener guardadas coordenadas (x,y) -> mirar librería GeoPy
#para estimar distancias en línea recta

#Guardar en diccionario (hashmap) de nodo -> tupla (x,y)

import networkx as nx   #Librería de grafos
import math             #Matemática


#VARIABLES GLOBALES
FICH_NODOS = "backend/nodos.txt"
FICH_ARISTAS_DISTANCIAS = "backend/aristas_distancia.txt"
FICH_ARISTAS_TRASBORDOS= "backend/aristas_trasbordo.txt"
RADIO = 6371
dict_nodos = dict()

def distancia(n1, n2):
#Recibe 2 nombres de estaciones

    x1, y1 = dict_nodos[n1]
    x2, y2 = dict_nodos[n2]

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def coordenadas():
    #Lo piden desde FrontEnd
    return dict_nodos

def cargar_aristas_distancia(g):

    file = open(FICH_ARISTAS_DISTANCIAS)
    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#") or linea.startswith("\n"):
            continue

        linea = linea.strip()

        # #Formato: estacion1, est2, distancia
        estacion1, estacion2, peso = linea.split()

        #dist_euclidea = distancia(estacion1, estacion2)

        if estacion1 not in g.nodes or estacion2 not in g.nodes:
            #Para evitar fallos de escritura en el fichero
            raise Exception
            print("Estación no en mapa")

        #Añadir la arista con el peso
        g.add_edge(estacion1, estacion2, weight = float(peso))


def cargar_aristas_transbordo(g):

    file = open(FICH_ARISTAS_TRASBORDOS)
    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#") or linea.startswith("\n"):
            continue

        linea = linea.strip()

        # #Formato: estacion1, est2, distancia
        estacion1, estacion2, peso = linea.split()

        if estacion1 not in g.nodes or estacion2 not in g.nodes:
            #Para evitar fallos de escritura en el fichero
            print("Estación no en mapa")
            raise Exception

        #Añadir la arista con el peso
        g.add_edge(estacion1, estacion2, weight = int(peso))


def cargar_nodos(g):
    #parsear el fichero nodos.txt

    GARIBALDI = (45.75160, 4.85398)


    file = open(FICH_NODOS)
    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#") or linea.startswith("\n"):
            continue

        linea = linea.strip()
        partes = linea.split()

        # Coordenadas (phi, tetha) Altitud y longitud
        nombre, phi, tetha = partes

        diff_phi = float(phi) - GARIBALDI[0]
        diff_tetha = float(tetha) - GARIBALDI[1]

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
    cargar_nodos(g_transbordos)
    cargar_aristas_transbordo(g_transbordos)

    return (g_distancias, g_transbordos, dict_nodos)




