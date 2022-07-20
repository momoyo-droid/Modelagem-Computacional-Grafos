
'''
Disciplina Modelagem Computacional em Grafos
Projeto 2: Algoritmo de Prim
Ana Cristina Silva de Oliveira - nUSP 11965630
Jefferson Eduardo Muniz Bueno - nUSP 11275255
'''

# Preenche a lista a partir do input do arquivo pajek
def preenche_list(N, list):
    for i in range(N-1):
        x, y = (int(num) for num in input().split())
        list[x-1].append(y-1)
        list[y-1].append(x-1)


# Função main
if __name__ == '__main__':

    # Aux: palavras que serão descartadas
    # N: número de vértices
    aux, N = input().split()
    N = int(N)
    aux = input()

    # Cria uma lista de listas
    list = []
    for i in range(N):
        list.append([])
        list[i].append(i)

    # Preenche a lista com o input do arquivo pajek
    preenche_list(N, list)

    subGraphNumber = [0,1,3,7,8,9,11,12,13]
    
    for i in range(N):
        count = 0
        if len(list[i]) >= 2 and i in subGraphNumber:
            #print("{}: ".format(list[i][0]), end = " ")
            for j in list[i]:
                if j in subGraphNumber:
                    #print(j, end = ", ")
                    count = count + 1
            #print()
        # Caso o número de vizinhos presentes no subvértice seja maior que 1, é o vértice a ser retirado
        if count > 2: print("{}".format(i+1), end = "")


