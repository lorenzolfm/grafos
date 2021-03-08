class Node:
    def __init__(self, idd, data):
        self.idd = idd
        self.data = data
        self.adjacents = []

    def getId(self):
        return self.idd

    def getData(self):
        return self.data

    def addAdjacent(self, adjNode):
        self.adjacents.append(adjNode)

    def getAdjList(self):
        return self.adjacents
