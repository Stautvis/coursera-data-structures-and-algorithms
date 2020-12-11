#Uses python3
import sys
import math

def to_adj(x:list, y:list):
    n = len(x)

    adj = list()
    weight = [[0] * n for _ in range(n)]

    for i in range(n):
        adj.append(list(v for v in range(n) if v != i))
        for j in range(n):
            if i != j:
                w = math.sqrt( ((x[i]-x[j])**2)+((y[i]-y[j])**2))
                weight[i][j] = w
                weight[j][i] = w
    return adj, weight

def minimum_distance(x: list, y: list):
    result = 0.

    used_edges = set()
    used_edges.add(0)

    adj, weight = to_adj(x, y)
    n = len(adj)

    while len(used_edges) != n:
        crossing = set()
        for u in used_edges:
            for v in adj[u]:
                if v not in used_edges:
                    crossing.add((u, v))
        edge = sorted(crossing, key=lambda e: weight[e[0]][e[1]])[0]
        result += weight[edge[0]][edge[1]]
        used_edges.add(edge[1])

    return result



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
