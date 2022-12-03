def salesman(city_map):
    
    citycnt = len(city_map[0])
    visited = [None]*citycnt
    visited[0] = True
    currpath = [None]*citycnt
    currpath[0] = 0
    cvisited = 1
    currweight = 0
    bestweight = 10000
    bestpath = path(visited, currpath, citycnt, cvisited, city_map, currweight, bestweight)
    print(bestpath)
    return bestpath




def weight(matrix, v1, v2):
        if (matrix[v1][v2] != 0):
            x = matrix[v1][v2]
            return x
        return -1



def path(visited, currpath, citycnt, cvisited, city_map, currweight, bestweight):
    if (cvisited == citycnt):
        #TODO
        return

    for i in range(0,citycnt):
        if(city_map[currpath[cvisited-1]][i] != 0 and visited[i] != True):
            currpath[cvisited] = i
            visited[i] = True
            cvisited += 1
            currweight += weight(city_map, currpath[cvisited-1], i)

    if (currweight < bestweight):
        bestweight = currweight

    return currpath



if __name__ == "__main__":
    
    cost = 0

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45