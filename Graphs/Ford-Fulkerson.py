from math import inf


def DFS_visit(G, visited, parent, u):
    visited[u] = True
    for v in range(len(G)):
        if not visited[v] and G[u][v] != 0:
            parent[v] = u
            DFS_visit(G, visited, parent, u)


def DFS(G, s, t, parent):
    n = len(G)
    visited = [False for _ in range(n)]
    DFS_visit(G, visited, parent, s)
    return visited[t]


def FordFulkersonMatrix(G, s, t):
    n = len(G)
    parents = [None for _ in range(n)]
    max_flow = 0
    while DFS(G, s, t, parents):
        curr_flow = inf
        curr = t
        while curr != s:
            curr_flow = min(curr_flow, G[parents[curr]][curr])
            curr = parents[curr]
        max_flow += curr_flow
        curr = t
        while curr != s:
            p = parents[curr]
            G[p][curr] -= curr_flow
            G[curr][p] += curr_flow
            curr = parents[curr]
    return max_flow
    