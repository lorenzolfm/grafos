from utils.Graph import Graph

graph = Graph('./assets/agm_tiny.net')
graph.level_list(graph.getNode(1))

print()

graph = Graph('./assets/fln_pequena.net')
graph.level_list(graph.getNode(1))
