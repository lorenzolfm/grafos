import os
from utils.Graph import Graph
from width_search import width_search

# grafo = Graph('./assets/fln_pequena.net')
# print()
grafo = Graph('./assets/agm_tiny.net')
grafo.printGraph()
print()
print(f"Qtd de vertices: {grafo.qtdVertices()}")
print(f"Qtd de arestas: {grafo.qtdArestas()}")
print(f"Grau do vertice 1: {grafo.grau(1)}")
print(f"Grau do vertice 2: {grafo.grau(2)}")
print(f"Rotulo do vertice 1: {grafo.rotulo(1)}")
print(f"Vizinhos do vertice 1: {grafo.vizinhos(1)}")
print(f"Há aresta entre 1 e 2? {grafo.haAresta(1, 2)}")
print(f"Há aresta entre 1 e 5? {grafo.haAresta(1, 5)}")
print(f"Qual o peso de 1 e 3? {grafo.peso(1, 3)}")
print(f"Qual o peso de 1 e 5? {grafo.peso(1, 5)}")

print()

grafo = Graph('./assets/fln_pequena.net')
print(f"Qtd de vertices: {grafo.qtdVertices()}")
print(f"Qtd de arestas: {grafo.qtdArestas()}")
print(f"Grau do vertice 1: {grafo.grau(1)}")
print(f"Grau do vertice 2: {grafo.grau(2)}")
print(f"Rotulo do vertice 1: {grafo.rotulo(1)}")
print(f"Vizinhos do vertice 1: {grafo.vizinhos(1)}")
print(f"Há aresta entre 1 e 2? {grafo.haAresta(1, 2)}")
print(f"Há aresta entre 1 e 5? {grafo.haAresta(1, 5)}")
print(f"Qual o peso de 1 e 3? {grafo.peso(1, 3)}")
print(f"Qual o peso de 1 e 5? {grafo.peso(1, 5)}")

width_search(grafo, 1)
