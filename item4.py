from utils.Graph import Graph

graph = Graph('./assets/agm_tiny.net')
# for i in range(1, 7):
    # print(i)
graph.print_bellman_ford(graph.getNode(3))

# graph = Graph('./assets/fln_pequena.net')
# graph.print_bellman_ford(graph.getNode(1))

# graph = Graph('./assets/fln_pequena.net')
# graph.print_bellman_ford(graph.getNode(5))
