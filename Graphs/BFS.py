from collections import deque


def BFS(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [0 for _ in range(n)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                Q.append(v)
    return distance, parent