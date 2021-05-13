import sys
from utils.Graph import Graph

try:
    path = str(sys.argv[1])
    graph = Graph(path, isDirected = True)
    s = graph.getNode(1)
    t = graph.getNode(6)
    # graph.edmonds_karp(s, t)
    graph.ford_fulkerson(s, t)
except FileNotFoundError:
    print("Nao achei esse arquivo")
