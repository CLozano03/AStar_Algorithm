import networkx as nx   #Librería de grafos

from . import cargar_grafo as cg #Para la heuristica
import queue    #Para el montículo

def heuristica(n, v):

    #Pasar por nombre
    return cg.distancia(n, v)



def nodo_no_descubierto(nodo, distancias_origen):

    return distancias_origen.get(nodo) == None

def descubrir_nodo(vecino, nodo_padre, abiertos, distancias_origen, d_actual, predecesores):
    abiertos.add(vecino)
    distancias_origen[vecino] = d_actual
    predecesores[vecino] = nodo_padre

def mejorar_distancias(vecino, nodo_padre, distancias_origen, d_actual, monticulo, predecesores):
    distancias_origen[vecino] = d_actual
    predecesores[vecino] = nodo_padre




def astar_path(g, inicio, fin):
    #Toma el grafo, devuelve un diccionario de predecesores

    abiertos = set()        #Nodos NO visitados
    cerrados = set()        #Nodos visitados

    predecesores = dict()
    distancias_origen = dict()     #Contiene distancias desde inicio hasta origen

    monticulo = queue.PriorityQueue()

    monticulo.put((heuristica(inicio,fin), inicio))
    distancias_origen[inicio] = 0

    predecesores[inicio] = inicio
    abiertos.add(inicio)

    N = inicio  #Nodo actual, inicialmente es el inicio


    while N != fin and not monticulo.empty():

        if len(abiertos) == 0 or monticulo.empty():
            print("No se ha encontrado camino desde {0} a {1}".format(inicio, fin))
            break

        dist, N = monticulo.get() #Acceso a nodo mejor

        if N not in abiertos:
            continue        #A veces introduce varios nodos abiertos en el montículo, evita un fallo

        abiertos.remove(N)
        cerrados.add(N)


        for vecino in g.neighbors(N):

            if vecino in cerrados:
                continue

            d_actual = distancias_origen[N] + g.edges[N, vecino]['weight']
            f = d_actual + heuristica(vecino, fin)

            if nodo_no_descubierto(vecino, distancias_origen):
                descubrir_nodo(vecino, N, abiertos, distancias_origen, d_actual, predecesores)

            elif d_actual < distancias_origen[vecino]:
                mejorar_distancias(vecino, N, distancias_origen, d_actual, monticulo, predecesores)


            monticulo.put((f, vecino))

    return predecesores

def reconstruir_ruta(g ,inicio, fin, dict_predecesores):

    #Toma el grafo y un diccionario de predecesores, devuelve una lista de la ruta
    # Funciona y es precioso

    if len(dict_predecesores) == 0:
        return []
    if inicio == fin:
        return [inicio]
    else:
        return [*reconstruir_ruta(g, inicio, dict_predecesores[fin], dict_predecesores), fin]


def ruta(g ,inicio, fin):

    #Existencia de nodos

    if inicio not in g.nodes or fin not in g.nodes:
        print("Error: no existe el nodo{}".format(inicio))
        return []
    if g.degree(inicio) == 0 or g.degree(fin) == 0:
        print("Error: no existe ruta")
        return []

    predecesores = astar_path(g, inicio, fin)
    l = reconstruir_ruta(g, inicio, fin, predecesores)

    return l

def ruta_deprecated(g, inicio, fin):

    return nx.astar_path(g, inicio, fin)



