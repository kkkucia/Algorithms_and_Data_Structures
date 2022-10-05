from math import inf


def relax(G, distance, parent, e):
    if distance[G[e][1]] > distance[G[e][0]] + G[e][2]:
        distance[G[e][1]] = distance[G[e][0]] + G[e][2]
        parent[G[e][1]] = G[e][0]


def Bellman_Ford(G, s):
    edges = len(G)
    V = 0
    for i in range(edges):
        V = max(G[i][0], G[i][1], V)
    distance = [inf for _ in range(V+1)]
    parent = [None for _ in range(V + 1)]
    distance[s] = 0
    for v in range(V-1):
        for e in range(edges):
            relax(G, distance, parent, e)
    for i in range(edges):
        if distance[G[i][1]] > distance[G[i][0]] + G[i][2]:
            return True
    return False