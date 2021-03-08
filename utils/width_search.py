from queue import Queue

def width_search(graph, vertice):
    # configurando vetores dos vértcies    
    known = [False] * graph.qtdVertices()
    edge_distance = [float("inf")] * graph.qtdVertices()
    ancestral = [None] * graph.qtdVertices()

    # configurando vértice de origem
    known[vertice - 1] = True
    edge_distance[vertice - 1] = 0
    
    # inicializando fila
    queue = Queue(maxsize = graph.qtdVertices())
    queue.put(vertice)
    
    # visitas
    level = 0
    print(f"{level}: {vertice}")
    while not queue.empty():
        actual = queue.get()
        
        adjacent = actual.getAdjList()
        level_list = []
        for v in adjacent:
            if known[v - 1] == False:
                known[v - 1] = True
                edge_distance[v - 1] = edge_distance[actual - 1] + 1
                ancestral[v - 1] = actual
                queue.put(v)
                level_list.append(v)        

        level += 1
        print(f"{level}: {level_list}")

    #return (edge_distance, ancestral)
