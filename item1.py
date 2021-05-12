import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path, isDirected = True)
    # Chamada da função
except FileNotFoundError:
    print("Não achei esse arquivo")
