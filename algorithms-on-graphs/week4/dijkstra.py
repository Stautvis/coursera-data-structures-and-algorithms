#Uses python3

import sys
import queue


def distance(adj: list, cost: list, s:int, t:int):
    distance=[float('inf')]*len(adj)
    distance[s] = 0
    queue = [s]
    while queue:
        q = queue.pop(0)
        for i in range(len(adj[q])):
            index = adj[q][i]
            if distance[index] > distance[q] + cost[q][i]:
                distance[index] = distance[q] + cost[q][i]
                queue.append(index)
    return distance[t] if distance[t] != float('inf') else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
