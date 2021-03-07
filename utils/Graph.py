class Graph:
    def __init__(self, file):
        self._numberOfNodes = 0
        self._numberOfEdges = 0
        self._nodes = []

        self._readFile(file)

    def getNumberOfNodes(self):
        return self._numberOfNodes

    def _readFile(self, file):
        with open(file) as f:
            fileData = f.read()
            fileData = fileData.splitlines()

            self._numberOfNodes = self._getNumberOfNodesFrom(fileData)

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])
