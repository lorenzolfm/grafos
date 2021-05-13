import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path, isDirected = True)
    graph.ford_fulkerson()
except FileNotFoundError:
    print("Nao achei esse arquivo")
