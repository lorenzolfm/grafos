from queue import Queue

def width_search(graph, vertice):
    # configurando vetores dos vértcies    
    known = [False] * graph.qtdVertices()
    edge_distance = [float("inf")] * graph.qtdVertices()
    ancestral = [None] * graph.qtdVertices()

    # configurando vértice de origem
    known[vertice.idd - 1] = True
    edge_distance[vertice.idd - 1] = 0
    
    # inicializando fila
    queue = Queue(maxsize = graph.qtdVertices())
    queue.put(vertice.idd)
    
    # visitas
    #level = 0
    #print(f"{level}: {vertice.idd}")
    while not queue.empty():
        actual = queue.get()
        
        adjacent = graph.Node(actual).getAdjList()
        #level_list = []
        for v in adjacent:
            if known[v.idd - 1] == False:
                known[v.idd - 1] = True
                edge_distance[v.idd - 1] = edge_distance[actual - 1] + 1
                ancestral[v.idd - 1] = actual
                queue.put(v.idd)
                #level_list.append(v.idd)        

        #level += 1
        #print(f"{level}: {level_list}")

    return (edge_distance, ancestral)


def level_list(grafo, vertice):
    a = width_search(grafo, vertice)
    level_list = []
    size = max(a[0]) + 1
    
    for i in range(size):
        level_list.append([])

    for i in range(len(a[0])):
       level_list[a[0][i]].append(i + 1)

    for i in range(size):
        print(f"{i}: {level_list[i]}")
