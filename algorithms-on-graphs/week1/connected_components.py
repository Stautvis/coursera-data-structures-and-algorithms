#Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = [0] * len(adj)

    for i in range(len(adj)): # for each vertices
        if not visited[i]: # not visited
            visit(adj, i, visited) # visit
            result += 1 # add +1 component
    return result

def visit(adj, edge, visited):
    visited[edge] = 1
    for i in range(len(adj[edge])): # visit neighboring edges
        if not visited[adj[edge][i]]: # not visited
            visit(adj, adj[edge][i], visited) # then visit

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
