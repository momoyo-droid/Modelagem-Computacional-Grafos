'''
Disciplina Modelagem Computacional em Grafos
Projeto 2: Algoritmo de Prim
Ana Cristina Silva de Oliveira - nUSP 11965630
Jefferson Eduardo Muniz Bueno - nUSP 11275255
'''
INF_VALUE = 9999999

class Graph():
    def __init__(self, n_vertex) -> None:
        self.n_vertex = n_vertex
        self.graph = [[0]*self.n_vertex for i in range(self.n_vertex)]

    def addEdges(self, edge) -> None: 
        u = int(edge.split()[0])
        v = int(edge.split()[1])
        weight = int(edge.split()[2])
        self.graph[u - 1][v - 1] = weight
        self.graph[v - 1][u - 1] = weight

    def minimumDistance(self, minWeight, selectedVertex) -> int:
        minD = INF_VALUE

        for i in range(self.n_vertex):
            if minWeight[i] < minD and selectedVertex[i] == False:
                minD = minWeight[i]
                minIndex = i
        return minIndex

    def primAlgorithm(self) -> None:

        minWeight = [INF_VALUE] * self.n_vertex
        minWeight[0] = 0  # primeiro vertice
        # array que guarda os indices dos pesos para a arvore minima geradora
        constructedMST = [None] * self.n_vertex
        constructedMST[0] = -1  # vertice raiz

        # array de vertices a serem selecionados
        selectedVertex = [False] * self.n_vertex

        for i in range(self.n_vertex):
            # busca a menor distancia entre os vertices
            minD = self.minimumDistance(minWeight, selectedVertex)
            selectedVertex[minD] = True # marca vertice como visitado
            # guarda menores pesos e seus respectivos indices na arvore minima geradora
            for j in range(self.n_vertex):
                if self.graph[minD][j] > 0 and selectedVertex[j] == False and minWeight[j] > self.graph[minD][j]:
                    minWeight[j] = self.graph[minD][j]
                    constructedMST[j] = minD

        self.printMST(constructedMST)

    def printMST(self, MST) -> None:
        totalMinWeight = 0
        for i in range(1, self.n_vertex):
            totalMinWeight += self.graph[i][MST[i]]
        print(totalMinWeight)

    def printGraph(self) -> None:
        for i in range(self.n_vertex):
            for j in range(self.n_vertex):
                print(self.graph[i][j], end=" ")
            print()

    def printSum(self) -> None:
        print(sum([sum(i) for i in self.graph]))


def main() -> None:
  # leitura do arquivo .in
    fileName = input()

    # leitura do conteudo do arquivo .pajek
    pajekFile = open(fileName, 'r')
    contentPajekFile = pajekFile.readlines()

    # armazena quantidade de vertices
    n_vertex = int(contentPajekFile[0].split()[1])

    # construcao do grafo
    G = Graph(n_vertex)

    # insercao de arestas e peso
    for i in range(2, len(contentPajekFile)):
        G.addEdges(contentPajekFile[i])
    # algoritmo de Prim + impressao da arvore minima geradora
    G.primAlgorithm()


if __name__ == "__main__":
    main()
