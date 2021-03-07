class Node:
    def __init__(self, idd, data):
        self.idd = idd
        self.data = data
        self.next = None

    def getId(self):
        return self.idd

    def getData(self):
        return self.data

    def setNext(self, adjNode):
        self.next = adjNode
