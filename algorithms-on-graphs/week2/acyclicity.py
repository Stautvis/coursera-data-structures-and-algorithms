#Uses python3

import sys


def acyclic(adj):
    visited = [0] * len(adj)
    prec = [0] * len(adj)
    for index in range(len(adj)):
        if visited[index]: continue
        if dfs(adj, index, visited, prec) == 1:
            return 1
    return 0

def dfs(adj: list, index: int, visited:list , prec: list):
    visited[index] = 1
    prec[index] = 1
    for i in range(len(adj[index])):
        if visited[adj[index][i]] == 0 and dfs(adj, adj[index][i], visited, prec):
            return 1;
        elif prec[adj[index][i]]:
            return 1
    prec[index] = 0
    return 0
        

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
