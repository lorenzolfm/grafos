import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path)
    r, cycle = graph.eulerian()
    if r:
        print(1)
        print(*cycle, sep = ",")
    else:
        print(0)
except FileNotFoundError:
    print("Não achei esse arquivo")
