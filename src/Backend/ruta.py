import networkx as nx   #Librería de grafos

def ruta(g, u, v):

    if u not in g.nodes or v not in g.nodes:
        print("Error, nodo no exitente")
        return []

    return nx.astar_path(g, u, v)   #xd

