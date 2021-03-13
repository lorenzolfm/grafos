from queue import Queue
from utils.Node import Node
from utils.AdjNode import AdjNode
from random import choice

class Graph:
    def __init__(self, file):
        self._numberOfNodes = 0
        self._numberOfEdges = 0

        self._numberOfNodes, rawNodes, rawEdges = self._readFile(file)

        self._nodes = [None] * self._numberOfNodes
        self._edges = []
        self._insertNodes(rawNodes)
        self._insertEdges(rawEdges)

    def qtdVertices(self):
        return self._numberOfNodes

    def qtdArestas(self):
        return self._numberOfEdges

    def getNode(self, v):
        return self._nodes[v - 1]

    def grau(self, v):
        return len(self._nodes[v - 1].getAdjList())

    def rotulo(self, v):
        return self._nodes[v - 1].getData()

    def vizinhos(self, v):
        return self._nodes[v - 1].getAdjList()

    def haAresta(self, u, v):
        source = self._nodes[u - 1]

        for adjacentNode in source.getAdjList():
            if adjacentNode.getId() == v:
                return True

        return False

    def peso(self, u, v):
        if self.haAresta(u, v):
            source = self._nodes[u - 1]
            for adjacentNode in source.getAdjList():
                if adjacentNode.getId() == v:
                    return adjacentNode.getWeight()
        return float('inf')


    def _readFile(self, file):
        with open(file) as f:
            fileData = f.read()
            fileData = fileData.splitlines()

            numberOfNodes = self._getNumberOfNodesFrom(fileData)

            rawNodes = fileData[1:numberOfNodes + 1:]

            rawEdges = fileData[numberOfNodes + 2::]

            return numberOfNodes, rawNodes, rawEdges


    def _insertNodes(self, rawNodes):
        for rawNode in rawNodes:
            rawNode = rawNode.split()

            idd = int(rawNode[0])
            data = rawNode[1::]

            dataWithNotQuotationMarks = []
            for word in data:
                word = word.replace('"', "")
                dataWithNotQuotationMarks.append(word)

            dataString = ' '.join(dataWithNotQuotationMarks)

            node = Node(idd, dataString)

            self._nodes[node.getId() - 1] = node


    def _insertEdges(self, rawEdges):
        for rawEdge in rawEdges:
            rawEdge = rawEdge.split()

            sourceId = int(rawEdge[0])
            destinyId = int(rawEdge[1])
            weight = float(rawEdge[2])

            self.addEdge(sourceId, destinyId, weight)
            self._numberOfEdges += 1


    def addEdge(self, sourceId, destinyId, weight):
        source = self._nodes[sourceId - 1]
        adjNode = AdjNode(destinyId, weight)
        source.addAdjacent(adjNode)

        destiny = self._nodes[destinyId - 1]
        adjNode = AdjNode(sourceId, weight)
        destiny.addAdjacent(adjNode)

        self._edges.append(
            (sourceId, destinyId)
        )


    def breadthFirstSearch(self, vertex):
        # Configurando vetores dos vértices
        known = [False] * self._numberOfNodes
        edge_distance = [float("inf")] * self._numberOfNodes
        ancestral = [None] * self._numberOfNodes

        # Configurando vértice de origem
        vertexId = vertex.getId()
        known[vertexId - 1] = True
        edge_distance[vertexId - 1] = 0

        # Inicializando fila
        queue = Queue(maxsize = self._numberOfNodes)
        queue.put(vertexId)

        # Visitas
        while not queue.empty():
            actual = queue.get()

            adjacent = self.getNode(actual).getAdjList()
            for v in adjacent:
                vId = v.getId()
                if known[vId - 1] == False:
                    known[vId - 1] = True
                    edge_distance[vId - 1] = edge_distance[actual - 1] + 1
                    ancestral[vId - 1] = actual
                    queue.put(vId)

        return edge_distance, ancestral

    def level_list(self, vertex):
        edge_distance, _ = self.breadthFirstSearch(vertex)
        level_list = []
        size = max(edge_distance) + 1

        for i in range(size):
            level_list.append([])

        for i in range(len(edge_distance)):
            level_list[edge_distance[i]].append(i + 1)

        for i in range(size):
            print(f"{i}: {level_list[i]}")

    def eulerian(self):
        # Marcar todas as arestas como desconhecidas
        knownEdges = {}
        for edge in self._edges:
            knownEdges[edge] = False

        # Selecionar um vértice arbritariamente
        while True:
            vertex = choice(self._nodes)
            # O vértice escolhido deve estar conectado a uma aresta
            if vertex.getAdjList():
                break

        # Buscar Subciclo Euleriano
        r, cycle = self.subcycle_search(vertex, knownEdges)


        r = False
        # print(knownEdges)
        if not r:
            # Não existe ciclo euleriano
            return (False, None)
        else:
            # Talvez de ruim v
            if knownEdges.count(False):
                # Há arestas que não foram visitadas
                return (False, None)
            else:
                return (True, cycle)

    def subcycle_search(self, vertex, knownEdges):
        # Vamos tentar encontrar um ciclo
        # print(knownEdges)
        # print(vertex.getId())
        cycle = [vertex]
        initial_vertex = vertex

        # Enquanto initial_vertex != vertex
        while True:
            # Filtrando o dicionario para as arestas desse vértice
            unknowEdgesOfVertex = dict(filter(
                lambda dictItem : (dictItem[0][0] == vertex.getId() or dictItem[0][1] == vertex.getId()) and dictItem[1] == False,
                knownEdges.items()
            ))

            # Não há arestas não visitadas adjacentes a vertex
            if self._areAllEdgesVisited(unknowEdgesOfVertex):
                # print("entrei")
                return (False, None)
            else:
                # Selecionar uma aresta de vertex que ainda não foi marcada como conhecida.
                edge, _ = choice(list(unknowEdgesOfVertex.items()))
                # print(vertex.getId())
                # print(edge)

                # Marcar como conhecida {u, v} = True
                knownEdges[edge] = True

                # Andar pela aresta
                if vertex.getId() == edge[0]:
                    vertex = self.getNode(edge[1])
                else:
                    vertex = self.getNode(edge[0])

                # print(f"Novo vértice: {vertex.getId()}")
                # Adiciona vertex ao final do ciclo
                cycle.append(vertex)

            if initial_vertex == vertex:
                break

        # Fechei um subciclo!
        # Preciso verificar se para o subciclo que eu achei, há algum vértice que possue arestas não marcadas
        # print()
        # print(knownEdges)
        # print()
        # print(cycle)

        # Para cada vértice
        for vertex in cycle:
            unknowEdgesOfVertex = dict(filter(
                lambda dictItem : (dictItem[0][0] == vertex.getId() or dictItem[0][1] == vertex.getId()) and dictItem[1] == False,
                knownEdges.items()
            ))
            # print(unknowEdgesOfVertex)

            # Que tem pelo menos uma aresta não marcada.
            if unknowEdgesOfVertex:
                r, OtherCycle = self.subcycle_search(vertex, knownEdges)
                if not r:
                    print("Não rola ciclo euleriano")
                    return (False, None)

                print(cycle)
                print(otherCycle)



        return(True, cycle)

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])


    def printGraph(self):
        for node in self._nodes:
            print(f"Vertice {node.getId()}: {node.getAdjList()}")

    def _areAllEdgesVisited(self, unknowEdgesOfVertex):
        # Se todas as arestas desse vértice forem conhecidas, retorne true
        if all(unknowEdgesOfVertex.values()):
            return True

        return False
