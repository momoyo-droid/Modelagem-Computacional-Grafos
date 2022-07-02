import math


# estrutura auxiliar para guardar o menor caminho
class HeapMin():

    def __init__(self) -> None:
        self.nodes = 0  # quantidade de vertices
        self.heap = []  # estrutura heap

    def add_node(self, weight, vertice) -> None:
        self.heap.append([weight, vertice])  # relacao entre peso e vertice
        self.nodes += 1

        child = self.nodes

        while True:
            if child == 1:
                break
            father = child // 2
            if self.heap[father - 1][0] <= self.heap[child - 1][0]:
                break
            else:
                self.heap[father -
                          1], self.heap[child -
                                        1] = self.heap[child -
                                                       1], self.heap[father -
                                                                     1]
                child = father

    # remove no e retorna o menor valor/vertice correspondente a distancia/peso
    def pop_node(self) -> int:
        node = self.heap[0]
        self.heap[0] = self.heap[self.nodes - 1]
        self.heap.pop()

        self.nodes -= 1

        father = 1

        while True:
            child = 2 * father
            if child > self.nodes:
                break
            if child + 1 <= self.nodes:
                if self.heap[child][0] < self.heap[child - 1][0]:
                    child += 1
            if self.heap[father - 1][0] <= self.heap[child - 1][0]:
                break
            else:
                self.heap[father -
                          1], self.heap[child -
                                        1] = self.heap[child -
                                                       1], self.heap[father -
                                                                     1]
                father = child
        return node

    def size_heap(self) -> int:
        return self.nodes


class Graph():

    def __init__(self, n_vertices) -> None:
        self.n_v = n_vertices  # quantidade de vertices
        self.graph = [[0] * self.n_v
                      for i in range(self.n_v)]  # matriz de distancias/peso

    def add_edge(self, edge, FLAG) -> None:
        if FLAG == 0:  # grafo nao direcionado
            u = int(edge.split()[0])
            v = int(edge.split()[1])
            weight = int(edge.split()[2])
            self.graph[u - 1][v - 1] = weight
            self.graph[v - 1][u - 1] = weight
        else:  # grafo direcionado
            u = int(edge.split()[0])
            v = int(edge.split()[1])
            weight = int(edge.split()[2])
            self.graph[u - 1][v - 1] = weight

    def display_matrix(self) -> None:
        print("Matriz de adjacencia:")
        for i in range(self.n_v):
            print(self.graph[i])

    def dijkstra(self, start_v) -> list:
        cost = [[float("inf"), 0] for i in range(self.n_v)]
        cost[start_v - 1] = [0, start_v]

        H = HeapMin()

        H.add_node(0, start_v)

        while H.size_heap() > 0:
            dist, vertice = H.pop_node()
            for i in range(self.n_v):  # calculo da distancia
                if self.graph[vertice - 1][i] != 0:
                    if cost[i][0] == -1 or cost[i][0] > dist + self.graph[
                            vertice - 1][i]:
                        cost[i] = [dist + self.graph[vertice - 1][i], vertice]
                        H.add_node(dist + self.graph[vertice - 1][i], i + 1)
        return cost


def main() -> None:
    # leitura do arquivo .in
    filename = input()

    # leitura do conteudo do arquivo .pajek
    pajek_file = open(filename, 'r')
    content_pf = pajek_file.readlines()

    # armazena quantidade de vertices
    n_vertices = int(content_pf[0].split()[1])

    # verifica se grafo é direcionado ou nao direcionado
    graph_type = content_pf[1]
    FLAG = 0  # nao direcionado
    if graph_type[1] == "A":
        FLAG = 1  # direcionado

    # construcao do grafo
    G = Graph(n_vertices)

    for i in range(2, len(content_pf)):
        G.add_edge(content_pf[i], FLAG)
    # impressao da matriz de distancias
    for i in range(1, n_vertices + 1):
        for j in range(n_vertices):
            print(G.dijkstra(i)[j][0], end=" ")
        print()


if __name__ == "__main__":
    main()
