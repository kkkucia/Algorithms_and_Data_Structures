from queue import PriorityQueue
from math import inf


def relax(G, u, v, distance, parent):
    if distance[v] > distance[u] + G[u][v]:
        distance[v] = distance[u] + G[u][v]
        parent[v] = u
        return True
    return False


def Dijkstra(G, s):
    n = len(G)
    Q = PriorityQueue()
    visited = [False] * n
    parent = [None] * n
    distance = [inf] * n
    distance[s] = 0
    Q.put((0, s))
    while not Q.empty():
        dist, u = Q.get()
        visited[u] = True
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                if relax(G, u, v, distance, parent):
                    Q.put((dist + G[u][v], v))

    return parent, distance
