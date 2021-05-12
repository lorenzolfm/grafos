import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path, isDirected = False)
    print(graph.hopcroft_karp())
except FileNotFoundError:
    print("Nao achei esse arquivo")
