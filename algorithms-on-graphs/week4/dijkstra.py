#Uses python3

import sys
import queue

class Node(object):
    def __init__(self, index, cost):
        self.index = index
        self.cost = cost
    def __lt__(self, obj):
        return self.cost < obj.cost
    def __cmp__(self, other):
        return self.cost - other.cost

def distance(adj:list, cost:list, s:int, t:int):
    #write your code here
    distance=[float('inf')]*len(adj)
    distance[s] = 0
    q = queue.PriorityQueue()
    q.put(Node(s, distance[s]))
    while not q.empty():
         u = q.get()
         u_index = u.index
         for v in adj[u_index]:
             v_index = adj[u_index].index(v)
             if distance[v] > distance[u_index] + cost[u_index][v_index]:
                distance[v] = distance[u_index] + cost[u_index][v_index]
                q.put(Node(v, distance[v]))
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
