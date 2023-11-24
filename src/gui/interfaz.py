#Necesario métodos:

#1: Imprimir grafo "a secas"

#2: Imprimir grafo resaltando aristas de la ruta

#3: Posible método borrar, puede que solape con 1


import matplotlib.pyplot as plt     #Librería gráfica
import networkx as nx   #Librería de grafos

from backend import cargar_grafo as cg


def dibujar(g):

    pos = posicionar(g)

    #Comando genérico para dibujar el grafo.
    #Apuntados muchos parámentros útiles (hay muchos)


    # nx.draw(g, pos, with_labels=True, node_size=2000, width = 2, edge_color = "r", font_size=12)

    
    # # Crear un grafo vacío
    # lineaA = nx.Graph()
    # # Agregar nodos
    # G.add_nodes_from([1, 2, 3, 4])
    # # Agregar aristas
    # G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
    # # Dibujar el grafo
    # nx.draw(G, with_labels=True, font_weight='bold')
    # # Mostrar el dibujo
    # plt.show()

    # LineaA
    lineaA = nx.Graph()
    # lineaA.add_nodes_from(['Perrache', 'Ampere_Victor\n_Hugo', 'Bellecour_A', 'Cordeliers', 
    #                        'Hotel_de_Ville\n_Louis_Pradel_A', 'Foch', 'Massena', 'Charpennes\n_Charles\n_Henau_A',
    #                        'Republique\n_Villeurbanne', 'Gratte-Ciel', 'Fiachet', 'Cusset', 'Laurent_Bonnevay\n_Astroballe',
    #                        'Vaulx-en-Velin_La_Sole'])
    lineaA.add_nodes_from(['Perrache', 'Ampere_Victor_Hugo', 'Bellecour_A', 'Cordeliers', 
                        'Hotel_de_Ville_Louis_Pradel_A', 'Foch', 'Massena', 'Charpennes_Charles_Henau_A',
                        'Republique_Villeurbanne', 'Gratte-Ciel', 'Fiachet', 'Cusset', 'Laurent_Bonnevay_Astroballe',
                        'Vaulx-en-Velin_La_Sole'], names={'Perrache': 'Perrache', 'Ampere_Victor_Hugo': 'Ampere\nVictor\nHugo',
                                                          'Bellecour_A': 'Bellecour A','Cordeliers': 'Cordeliers',
                                                          'Hotel_de_Ville_Louis_Pradel_A': 'Hotel de Ville\nLouis Pradel A',
                                                          'Foch': 'Foch', 'Massena': 'Massena', 
                                                          'Charpennes_Charles_Henau_A': 'Charpennes\nCharles\nHenau A',
                                                          'Republique_Villeurbanne': 'Republique\nVilleurbanne',
                                                          'Gratte-Ciel': 'Gratte-Ciel', 'Fiachet': 'Fiachet', 'Cusset': 'Cusset',
                                                          'Laurent_Bonnevay_Astroballe': 'Laurent\nBonnevay\nAstroballe',
                                                          'Vaulx-en-Velin_La_Sole': 'Vaulx-en-Velin\nLa Sole',})
    
    # lineaA.add_edges_from([('Perrache', 'Ampere_Victor_Hugo'), ('Ampere_Victor\n_Hugo', 'Bellecour_A'), ('Bellecour_A', 'Cordeliers'),('Cordeliers','Hotel_de_Ville\n_Louis_Pradel_A'),('Hotel_de_Ville\n_Louis_Pradel_A', 'Foch'), ('Foch', 'Massena'), ('Massena', 'Charpennes\n_Charles\n_Henau_A')
    #                        ,('Charpennes\n_Charles\n_Henau_A','Republique\n_Villeurbanne'),( 'Republique\n_Villeurbanne', 'Gratte-Ciel'),( 'Republique\n_Villeurbanne', 'Gratte-Ciel'),
    #                        ('Gratte-Ciel', 'Fiachet'),('Fiachet', 'Cusset'),('Cusset', 'Laurent_Bonnevay\n_Astroballe'),('Laurent_Bonnevay\n_Astroballe','Vaulx-en-Velin_La_Sole')])
    lineaA.add_edges_from([('Perrache', 'Ampere_Victor_Hugo'), ('Ampere_Victor_Hugo', 'Bellecour_A'), ('Bellecour_A', 'Cordeliers'),('Cordeliers','Hotel_de_Ville_Louis_Pradel_A'),('Hotel_de_Ville_Louis_Pradel_A', 'Foch'), ('Foch', 'Massena'), ('Massena', 'Charpennes_Charles_Henau_A')
                           ,('Charpennes_Charles_Henau_A','Republique_Villeurbanne'),( 'Republique_Villeurbanne', 'Gratte-Ciel'),( 'Republique_Villeurbanne', 'Gratte-Ciel'),
                           ('Gratte-Ciel', 'Fiachet'),('Fiachet', 'Cusset'),('Cusset', 'Laurent_Bonnevay_Astroballe'),('Laurent_Bonnevay_Astroballe','Vaulx-en-Velin_La_Sole')])




    # LineaB
    lineaB = nx.Graph()
    lineaB.add_nodes_from(['OullinsGare', 'Stade_de_Gerland', 'Debourg', 'Place_Jean_Jaures', 'Jean_Mace', 
                           'Saxe_Gambetta_B', 'Place_Guichard_Bourse_du_Travail', 'Gare_Part_Dieu_Vivier_Merle',
                            'Brotteaux', 'Charpennes_Charles_Henau_B'])
    lineaB.add_edges_from([('OullinsGare', 'Stade_de_Gerland'),('Stade_de_Gerland', 'Debourg'), ( 'Debourg', 'Place_Jean_Jaures'), ('Place_Jean_Jaures', 'Jean_Mace'),
                            ('Jean_Mace', 'Saxe_Gambetta_B'),('Saxe_Gambetta_B', 'Place_Guichard_Bourse_du_Travail'),('Place_Guichard_Bourse_du_Travail', 'Gare_Part_Dieu_Vivier_Merle')
                            ,('Gare_Part_Dieu_Vivier_Merle','Brotteaux'), ('Brotteaux', 'Charpennes_Charles_Henau_B')])

    
    # LineaC
    lineaC = nx.Graph()
    lineaC.add_nodes_from(['Cuire', 'Henon', 'Croix-Rousse', 'Croix-Paquet', 'Hotel_de_Ville_Louis_Pradel_C'])
    lineaC.add_edges_from([('Cuire', 'Henon'), ('Henon', 'Croix-Rousse'), ('Croix-Rousse','Croix-Paquet'), 
                           ('Croix-Paquet', 'Hotel_de_Ville_Louis_Pradel_C')])


    # LineaD
    lineaD = nx.Graph()
    lineaD.add_nodes_from(['Gare_de_Vaise', 'Valmy', 'Gorge_de_Loup', 'Vieux_Lyon_Cathedrale_St_Jean', 
                           'Bellecour_D', 'Guillotiere', 'Saxe_Gambetta_D', 'Garibaldi', 'Sans-Souci', 
                           'Monplaisir-Lumiere', 'Grange_Blanche','Laennec', 'Mermoz_Pinel', 'Parrilly', 
                           'Gare_de_Venissieux'])
    lineaD.add_edges_from([('Gare_de_Vaise', 'Valmy'),( 'Valmy', 'Gorge_de_Loup'),('Gorge_de_Loup', 'Vieux_Lyon_Cathedrale_St_Jean'),
                            ('Vieux_Lyon_Cathedrale_St_Jean', 'Bellecour_D'),('Bellecour_D', 'Guillotiere'),('Guillotiere', 'Saxe_Gambetta_D'),
                            ('Saxe_Gambetta_D', 'Garibaldi'),('Garibaldi', 'Sans-Souci'),('Sans-Souci', 'Monplaisir-Lumiere'),
                            ('Monplaisir-Lumiere', 'Grange_Blanche'),('Grange_Blanche','Laennec'),('Laennec', 'Mermoz_Pinel'),
                            ('Mermoz_Pinel', 'Parrilly'),('Parrilly','Gare_de_Venissieux')])






    # Configurar la disposición de los nodos
    pos1 = nx.spring_layout(lineaA)
    pos2 = nx.spring_layout(lineaB)
    pos3 = nx.spring_layout(lineaC)
    pos4 = nx.spring_layout(lineaD)
   

