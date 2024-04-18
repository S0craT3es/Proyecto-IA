import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
# Crear un grafo dirigido
G = nx.Graph()

# Agregar nodos
nodos = ["Tijuana", "Rosarito", "Ensenada", "San Quintin", "Guerrero Negro", "Tecate", "Mexicali", "San Felipe"]
for nodo in nodos:
    G.add_node(nodo)

# Agregar aristas con peso
aristas = [
    ("Tijuana", "Rosarito", 20), ("Tijuana", "Tecate", 52), ("Rosarito", "Ensenada", 85),
    ("Ensenada", "Tecate", 100), ("Tecate", "Mexicali", 135), ("Mexicali", "San Felipe", 197),
    ("Ensenada", "San Felipe", 246), ("Ensenada", "San Quintin", 185), ("San Quintin", "Guerrero Negro", 425),
    ("Guerrero Negro", "San Felipe", 394)
]
for origen, destino, peso in aristas:
    G.add_edge(origen, destino, weight=peso)

# Usar Kamada-Kawai layout para una mejor distribución inicial
pos = nx.kamada_kawai_layout(G)

# Dibujar el grafo
plt.figure(figsize=(12, 8))  # Aumentar el tamaño de la figura
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_color='darkred')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='green')
plt.title("Visualización del Grafo de Ciudades")
plt.show()
