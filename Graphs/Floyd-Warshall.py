from math import inf


def Floyd_Warshall(G):
    n = len(G)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            elif G[i][j] != 0:
                distance[i][j] = G[i][j]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance
