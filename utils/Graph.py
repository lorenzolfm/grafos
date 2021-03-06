from copy import deepcopy
from queue import Queue
from utils.Node import Node
from utils.AdjNode import AdjNode
from random import choice


class Graph:
    def __init__(self, file, isDirected):
        self._numberOfNodes = 0
        self._numberOfEdges = 0
        self.isDirected = isDirected
        self._numberOfNodes, rawNodes, rawEdges = self._readFile(file)
        self._nodes = [None] * self._numberOfNodes
        self._edges = []
        self._insertNodes(rawNodes)
        self._insertEdges(rawEdges)

    def qtdVertices(self):
        return self._numberOfNodes

    def qtdArestas(self):
        return self._numberOfEdges

    def getNode(self, v):
        return self._nodes[v - 1]

    def grau(self, v):
        return len(self._nodes[v - 1].getAdjList())

    def rotulo(self, v):
        return self._nodes[v - 1].getData()

    def vizinhos(self, v):
        return self._nodes[v - 1].getAdjList()

    def haAresta(self, u, v):
        source = self._nodes[u - 1]

        for adjacentNode in source.getAdjList():
            if adjacentNode.getId() == v:
                return True

        return False

    def peso(self, u, v):
        if self.haAresta(u, v):
            source = self._nodes[u - 1]
            for adjacentNode in source.getAdjList():
                if adjacentNode.getId() == v:
                    return adjacentNode.getWeight()
        return float('inf')


    def _readFile(self, file):
        with open(file) as f:
            fileData = f.read()
            fileData = fileData.splitlines()

            numberOfNodes = self._getNumberOfNodesFrom(fileData)

            rawNodes = fileData[1:numberOfNodes + 1:]

            rawEdges = fileData[numberOfNodes + 2::]

            return numberOfNodes, rawNodes, rawEdges


    def _insertNodes(self, rawNodes):
        for rawNode in rawNodes:
            rawNode = rawNode.split()

            idd = int(rawNode[0])
            data = rawNode[1::]

            dataWithNotQuotationMarks = []
            for word in data:
                word = word.replace('"', "")
                dataWithNotQuotationMarks.append(word)

            dataString = ' '.join(dataWithNotQuotationMarks)

            node = Node(idd, dataString)

            self._nodes[node.getId() - 1] = node

    def _insertEdges(self, rawEdges):
        for rawEdge in rawEdges:
            rawEdge = rawEdge.split()

            sourceId = int(rawEdge[0])
            destinyId = int(rawEdge[1])
            weight = float(rawEdge[2])

            self.addEdge(sourceId, destinyId, weight)
            self._numberOfEdges += 1

    def addEdge(self, sourceId, destinyId, weight):
        source = self._nodes[sourceId - 1]
        adjNode = AdjNode(destinyId, weight)
        source.addAdjacent(adjNode)

        if not(self.isDirected):
            destiny = self._nodes[destinyId - 1]
            adjNode = AdjNode(sourceId, weight)
            destiny.addAdjacent(adjNode)

        self._edges.append(
            (sourceId, destinyId, weight)
        )

    def breadthFirstSearch(self, vertex):
        # Configurando vetores dos v??rtices
        known = [False] * self._numberOfNodes
        edge_distance = [float("inf")] * self._numberOfNodes
        ancestral = [None] * self._numberOfNodes

        # Configurando v??rtice de origem
        vertexId = vertex.getId()
        known[vertexId - 1] = True
        edge_distance[vertexId - 1] = 0

        # Inicializando fila
        queue = Queue(maxsize = self._numberOfNodes)
        queue.put(vertexId)

        # Visitas
        while not queue.empty():
            actual = queue.get()

            adjacent = self.getNode(actual).getAdjList()
            for v in adjacent:
                vId = v.getId()
                if known[vId - 1] == False:
                    known[vId - 1] = True
                    edge_distance[vId - 1] = edge_distance[actual - 1] + 1
                    ancestral[vId - 1] = actual
                    queue.put(vId)

        return edge_distance, ancestral

    def level_list(self, vertex):
        edge_distance, _ = self.breadthFirstSearch(vertex)
        level_list = []
        size = max(edge_distance) + 1

        for i in range(size):
            level_list.append([])

        for i in range(len(edge_distance)):
            level_list[edge_distance[i]].append(i + 1)

        for i in range(size):
            string = str(level_list[i])[1:-1].replace(" ", "")
            print(f"{i}: {string}")

    def eulerian(self):
        # Marcar todas as arestas como desconhecidas
        knownEdges = {}
        for edge in self._edges:
            knownEdges[edge] = False

        # Selecionar um v??rtice arbritariamente
        while True:
            vertex = choice(self._nodes)
            # O v??rtice escolhido deve estar conectado a uma aresta
            if vertex.getAdjList():
                break

        # Buscar Subciclo Euleriano
        r, cycle = self.subcycle_search(vertex, knownEdges)

        if r == False:
            # N??o existe ciclo euleriano
            return False, None
        else:
            if list(knownEdges.values()).count(False):
                # H?? arestas que n??o foram visitadas
                return False, None
            else:
                return True, cycle

    def subcycle_search(self, vertex, knownEdges):
        # Vamos tentar encontrar um ciclo
        cycle = [vertex]
        initial_vertex = vertex

        # Enquanto initial_vertex != vertex
        while True:
            # Filtrando o dicionario para as arestas desse v??rtice
            unknowEdgesOfVertex = dict(filter(
                lambda dictItem : (dictItem[0][0] == vertex.getId() or dictItem[0][1] == vertex.getId()) and dictItem[1] == False,
                knownEdges.items()
            ))

            # N??o h?? arestas n??o visitadas adjacentes a vertex
            if not(unknowEdgesOfVertex):
                return False, None
            else:
                # Selecionar uma aresta de vertex que ainda n??o foi marcada como conhecida.
                edge, _ = choice(list(unknowEdgesOfVertex.items()))

                # Marcar como conhecida {u, v} = True
                knownEdges[edge] = True

                # Andar pela aresta
                if vertex.getId() == edge[0]:
                    vertex = self.getNode(edge[1])
                else:
                    vertex = self.getNode(edge[0])

                # Adiciona vertex ao final do ciclo
                cycle.append(vertex)

            if initial_vertex == vertex:
                break

        # Fechei um subciclo!
        # Preciso verificar se para o subciclo que eu achei, h?? algum v??rtice que possue arestas n??o marcadas

        # Para cada v??rtice que tem pelo menos uma aresta n??o marcada:
        for vertex in cycle:
            unknowEdgesOfVertex = dict(filter(
                lambda dictItem : (dictItem[0][0] == vertex.getId() or dictItem[0][1] == vertex.getId()) and dictItem[1] == False,
                knownEdges.items()
            ))

            # Que tem pelo menos uma aresta n??o marcada.
            if unknowEdgesOfVertex:
                r, otherCycle = self.subcycle_search(vertex, knownEdges)

                if r == False:
                    return False, None

                indexOfVertex = cycle.index(vertex)
                for i in range(len(otherCycle)):
                    cycle.insert(i + indexOfVertex, otherCycle[i])

        return True, cycle

    def bellman_ford(self, vertex):
        # Inicializa????o

        # Custo encontrado de vertex p/ todos os outros
        distance = [float("inf")] * self._numberOfNodes
        ancestral = [None] * self._numberOfNodes
        distance[vertex.getId() - 1] = 0

        # Caminho m??nimo
        for _ in range(self._numberOfNodes - 1):
            for u, v, w in self._edges:
                if distance[u - 1] != float("inf") and distance[u - 1] + w < distance[v - 1]:
                    distance[v - 1] = distance[u - 1] + w
                    ancestral[v - 1] = u
                elif distance[v - 1] != float("inf") and distance[v - 1] + w < distance[u - 1]:
                    distance[u - 1] = distance[v - 1] + w
                    ancestral[u - 1] = v

        # Detectar se h?? ciclo negativo
        for u, v, w in self._edges:
            if distance[u - 1] != float("inf") and distance[u - 1] + w < distance[v - 1]:
                return (False, None, None)
            elif distance[v - 1] != float("inf") and distance[v - 1] + w < distance[u - 1]:
                return (False, None, None)

        return (True, distance, ancestral)

    def print_bellman_ford(self, vertex):
        flag, distance, ancestral = self.bellman_ford(vertex)

        if flag == False:
            print("H?? ciclo negativo")
            return

        for i in range(self._numberOfNodes):
            aux = i + 1
            way = [aux]
            while aux != None:
                aux = ancestral[aux - 1]
                if aux == None:
                    pass
                else:
                    way.insert(0, aux)
                    string = str(way)[1:-1].replace(" ", "")

            print(f"{i+1}: {string}; d={distance[i]}")

    def floyd_warshall(self):
        matrix = []
        edgesWithoutWeight = [(edge[0], edge[1]) for edge in self._edges]

        matrix = [[None for x in range(self._numberOfNodes)] for y in range(self._numberOfNodes)]

        for i in range(self._numberOfNodes):
            for j in range(i, self._numberOfNodes):
                if i == j:
                    matrix[i][j] = 0
                else:
                    u = i + 1
                    v = j + 1
                    edge = (u, v)
                    if edge in edgesWithoutWeight:
                        index = edgesWithoutWeight.index(edge)
                        matrix[i][j] = self._edges[index][2]
                        matrix[j][i] = self._edges[index][2]
                    else:
                        matrix[i][j] = float('inf')
                        matrix[j][i] = float('inf')

        for k in range(self._numberOfNodes):
            for u in range(self._numberOfNodes):
                for v in range(self._numberOfNodes):
                    matrix[u][v] = min(matrix[u][v], matrix[u][k] + matrix[k][v])

        return matrix

    def print_floyd_warshall(self):
        matrix = self.floyd_warshall()
        for i in range(len(matrix)):
            string = str(matrix[i])[1:-1].replace(" ", "")
            print(f"{i + 1}:{string}")

    def _getNumberOfNodesFrom(self, fileData):
        return int(fileData[0].split()[1])


    def printGraph(self):
        for node in self._nodes:
            print(f"Vertice {node.getId()}: {node.getAdjList()}")


    def _areAllEdgesVisited(self, unknowEdgesOfVertex):
        # Se todas as arestas desse v??rtice forem conhecidas, retorne true
        if all(list(unknowEdgesOfVertex.values())):
            return True

        return False



    def topological_ordering(self):
        # Cv
        known = [False] * self._numberOfNodes
        # Tv
        beginTime = [float('inf')] * self._numberOfNodes
        # Fv
        endTime = [float('inf')] * self._numberOfNodes

        # Configurando tempo de in??cio
        time = 0

        # Criando lista com os v??rtices ordenados topologicamente
        topologicalOrder = []

        for node in self._nodes:
            if not(known[node.getId() -1]):
                self.dfsVisitOT(node, known, beginTime, endTime, time, topologicalOrder)

        return topologicalOrder

    def dfsVisitOT(self, vertex, knowNodes, beginTime, endTime, time, topologicalOrder):
        knowNodes[vertex.getId()-1] = True

        time += 1

        beginTime[vertex.getId()-1] = time

        for i in vertex.getAdjList():
            if not knowNodes[i.getId()-1]:
                self.dfsVisitOT(self._nodes[i.getId()-1], knowNodes, beginTime, endTime, time, topologicalOrder)

        time += 1
        endTime[vertex.getId()-1] = time
        topologicalOrder.insert(0, vertex.getData())

    def print_ordering(self):
        print(*self.topological_ordering(), sep=" -> ")


    def stronglyConnectedComponents(self,):
        known, beginTime, ancestral, endTime = self.dfs(self._nodes)

        transposedGraph = deepcopy(self)
        transposedGraph._edges = self.invertArchs()
        for vertex in transposedGraph._nodes:
            vertex.getAdjList().clear()

        for edge in transposedGraph._edges:
            source = transposedGraph._nodes[edge[0] - 1]
            destiny = transposedGraph._nodes[edge[1] - 1]
            weight = edge[2]
            adjNode = AdjNode(destiny.getId(), weight)
            source.addAdjacent(adjNode)

        endTimeDict = {}
        for i in range(len(self._nodes)):
            endTimeDict[self._nodes[i]] = endTime[i]

        order = list(dict(sorted(endTimeDict.items(), key=lambda item: item[1], reverse = True)).keys())

        Ct, Tt, At, Ft = transposedGraph.dfs(order)

        return At


    def dfs(self, order):
        known = [False] * self._numberOfNodes
        beginTime = [float('inf')] * self._numberOfNodes
        endTime = [float('inf')] * self._numberOfNodes
        ancestral = [None] * self._numberOfNodes

        time = 0

        for i in order:
            if not known[i.getId() - 1]:
                time = self.dfsVisit(self._nodes[i.getId() - 1], known, beginTime, ancestral, endTime, time)

        return known, beginTime, ancestral, endTime


    def dfsVisit(self, vertex, known, beginTime, ancestral, endTime, time):
        known[vertex.getId() - 1] = True
        time += 1
        beginTime[vertex.getId() - 1] = time


        for i in vertex.getAdjList():
            if not known[i.getId()-1]:
                ancestral[i.getId() - 1] = vertex
                time = self.dfsVisit(self._nodes[i.getId() - 1], known, beginTime, ancestral, endTime, time)

        time += 1
        endTime[vertex.getId() - 1] = time

        return time

    def invertArchs(self):
        invertedArchs = [(y, x, z) for (x, y, z) in self._edges]
        return invertedArchs

    def printCFC(self):
        At = self.stronglyConnectedComponents()

        output = [[i + 1] for i in range(len(At)) if At[i] == None]

        for i in range(len(At)):
            if At[i] != None:
                aux = At[i]
                while At[aux.getId() - 1] != None:
                    aux = At[aux.getId() - 1]

                for lista in output:
                    if aux.getId() in lista:
                        lista.append(i + 1)

        for lista in output:
            print(*lista, sep=",")

    def kruskal(self):
        tree = []
        tree_map = [[vertex.getId()] for vertex in self._nodes]
        crescent_edges = sorted(self._edges, key=lambda x: x[2])
        for edge in crescent_edges:
            if tree_map[edge[0]-1] != tree_map[edge[1]-1]:
                tree.append(edge)
                x = tree_map[edge[0]-1] + tree_map[edge[1]-1]

            for y in x:
                tree_map[y-1] = x

        return tree

    def print_kruskal(self):
        tree = self.kruskal()
        cust = 0
        test = []
        for x in tree:
            cust += x[2]
            test.append(f"{x[0]}-{x[1]}")

        print(cust)
        print(*test, sep=", ")

    """
    Cria um programa que receba um grafo dirigido e ponderado como argumento.
    Ao final, imprima na tela o valor do fluxo m??ximo resultante da execu????o do algoritmo de Edmonds-Karp
    """
    def edmonds_karp(self, s, t, fuv):
        # Configurando todos os v??rtices
        C = {vertex: False for vertex in self._nodes}
        A = {vertex: None for vertex in self._nodes}

        # Configurando v??rtice de origem
        C[s] = True

        Q = Queue()

        # Iniciar busca pela fonte
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in u.getAdjList():
                v = self._nodes[v.getId() - 1]
                flow = self.peso(u.getId(), v.getId()) - fuv[(u.getId(), v.getId())]
                if (not C[v]) and (flow > 0):
                    C[v] = True
                    A[v] = u
                    # Sorvedouro encontrado. Criar caminho aumentante.
                    if v == t:
                        p = [t]
                        w = t
                        while w != s:
                           w = A[w]
                           p.insert(0, w)
                        return p
                    Q.put(v)

        return None

    def ford_fulkerson(self):
        s = self._nodes[0]
        t = self._nodes[-1]
        fuv = {(edge[0], edge[1]): 0 for edge in self._edges}
        p = self.edmonds_karp(s, t, fuv)
        max_flow = 0

        while p:
            cost = []
            arestas = []
            for i in range(len(p) - 1):
                arestas.append([p[i].getId(), p[i+1].getId()])
                peso = self.peso(p[i].getId(), p[i+1].getId())
                cost.append(peso)

            cfp = min(cost)
            max_flow += cfp

            for u, v in arestas:
                if self.haAresta(u, v):
                    fuv[(u, v)] += cfp
                else:
                    fuv[(v, u)] -= cfp

            p = self.edmonds_karp(s, t, fuv)

        print(max_flow)
        return max_flow

    def hopcroft_karp(self):
        null = Node(len(self._nodes) + 1, None)
        D = [float('inf') for _ in self._nodes]
        D.append(float("inf"))
        mate = [null for _ in self._nodes]

        m = 0
        X, _ = self.split_graph()

        while self.BFS(mate, D, null, X):
            for x in X:
                if mate[x.getId() - 1] == null:
                    if self.DFS(mate, x, D, null):
                        m += 1

        return (m, mate)

    def BFS(self, mate, D, null, X):
        Q = Queue()
        for x in X:
            if mate[x.getId() - 1] == null:
                D[x.getId() - 1] = 0
                Q.put(x)
            else:
                D[x.getId() - 1] = float('inf')

        D[-1] = float("inf")
        while not Q.empty():
            x = Q.get()
            if D[x.getId() - 1] < D[-1]:
                for y in x.getAdjList():
                    y = self._nodes[y.getId() - 1]
                    nova = mate[y.getId() - 1]
                    if D[nova.getId() - 1] == float('inf'):
                        D[nova.getId() - 1] = D[x.getId() - 1] + 1
                        Q.put(nova)

        return D[-1] != float('inf')

    def DFS(self, mate, x, D, null):
        if x != null:
            for y in x.getAdjList():
                y = self._nodes[y.getId() - 1]
                nova = mate[y.getId() - 1]
                if D[nova.getId() - 1] == D[x.getId() - 1] + 1:
                    if self.DFS(mate, nova, D, null):
                        mate[y.getId() - 1] = x
                        mate[x.getId() - 1] = y
                        return True

            D[x.getId() - 1] = float('inf')
            return False

        return True

    def print_hopcroft_karp(self):
        max_par, edges = self.hopcroft_karp()
        aux = []
        for i in range(len(edges)):
            begin_vertex = self._nodes[i]
            end_vertex = edges[i]
            if [begin_vertex, end_vertex] not in aux and [end_vertex, begin_vertex] not in aux:
                aux.append([begin_vertex, end_vertex])

        print(f"Emparelhamento M??ximo: {max_par} \n"
              f"Arestas: ", end="")
        print(*aux, sep=", ")

    def split_graph(self):
        X = []
        Y = []
        for u, v, _ in self._edges:
            u = self._nodes[u - 1]
            v = self._nodes[v - 1]
            if u not in X and u not in Y:
                X.append(u)
            if v not in X and v not in Y:
                Y.append(v)

        return X, Y
