import networkx as nx   #Librería de grafos

from . import cargar_grafo as cg #Para la heuristica
import queue    #Para el montículo

def heuristica(n, v):

    #Pasar por nombre
    return cg.distancia(n, v)


def expandir(g, nodo, abierto):

    pass
       




def astar_path(g, inicio, fin, dict_nodos):
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
    #N no esta definido
    while N != fin and not monticulo.empty():
        if len(abiertos) == 0 or monticulo.empty():
            print("No se ha encontrado camino desde {0} a {1}".format(inicio, fin))
            return []

        dist, N = monticulo.get() #Acceso a nodo mejor
        expandir(g, N, abiertos)
        abiertos.remove(N)
        cerrados.add(N)

        for vecino in g.neighbors(N):
            
            d_actual = distancias_origen[N] + g.edges[N, vecino]['weight']
            
            if distancias_origen.get(N) == None:
                abiertos.add(vecino)
                distancias_origen[vecino] = d_actual

            f = d_actual + heuristica(vecino, fin)
            

            if d_actual < distancias_origen[vecino]:
                distancias_origen[vecino] = d_actual
                monticulo.remove(vecino)
                predecesores[vecino] = N

            monticulo.put((f, vecino))
    









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



