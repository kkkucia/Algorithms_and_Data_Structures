from queue import PriorityQueue
from math import inf


def Prim(G, s):
    n = len(G)
    Q = PriorityQueue()

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    scale = [inf for _ in range(n)]
    scale[s] = 0
    Q.put((0, s))
    while not Q.empty():
        s, u = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]] and scale[v[0]] > v[1]:
                scale[v[0]] = v[1]
                parent[v[0]] = u
                Q.put((scale[v[0]], v[0]))

    output = []
    for i in range(n):
        if parent[i] is not None:
            output.append((i, parent[i], scale[i]))
    return output
