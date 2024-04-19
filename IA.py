import networkx as nx
import random
import math
import matplotlib.pyplot as plt
import scipy as sp

# Crear el grafo
G = nx.Graph()
nodos = ["Tijuana", "Rosarito", "Ensenada", "San Quintin", "Guerrero Negro", "Tecate", "Mexicali", "San Felipe"]
aristas = [
    ("Tijuana", "Rosarito", 20), ("Tijuana", "Tecate", 52), ("Rosarito", "Ensenada", 85),
    ("Ensenada", "Tecate", 100), ("Tecate", "Mexicali", 135), ("Mexicali", "San Felipe", 197),
    ("Ensenada", "San Felipe", 246), ("Ensenada", "San Quintin", 185), ("San Quintin", "Guerrero Negro", 425),
    ("Guerrero Negro", "San Felipe", 394)
]
for origen, destino, peso in aristas:
    G.add_edge(origen, destino, weight=peso)

def calculate_cost(path):
    """ Calcula el costo total de un camino dado """
    cost = 0
    for i in range(len(path) - 1):
        if path[i+1] in G[path[i]]:
            cost += G[path[i]][path[i+1]]['weight']
        else:
            cost += float('inf')  # Si el camino no es válido (no conectado directamente), penaliza severamente
    return cost

def modify_solution(path):
    """ Modifica la solución actual para explorar nuevas soluciones """
    if len(path) <= 3:
        return path
    mid_point = len(path) // 2
    start = 0
    end = len(path) - 1
    # Intercambiar segmentos en el camino
    new_path = path[:mid_point]
    random.shuffle(new_path)
    new_path.extend(path[mid_point:])
    return new_path

def simulated_annealing(start, goal, initial_temp, cooling_rate, min_temp):
    """ Algoritmo de Simulated Annealing """
    # Generar una solución inicial usando shortest_path (solo para comenzar con un camino válido)
    current_solution = nx.shortest_path(G, source=start, target=goal, weight='weight')
    current_cost = calculate_cost(current_solution)
    temperature = initial_temp
    
    while temperature > min_temp:
        new_solution = modify_solution(current_solution)
        new_cost = calculate_cost(new_solution)
        if new_cost < current_cost or random.uniform(0, 1) < math.exp(-(new_cost - current_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost
        
        temperature *= cooling_rate
    
    return current_solution, current_cost

# Parámetros del algoritmo
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1

# Correr el algoritmo
start_node = 'Tijuana'
goal_node = 'Guerrero Negro'
best_path, best_cost = simulated_annealing(start_node, goal_node, initial_temp, cooling_rate, min_temp)
print(f"Best path: {best_path} with cost: {best_cost}")

# Dibujar el mejor camino encontrado
path_edges = list(zip(best_path, best_path[1:]))
pos = nx.kamada_kawai_layout(G)  # Posiciones de los nodos para visualización
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_color='darkred', edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='green')
plt.title("Camino más corto encontrado usando Simulated Annealing")
plt.show()