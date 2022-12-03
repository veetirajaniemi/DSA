from graph import Graph


def floyd(graph):
    D = [[0]*graph.N for i in range(graph.N)]
    for i in range(0,graph.N):
        for j in range(0,graph.N):
            if (graph.weight(i,j) != -1):
                D[i][j] = graph.weight(i,j)
            else:
                if (i != j):
                    D[i][j] = 100

    for k in range(0,graph.N):
        for l in range(0,graph.N):
            for m in range(0,graph.N):
                if (D[l][m] > (D[l][k] + D[k][m])):
                    D[l][m] = D[l][k] + D[k][m]

    for i in range(0,graph.N):
        for j in range(0,graph.N):
            if D[i][j] == 100:
                D[i][j] = 0
    return D
    

if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    graph = Graph(matrix)
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 