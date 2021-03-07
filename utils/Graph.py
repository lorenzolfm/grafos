class Graph:
    def __init__(self, file):
        self._readFile(file)
        self.numberOfNodes = 0
        self.nodes = []

    def _readFile(self, file):
        with open(file) as f:
            fileData = f.read()
            fileData = fileData.splitlines()

            print(fileData)
