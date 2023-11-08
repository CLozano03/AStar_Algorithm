import networkx as nx   #Librería de grafos

import IA.src.backend.cargar_grafo as cg

def heuristica(n, v):

    return cg.distancia(n, v)

def ruta(g, u, v, dn):

    if u not in g.nodes or v not in g.nodes:
        print("Error, nodo no exitente")
        return []

    def heur(u, v):

        return cg.distancia(u, v)
    l = []
    try:
        l = nx.astar_path(g, u, v) #xd
    except nx.NetworkXNoPath:
        l = []
    return l

