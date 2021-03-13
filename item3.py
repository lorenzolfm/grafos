from utils.Graph import Graph

graph = Graph('./assets/exemploEuler.net')
r, cycle = graph.eulerian()

if r:
    print(1)
    print(cycle)
else:
    print(0)
