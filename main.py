import os

"""
Grafo não-dirigido e ponderado
"""
class Grafo:
    def __init__(self, arquivo):
        self.vertices, self.arestas = self._lerArquivo(arquivo)

    """
    Retorna a quantidade de vértices;
    """
    def qtdVertices(self):
        return len(self.vertices)

    """
    Retorna a quantidade de arestas;
    """
    def qtdArestas(self):
        return len(self.arestas)

    """
    Retorna o grau de um vértice
    """
    def grauVertice(self, vertice):
        pass

    def rotulo(self, vertice):
        pass

    def vizinhos(self, vertice):
        pass

    def haAresta(self, u, v):
        pass

    def peso(self, u, v):
        pass

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

    def _addVertice(self, verticeString):
        vertice = verticeString.split()
        return {"id": int(vertice[0]), "rotulo": vertice[1]}

    def _addAresta(self, arestaString):
        aresta = arestaString.split()
        return {"aresta": (int(aresta[0]), int(aresta[1])), "peso": float(aresta[2])}

grafo = Grafo('./fln_pequena.net')
