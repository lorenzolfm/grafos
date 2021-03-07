import os

"""
Grafo não-dirigido e ponderado.

G = (V, E, w)

V -> Conjunto de vértices;
E -> Conjunto de arestas;
w -> Função que mapeia o peso de cada aresta {u, v} e E.
"""
class Grafo:
    """
    Construtor

    Parameter: arquivo (.net), como especificado pelo professor.
    """
    def __init__(self, arquivo):
        self.vertices, self.arestas = self._lerArquivo(arquivo)

    """
    Quantidade de Vértices

    Return: Quantidade de vértices do grafo (inteiro).
    """
    def qtdVertices(self):
        return len(self.vertices)

    """
    Quantidade de Arestas


    Return: Quantidade de arestas (inteiro).
    """
    def qtdArestas(self):
        return len(self.arestas)

    """
    Grau do vértice

    Parameter: vertice (dict).
    Return: Grau do vértice passado como argumento.
    """
    def grauVertice(self, vertice):
        pass

    """
    Rótulo

    Parameter: vertice (dict).
    Return: Rótulo do vértice passado como argumento (TIPO?).
    """
    def rotulo(self, vertice):
        pass

    """
    Vizinhos

    Parameter: vertice (dict).
    Return: Retorna os vizinhos do vértice passado como argumento (List(?))
    """
    def vizinhos(self, vertice):
        pass

    """
    Há Aresta?

    Parameter: u, vértice.
    Parameter: v, vértice.
    Return: True se há aresta ligando u e v, False caso contrário (bool).
    """
    def haAresta(self, u, v):
        pass

    """
    Peso

    Parameter: u, vértice.
    Parameter: v, vértice.
    Return: peso da aresta que liga u e v (float).
    """
    def peso(self, u, v):
        pass

    """
    Ler Arquivo

    Lê arquivo e retorna duas listas:
    * vertices
    * arestas

    Parameter: arquivo (.net)
    Return: vertices, arestas
    """
    def _lerArquivo(self, arquivo):
        with open(arquivo) as file:
            vertices = []

            data = file.read()
            data = data.splitlines()

            numVertices = int(data[0].split()[1])
            data = data[1::]

            for i in range(numVertices):
                vertices.append(
                    self._addVertice(data[i])
                )

            data = data[numVertices::]
            data = data[1::]

            arestas = []

            for aresta in data:
                arestas.append(
                    self._addAresta(aresta)
                )

            return vertices, arestas

    """
    Adiciona Vértice

    Parameter: Vértice no formato "ID ROTULO" (str).
    Return: Dicionário com as chaves id e rótulo (dict).
    """
    def _addVertice(self, verticeString):
        vertice = verticeString.split()
        return {"id": int(vertice[0]), "rotulo": vertice[1]}

    """
    Adiciona Aresta

    Parameter: Aresta no formato "u v w" (vértice, vértice e peso) (str).
    """
    def _addAresta(self, arestaString):
        aresta = arestaString.split()
        return {"aresta": (int(aresta[0]), int(aresta[1])), "peso": float(aresta[2])}

grafo = Grafo('./fln_pequena.net')
