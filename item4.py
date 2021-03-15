import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path)
    vertex = graph.getNode(int(sys.argv[2]))
    graph.print_bellman_ford(vertex)
except FileNotFoundError:
    print("Não achei esse arquivo")
