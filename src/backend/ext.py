#Fichero innecesario.

#Usado para calcular nodo más centrado. SOLUCIÓN: nodo más centrado: Garibaldi
import statistics
import math
import IA.src.backend.cargar_grafo

def dist(t1, t2):
    #distancia a partir de tuplas

    x1, y1 = t1
    x2, y2 = t2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def cargar_nodos(d):
    #parsear el fichero nodos.txt

    RADIO = 6371
    FICH_NODOS = "backend/nodos.txt"


    file = open(FICH_NODOS)

    lineas = file.readlines()
    for linea in lineas:
        if not linea or linea.startswith("#") or linea.startswith("\n"):
            continue

        linea = linea.strip()
        partes = linea.split()

        # Coordenadas (phi, tetha) Altitud y longitud
        nombre, phi, tetha = partes


        d[nombre] = (float(phi), float(tetha))

    return d
def min():


    d = dict()
    dict_nodes = cargar_nodos(d)

    media = dict_nodes.values
    lcoordx = []
    lcoordy = []
    for comp in dict_nodes.items():

        nombre, coord = comp
        x, y = coord

        lcoordx.append(x)
        lcoordy.append(y)

    mediax = statistics.mean(lcoordx)
    mediay = statistics.mean(lcoordy)

    minimo = 9999
    ciumin = ""

    for comp in dict_nodes.items():

        nombre, coord = comp
        d = dist(coord, (mediax, mediay))

        if (d < minimo):
            minimo = d
            ciumin = nombre

    print(ciumin, x, y)


    return ciumin