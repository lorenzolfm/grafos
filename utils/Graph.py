from queue import Queue
from utils.Node import Node
from utils.AdjNode import AdjNode
from random import randint

class Graph:
    def __init__(self, file):
        self._numberOfNodes = 0
        self._numberOfEdges = 0

        self._numberOfNodes, rawNodes, rawEdges = self._readFile(file)

        self._nodes = [None] * self._numberOfNodes
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
        knowm = [False] * self.qtdArestas()
        vertex = randint(0, self.qtdVertices() - 1)

        r, cycle = subcycle_search(vertex, known)

        if not r:
            return (False, None)
        elif cycle.count(False):
            return (False, None)
        else:
            return (True, cycle)

    def subcycle_search(self, vertex, known):
        cycle = [vertex]
        initial = vertex
        pass

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])


    def printGraph(self):
        for node in self._nodes:
            print(f"Vertice {node.getId()}: {node.getAdjList()}")
