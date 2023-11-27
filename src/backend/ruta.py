import networkx as nx   #Librería de grafos

from . import cargar_grafo as cg #Para la heuristica
import queue    #Para el montículo

def heuristica_distancia(f, n, v):
#f no vale para nada, pero lo hace fácil de hacer con 2 heurísticas
    #Pasar por nombre
    return cg.distancia(n, v)

def heuristica_trasbordo(dict_por_lineas, actual, fin):

    if dict_por_lineas[actual] == dict_por_lineas[fin]:
        return 0
    else:
        return 1



def nodo_no_descubierto(nodo, distancias_origen):

    return distancias_origen.get(nodo) == None

def descubrir_nodo(vecino, nodo_padre, abiertos, distancias_origen, d_actual, predecesores):
    abiertos.add(vecino)
    distancias_origen[vecino] = d_actual
    predecesores[vecino] = nodo_padre

def mejorar_distancias(vecino, nodo_padre, distancias_origen, d_actual, monticulo, predecesores):
    distancias_origen[vecino] = d_actual
    predecesores[vecino] = nodo_padre




def astar_path(g, heuristica, inicio, fin, dict_por_lineas):
    #Toma el grafo, devuelve un diccionario de predecesores

    abiertos = set()        #Nodos NO visitados
    cerrados = set()        #Nodos visitados

    predecesores = dict()
    distancias_origen = dict()     #Contiene distancias desde inicio hasta origen

    monticulo = queue.PriorityQueue()

    monticulo.put((heuristica(dict_por_lineas, inicio, fin), inicio))
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
            f = d_actual + heuristica(dict_por_lineas, vecino, fin)

            if nodo_no_descubierto(vecino, distancias_origen):
                descubrir_nodo(vecino, N, abiertos, distancias_origen, d_actual, predecesores)

            else:
                if d_actual < distancias_origen[vecino]:
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

def gestor(modo):

    if modo == "distancia":
        return heuristica_distancia
    elif modo == "trasbordo":
        return heuristica_trasbordo
    else:
        print("Error: seleccione distancia o trasbordo")

def ruta(g, inicio, fin, modo, dict_por_lineas):

    #Existencia de nodos

    if inicio not in g.nodes:
        print("Error: no existe el nodo{}".format(inicio))
        return []
    if fin not in g.nodes:
        print("Error: no existe el nodo{}".format(fin))
        return []
    if g.degree(inicio) == 0 or g.degree(fin) == 0:
        print("Error: no existe ruta")
        return []

    heuristica = gestor(modo)

    predecesores = astar_path(g, heuristica, inicio, fin, dict_por_lineas)
    l = reconstruir_ruta(g, inicio, fin, predecesores)

    return l

def long_ruta(g, l):

    acc = 0
    for i in range(0, len(l) - 1):
        acc += g.edges[l[i], l[i+1]]['weight']

    return acc
def ruta_deprecated(g, inicio, fin):

    return nx.astar_path(g, inicio, fin)



