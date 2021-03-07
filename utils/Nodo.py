class EdgeNode:
    def __init__(self, y, weight, edgeNode):
        self.y = y
        self.weight = weight
        self.edgeNode = edgeNode

    def getDegree(self):
        return len(listOfAdjacents)

class Vertice:
    def __init__(self, idd, label, degree):
        self.idd = idd
        self.label = label
        self.degree = 0
