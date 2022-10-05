def DFS_visit(G, visited, parent, result, u):
    visited[u] = True
    result.append(u)
    for v in G[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            DFS_visit(G, visited, parent, result, v)


def DFS(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    result = []

    DFS_visit(G, visited, parent, result, s)
    return result
