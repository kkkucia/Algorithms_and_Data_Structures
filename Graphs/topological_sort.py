def DFS(G, visited, result, i):
    visited[i] = True
    for v in G[i]:
        if not visited[v]:
            DFS(G, visited, result, v)
    result.insert(0, i)

def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []
    for i in range(n):
        if not visited[i]:
            DFS(G, visited, result, i)
    return result
