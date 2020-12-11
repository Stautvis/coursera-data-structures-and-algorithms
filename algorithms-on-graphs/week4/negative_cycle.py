#Uses python3

import queue
import sys


def negative_cycle(graph, V, E, src): 
    inf = 100000
    dis = [inf] * V
    dis[src] = 0
  
    for i in range(V - 1): 
        for j in range(E): 
            if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]: 
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2] 

    for i in range(E): 
        x = graph[i][0] 
        y = graph[i][1] 
        weight = graph[i][2] 
        if dis[x] != inf and dis[x] + weight < dis[y]: 
            return 1
    return 0
  

 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    graph = []

    for ((a, b), w) in edges:
        graph.append([a - 1, b - 1, w])
    print(negative_cycle(graph, n, m, 0))
