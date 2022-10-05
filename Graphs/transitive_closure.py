def transitive_closure(G):
    graph = [[0 for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j or G[i][j] != 0:
                graph[i][j] = 1

    n = len(graph)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                graph[u][v] = graph[u][v] or (graph[u][k] and graph[k][v])
    return graph

