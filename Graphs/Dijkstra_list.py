from queue import PriorityQueue
from math import inf


def relax(distance, parent, u, v):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def Dijkstra(G, s):
    n = len(G)
    Q = PriorityQueue()

    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]

    Q.put((0, s))
    distance[s] = 0
    while not Q.empty():
        dist, u = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]] and relax(distance, parent, u, v):
                Q.put((dist + v[1], v[0]))

    return parent, distance