import sys
import random
from random import random

def create_matrix(matrix, n_vertices, prob):
    for i in range(n_vertices):
        row = []
        for j in range(n_vertices):
            row += [0]
        matrix += [row]
    return matrix

def get_random_number(matrix, n_vertices, prob):
    for i in range(n_vertices):
        for j in range(i+1,n_vertices):
            x = random()
            
            if x > prob:
                matrix[i][j] = 1
                matrix[j][i] = 1
            else:
                continue

def display_matrix(matrix, n_vertices):
    for i in range(n_vertices):
        print(matrix[i])
        
def main():
    n_vertices = int(input("enter a value for the number of vertices in the graph\n"))
    prob = float(input("enter a value between 0 and 1 for the probability of edges between vertices\n"))
    
    if prob > 0 and prob < 1:
        matrix = []
        create_matrix(matrix, n_vertices, prob)
        get_random_number(matrix, n_vertices, prob)
        display_matrix(matrix, n_vertices)
    else:
        sys.exit("enter a value between 0 and 1 for the probability")
    
if __name__ == "__main__":
    main()