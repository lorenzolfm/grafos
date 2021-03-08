class AdjNode:
    def __init__(self, idd, weight):
        self.idd = idd
        self.weight = weight

    def getId(self):
        return self.idd

    def getWeight(self):
        return self.weight

    def __repr__(self):
        return f"({self.idd}, {self.weight})"
