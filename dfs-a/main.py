class Graph():
    def __init__(self, vertex) -> None:
        self.vertex = vertex
        self.list_adj = [[] for i in range(self.vertex)]       
    
    def create_edges(self, edge) -> None:
        u = int(edge.split()[0])
        v = int(edge.split()[1])
        
        self.list_adj[u-1].append(v-1)
        self.list_adj[v-1].append(u-1)
    
    def dfs(self, store_cc, vertex, visited_nodes) -> list:
        visited_nodes[vertex] = True
        
        store_cc.append(vertex)
        
        for i in self.list_adj[vertex]:
            if visited_nodes[i] == False:
                store_cc = self.dfs(store_cc,i,visited_nodes)
        
        return store_cc
    
    def connected_components(self) -> list:
        visited_nodes = []
        cc = []
        
        for i in range(self.vertex):
            visited_nodes.append(False)
            
        for v in range(self.vertex):
            if visited_nodes[v] == False:
                store_cc = []
                cc.append(self.dfs(store_cc,v,visited_nodes))

        return cc            
    
def main():
    # leitura do arquv
    filename = input()
    
    pajek_file = open(filename, 'r')
    
    lines_f = pajek_file.readlines()
    
    # cria grafo de acordo c numero de vertices
    vertex = int(lines_f[0].split()[1])
    G = Graph(vertex)
        
    # adiciona cada aresta no grafo    
    for i in range(2, len(lines_f)):
        G.create_edges(lines_f[i])
    
    # busca componentes conexos
    cc = G.connected_components()
    cc.sort(reverse=True, key=len)
    
    print(len(cc))
    
    for i in cc:
        print(len(i))
            

if __name__ == "__main__":
    main()