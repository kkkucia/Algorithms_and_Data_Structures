from collections import deque


def BFS(G, s, t, parent):
    n = len(G)
    visited = [False for _ in range(n)]
    Q = deque()
    visited[s] = True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)
    return visited[t]


def Edmonds_Karp(G, s, t):
    n = len(G)
    max_flow = 0
    parent = [None for _ in range(n)]
    while BFS(G, s, t, parent):
        curr_flow = float('inf')
        curr = t
        while curr != s:
            curr_flow = min(curr_flow, G[parent[curr]][curr])
            curr = parent[curr]
        max_flow += curr_flow
        curr = t
        while curr != s:
            p = parent[curr]
            G[p][curr] -= curr_flow
            G[curr][p] += curr_flow
            curr = p
    return max_flow
    