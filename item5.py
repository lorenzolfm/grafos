import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path)
    graph.print_floyd_warshall()
except FileNotFoundError:
    print("Não achei esse arquivo")
