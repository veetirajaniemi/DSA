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
        print(f"Vertex {v} VISITED.")
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
        [0,11,6,10,0],
        [11,0,3,6,4],
        [6,3,0,2,0],
        [10,6,2,0,6],
        [0,4,0,6,0],
        ]

    graph = Graph(matrix)
    new_graph = dijkstragraph(graph, 0)
    print(new_graph.graph_matrix)