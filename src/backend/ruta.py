import networkx as nx   #Librería de grafos

from . import cargar_grafo as cg #Para la heuristica

def heuristica(n, v):

    return cg.distancia(n, v)

'''
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
'''

def expandir(g, nodo):
    return g.out_edges(nodo)

def astar_path(g ,inicio, fin):

    #Existencia de nodos
    if inicio not in g.nodes:
        print("Error: no existe el nodo{}".format(inicio))
        return []
    elif fin not in g.nodes:
        print("Error: no existe el nodo{}".format(fin))
        return []
    
    cerrados = {}
    abiertos = {inicio}

    while True:
        if len(abiertos) == 0:
            print("No se ha encontrado camino desde {0} a {1}".format(inicio, fin))
            return []
        
        N = abiertos.pop()
        if(N == fin):
            return N
        cerrados.append(N)

        sucesores = expandir(g, N)

        for S in sucesores:
            if S not in cerrados and S not in abiertos:
                # TODO Guardar N como predecesor de S
                abiertos.append(S)

