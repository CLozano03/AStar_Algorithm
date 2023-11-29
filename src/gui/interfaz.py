#Necesario métodos:

#1: Imprimir grafo "a secas"

#2: Imprimir grafo resaltando aristas de la ruta

#3: Posible método borrar, puede que solape con 1


import matplotlib.pyplot as plt     #Librería gráfica
import networkx as nx   #Librería de grafos

from backend import cargar_grafo as cg

# FICH_NODOS = "gui/coord.txt"
FICH_NODOS = "backend/nodos.txt"
def dibujar(g):

    # LineaA
    lineaA = nx.Graph()
    lineaA.add_nodes_from(['Perrache', 'Ampere_Victor_Hugo', 'Bellecour_A', 'Cordeliers', 
                        'Hotel_de_Ville_Louis_Pradel_A', 'Foch', 'Massena', 'Charpennes_Charles_Henau_A',
                        'Republique_Villeurbanne', 'Gratte-Ciel', 'Fiachet', 'Cusset', 'Laurent_Bonnevay_Astroballe',
                        'Vaulx-en-Velin_La_Sole'])
    
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


    names={'Perrache': 'Perrache', 'Ampere_Victor_Hugo': 'Ampere\nVictor\nHugo',
            'Bellecour_A': '','Cordeliers': 'Cordeliers',
            'Hotel_de_Ville_Louis_Pradel_A': '',
            'Foch': 'Foch', 'Massena': 'Massena', 
            'Charpennes_Charles_Henau_A': 'Charpennes\nCharles\nHenau',
            'Republique_Villeurbanne': 'Republique\nVilleurbanne',
            'Gratte-Ciel': 'Gratte-Ciel', 'Fiachet': 'Fiachet', 'Cusset': 'Cusset',
            'Laurent_Bonnevay_Astroballe': 'Laurent\nBonnevay\nAstroballe',
            'Vaulx-en-Velin_La_Sole': 'Vaulx-en\n-Velin\nLa Sole',
            
            'OullinsGare': 'Oullins\nGare',
            'Stade_de_Gerland': 'Stade\nde\nGerland',
            'Debourg': 'Debourg',
            'Place_Jean_Jaures': 'Place\nJean\nJaures',
            'Jean_Mace': 'Jean\nMace',
            'Saxe_Gambetta_B': '',
            'Place_Guichard_Bourse_du_Travail': 'Place\nGuichard\nBourse du\nTravail',
            'Gare_Part_Dieu_Vivier_Merle': 'Gare\nPart-Dieu\nVivier\nMerle',
            'Brotteaux': 'Brotteaux',
            'Charpennes_Charles_Henau_B': '',

            'Cuire': 'Cuire',
            'Henon': 'Henon',
            'Croix-Rousse': 'Croix-\nRousse',
            'Croix-Paquet': 'Croix-\nPaquet',
            'Hotel_de_Ville_Louis_Pradel_C': 'Hotel\nde Ville\nLouis\nPradel',

            'Gare_de_Vaise': 'Gare de\n Vaise',
            'Valmy': 'Valmy',
            'Gorge_de_Loup': 'Gorge \nde Loup',
            'Vieux_Lyon_Cathedrale_St_Jean': 'Vieux Lyon\nCathedrale\nSt Jean',
            'Bellecour_D': 'Bellecour',
            'Guillotiere': 'Guillotiere',
            'Saxe_Gambetta_D': 'Saxe\nGambetta',
            'Garibaldi': 'Garibaldi',
            'Sans-Souci': 'Sans-Souci',
            'Monplaisir-Lumiere': 'Monplaisir-\nLumiere',
            'Grange_Blanche': 'Grange\nBlanche',
            'Laennec': 'Laennec',
            'Mermoz_Pinel': 'Mermoz-\nPinel',
            'Parrilly': 'Parrilly',
            'Gare_de_Venissieux': 'Gare de\nVenissieux',}
    
    # Configurar la disposición de los nodos
    # Leo el archivo y pongo las coordenadas
    posiciones_deseadas = {}

    with open(FICH_NODOS, 'r') as archivo:
        for linea in archivo:
            if '#' not in linea:
                # Divide la línea en palabras
                palabras = linea.split()
                
                if len(palabras) >= 3: # para saltarse las lineas vacias
                    
                    nombre = palabras[0]
                    x = float(palabras[1])
                    y = float(palabras[2])
                    
                # Agrega las coordenadas
                posiciones_deseadas[nombre] = (x, y)

    # Imprimo el resultado (para testear)
    # print(posiciones_deseadas)

    # # Configurar la disposición de los nodos
    pos1 = nx.spring_layout(lineaA)
    pos1.update(posiciones_deseadas)
    pos2 = nx.spring_layout(lineaB)
    pos2.update(posiciones_deseadas)
    pos3 = nx.spring_layout(lineaC)
    pos3.update(posiciones_deseadas)
    pos4 = nx.spring_layout(lineaD)
    pos4.update(posiciones_deseadas)

    # pongo lo de label para que los nombres del nodo sean distintos a los de 
    # las etiquetas (Saltos de linea etc)
    nx.set_node_attributes(lineaA, names, 'label')
    nx.set_node_attributes(lineaB, names, 'label')
    nx.set_node_attributes(lineaC, names, 'label')
    nx.set_node_attributes(lineaD, names, 'label')

    # Dibujar los 4 grafos superpuestos
    nx.draw(lineaA, pos1,  with_labels=True, labels=nx.get_node_attributes(lineaA, 'label'), node_size=1800, node_color='red', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='r')
    nx.draw(lineaB, pos2,  with_labels=True, labels=nx.get_node_attributes(lineaB, 'label'), node_size=1800, node_color='skyblue', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='skyblue',)
    nx.draw(lineaC, pos3,  with_labels=True, labels=nx.get_node_attributes(lineaC, 'label'), node_size=1800, node_color='orange', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='orange')
    nx.draw(lineaD, pos4,  with_labels=True, labels=nx.get_node_attributes(lineaD, 'label'), node_size=1800, node_color='green', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='green')
   
    # # Mostrar la figura
    # plt.show()
    plt.show(block=False)
    entrada_usuario = input("Presiona Enter para resaltar la ruta: ")

    # Comprobar si se presionó Enter
    if not entrada_usuario.strip():
        # print("Presionaste Enter")
        # # Aquí agrega el código que se ejecutará después de presionar Enter
        # nx.draw(lineaA, pos1,  with_labels=True, labels=nx.get_node_attributes(lineaA, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        # nx.draw(lineaB, pos2,  with_labels=True, labels=nx.get_node_attributes(lineaB, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey',)
        # nx.draw(lineaC, pos3,  with_labels=True, labels=nx.get_node_attributes(lineaC, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        # nx.draw(lineaD, pos4,  with_labels=True, labels=nx.get_node_attributes(lineaD, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
    
        # # Mostrar solo el camino
        # nx.draw(lineaA, pos1,  with_labels=True, labels=nx.get_node_attributes(lineaA, 'label'), node_size=1500, node_color='purple', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='purple')


        # plt.show()


        # Crear diccionarios de colores para nodos específicos en cada línea || uno para todos (aun no se cual de los 2)
        # colores_nodos_lineaA = {'Hotel_de_Ville_Louis_Pradel_A': 'red', 'Foch': 'red', 'Massena': 'red'}
        # colores_nodos_lineaB = {'Charpennes_Charles_Henau_B': 'blue', 'Brotteaux': 'blue','Place_Guichard_Bourse_du_Travail': 'blue', 'Gare_Part_Dieu_Vivier_Merle': 'blue'}
        # colores_nodos_lineaC = {'Croix-Rousse': 'orange', 'Croix-Paquet': 'orange'}
        # colores_nodos_lineaD = {'Saxe_Gambetta': 'green', 'Garibaldi': 'green'}
        colores_nodos_todos = {'Hotel_de_Ville_Louis_Pradel_C': 'red', 'Foch': 'red', 'Massena': 'red', 'Saxe_Gambetta_D': 'green', 'Garibaldi': 'green'}

        # Dibujar los 4 grafos superpuestos con colores específicos para nodos
        nx.draw(lineaA, pos1, with_labels=True, labels=nx.get_node_attributes(lineaA, 'label'), node_size=1800, node_color=[colores_nodos_todos.get(node, 'grey') for node in lineaA.nodes()], font_size=7, font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        nx.draw(lineaB, pos2, with_labels=True, labels=nx.get_node_attributes(lineaB, 'label'), node_size=1800, node_color=[colores_nodos_todos.get(node, 'grey') for node in lineaB.nodes()], font_size=7, font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        nx.draw(lineaC, pos3, with_labels=True, labels=nx.get_node_attributes(lineaC, 'label'), node_size=1800, node_color=[colores_nodos_todos.get(node, 'grey') for node in lineaC.nodes()], font_size=7, font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        nx.draw(lineaD, pos4, with_labels=True, labels=nx.get_node_attributes(lineaD, 'label'), node_size=1800, node_color=[colores_nodos_todos.get(node, 'grey') for node in lineaD.nodes()], font_size=7, font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
        plt.show()

    
    # nx.draw(lineaA, pos1,  with_labels=True, labels=nx.get_node_attributes(lineaA, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
    # nx.draw(lineaB, pos2,  with_labels=True, labels=nx.get_node_attributes(lineaB, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey',)
    # nx.draw(lineaC, pos3,  with_labels=True, labels=nx.get_node_attributes(lineaC, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
    # nx.draw(lineaD, pos4,  with_labels=True, labels=nx.get_node_attributes(lineaD, 'label'), node_size=1500, node_color='grey', font_size=7,font_weight='bold', font_family='sans-serif', font_color='black', edge_color='grey')
    
# def posicionar(g):
#     pos = cg.coordenadas()
#     return pos