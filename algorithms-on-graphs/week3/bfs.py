#Uses python3

import sys
import queue

def distance(adj:list, s:int, t:int):
    distance = [len(adj)] * len(adj)
    distance[s] = 0
    queue = [s]

    while queue:
      q = queue.pop(0)
      for neighbour in adj[q]:
        if distance[neighbour] == len(adj):
          queue.append(neighbour)
          distance[neighbour] = distance[q] + 1

    return distance[t] if distance[t] != len(adj) else -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
