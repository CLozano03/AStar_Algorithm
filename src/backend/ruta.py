import networkx as nx   #Librería de grafos

def ruta(g, u, v):

    return nx.astar_path(g, u, v)   #xd

