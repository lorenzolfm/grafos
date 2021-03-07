from utils.Node import Node
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
            print(f"Adicionando vértice {node.getId()} na posição {node.getId() - 1} da lista")

    def _insertEdges(self, rawEdges):
        pass

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])