#----experimentos
   # Personalizar las etiquetas de los nodos ajustando la fuente según el tamaño del nodo
    # for node, (x, y) in pos1.items():
    #     plt.text(x, y, node, fontsize=100/5, ha='center', va='center', color='red')

# Ajustar automáticamente el tamaño de la fuente según la longitud del texto???
    # labelsA = nx.get_node_attributes(lineaA, 'names')

#---fin experimentos

    # Dibujar los 4 grafos superpuestos
    # nx.draw(lineaA, pos1, with_labels=True, node_color='r', edge_color='r')
    nx.draw(lineaA, pos1, with_labels=True, node_size=1000, node_color='skyblue', font_size=5,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='r')
    # nx.draw_networkx_labels(lineaA, pos1, labelsA, font_color='red')
    # nx.draw(lineaB, pos2, with_labels=True, node_color='b', edge_color='b')
    # nx.draw(lineaC, pos3, with_labels=True, node_color='orange', edge_color='orange')
    # nx.draw(lineaD, pos4, with_labels=True, node_color='green', edge_color='green')
    # Mostrar la figura
    plt.show()


    #Dibujar algunas aristas: parámetro (edge_list = listadearistas)

    '''
    #Idea: dibujar nodos por separado y tocar solo aristas. Está por ver
    draw_networkx_nodes, draw_networkx_edges
    '''

    # plt.show()




#Para dibujar antes se necesita calcular los (x,y) de cada nodo.
#La librería tiene algunos layouts, pero se pueden guardar a mano
#Luego se reescala

def posicionar(g):


    #pos = nx.kamada_kawai_layout(g, g.nodes()) #funciona

    pos = cg.coordenadas()

    return pos



