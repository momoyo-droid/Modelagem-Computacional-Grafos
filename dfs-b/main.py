class Graph():
    def __init__(self, vertex) -> None:
        self.vertex = vertex
        self.list_adj = [[] for i in range(self.vertex)]       
    
    def create_edges(self, edge) -> None:
        u = int(edge.split()[0])
        v = int(edge.split()[1])
        
        self.list_adj[u-1].append(v-1)
    
    def dfs(self, node, visited_nodes, recursion_stack) -> bool:
        visited_nodes[node] = True
        recursion_stack[node] = True
        
        for i in self.list_adj[node]:
            if visited_nodes[i] == False:
                if self.dfs(i,visited_nodes,recursion_stack):
                    return True
            elif recursion_stack[i] == True:
                return True
        
        recursion_stack[node] = False
        return False
    
    def isCyclic(self) -> bool:
        visited_nodes = [False] * (self.vertex+1)
        recursion_stack = [False] * (self.vertex+1)
            
        for node in range(self.vertex):
            if visited_nodes[node] == False:
                if self.dfs(node, visited_nodes,recursion_stack) == True:
                    return True
        return False   
    
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
        if lines_f[i] == '\n':
            break
        G.create_edges(lines_f[i])
    
    if G.isCyclic() == True:
        print("S")
    else:
        print("N")
            
if __name__ == "__main__":
    main()