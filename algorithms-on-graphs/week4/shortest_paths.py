#Uses python3

import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    inf = 10**19

    distance[s] = 0
    reachable[s] = 1

    q = queue.Queue()

    for i in range(n):
        for u in range(n):
            for v_index, v in enumerate(adj[u]):
                w = distance[u] + cost[u][v_index]
                if distance[u] != inf and distance[v] > w:
                    distance[v] = w
                    reachable[v] = 1
                    if i == n - 1:
                        q.put(v)

    visited = [0] * n
    while not q.empty():
        u = q.get()
        visited[u] = 1
        if u != s:
            shortest[u] = 0
        for v in adj[u]:
            if visited[v] == 0:
                q.put(v)
                visited[v] = 1
                shortest[v] = 0
    distance[s] = 0

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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

