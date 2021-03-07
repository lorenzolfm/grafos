from utils.Node import Node
from utils.AdjNode import AdjNode

class Graph:
    def __init__(self, file):
        self._numberOfNodes = 0
        self._numberOfEdges = 0

        self._numberOfNodes, rawNodes, rawEdges = self._readFile(file)

        self._nodes = [None] * self._numberOfNodes
        self._insertNodes(rawNodes)
        self._insertEdges(rawEdges)


    def getNumberOfNodes(self):
        return self._numberOfNodes

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
            data = rawNode[1]
            node = Node(idd, data)

            self._nodes[node.getId() - 1] = node
            # print(f"Adicionando vértice {node.getId()} na posição {node.getId() - 1} da lista")

    def _insertEdges(self, rawEdges):
        for rawEdge in rawEdges:
            rawEdge = rawEdge.split()

            sourceId = int(rawEdge[0])
            destinyId = int(rawEdge[1])
            weight = float(rawEdge[2])

            source = self._nodes[sourceId - 1]
            adjNode = AdjNode(destinyId, weight)
            source.setNext(adjNode)

            destiny = self._nodes[destinyId - 1]
            adjNode = AdjNode(sourceId, weight)
            destiny.setNext(adjNode)

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])
