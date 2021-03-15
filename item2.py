import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    index = int(sys.argv[2])
    graph = Graph(path)
    graph.level_list(graph.getNode(index))
except FileNotFoundError:
    print("Não achei esse arquivo")
