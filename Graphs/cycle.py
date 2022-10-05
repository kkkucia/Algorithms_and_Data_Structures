def DFS(G, visited, parent, u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            return DFS(G, visited, parent, v)
        elif v != parent[u]:
            return True
    return False


def if_cycle(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    return DFS(G, visited, parent, 0)