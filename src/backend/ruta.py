import networkx as nx   #Librería de grafos

from . import cargar_grafo as cg #Para la heuristica
import queue    #Para el montículo

def heuristica(n, v):

    #Pasar por nombre
    return cg.distancia(n, v)


def expandir(g, nodo, abierto):

    for n in g.neighbors(nodo):
        if n not in abierto:
            abierto.add(n)




def astar_path(g, inicio, fin, dict_nodos):
    #Toma el grafo, devuelve un diccionario de predecesores

    abiertos = set()
    cerrados = set()

    predecesores = dict()
    distancias = dict()     #Contiene distancias desde inicio hasta origen

    monticulo = queue.PriorityQueue()

    monticulo.put((0, inicio))
    distancias[inicio] = 0
    predecesores[inicio] = inicio
    abiertos.add(inicio)

    while True:
        if len(abiertos) == 0 or monticulo.empty():
            print("No se ha encontrado camino desde {0} a {1}".format(inicio, fin))
            return []

        dist, N = monticulo.get() #Acceso a nodo mejor

        if (N == fin):
            break

        h = dist + heuristica(N, fin)






        abiertos.remove(N)
        cerrados.add(N)

        expandir(g, N, abiertos)


    return predecesores

def reconstruir_ruta(g ,inicio, fin, dict_predecesores):

    #Toma el grafo y un diccionario de predecesores, devuelve una lista de la ruta
    # Funciona y es precioso

    if len(dict_predecesores) == 0:
        return []
    if inicio == fin:
        return [inicio]
        # lista.append(inicio)
    else:
        return [*reconstruir_ruta(g, inicio, dict_predecesores[fin], dict_predecesores), fin]





def ruta(g ,inicio, fin, dict_nodos):

    #Existencia de nodos

    if inicio not in g.nodes or fin not in g.nodes:
        print("Error: no existe el nodo{}".format(inicio))
        return []
    if g.degree(inicio) == 0 or g.degree(fin) == 0:
        print("Error: no existe ruta")
        return []



    predecesores = astar_path(g, inicio, fin, dict_nodos)
    reconstruir_ruta(g, inicio, fin, predecesores)

def ruta_deprecated(g, inicio, fin):

    return nx.astar_path(g, inicio, fin)



