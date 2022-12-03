from graph import Graph

def dijkstragraph(self, start):
    self.visits = [None]*self.N
    dist = [None]*self.N
    newMatrix = [[0]*len(dist) for i in range(len(dist))]
    for i in range(0,self.N):
        dist[i] = 100 # no inf in python
    dist[start] = 0
    for i in range(0,self.N):
        v = self.minVertex(dist)
        self.visits[v] = "VISITED"
        if (dist[v] == 100):
            return
        nList = self.neighbours(v)
        for j in range(0,len(nList)):
            w = nList[j]
            if (dist[w] > dist[v] + self.weight(v,w)):
                dist[w] = dist[v] + self.weight(v,w)
                path = self.weight(v,w)
                for k in range(0,self.N):
                    newMatrix[k][w] = 0
                newMatrix[v][w] = path 

    newGraph = Graph(newMatrix)
    return newGraph

if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        ]

    graph = Graph(matrix)

    new_graph = dijkstragraph(graph, 0)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8 
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    print(new_graph.weight(3, 6))   # 4
    print(new_graph.weight(5, 8))   # -1