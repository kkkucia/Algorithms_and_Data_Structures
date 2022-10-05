def DFS(visited, distance, low, parent, curr_dist, i, G):
    visited[i] = True
    distance[i] = curr_dist
    curr_dist += 1
    low[i] = distance[i]
    for v in G[i]:
        if not visited[v]:
            parent[v] = i
            DFS(visited, distance, low, parent, curr_dist, v)
            low[i] = min(low[i], low[v])
        elif parent[i] != v:
            low[i] = min(low[i], distance[v])


def find_bridges(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [0 for _ in range(n)]
    low = [float('inf') for _ in range(n)]

    curr_dist = 0
    for i in range(n):
        if not visited[i]:
            DFS(visited, distance, low, parent, curr_dist, i, G)
    bridges = []
    for i in range(n):
        if low[i] == distance[i] and parent[i] is not None:
            bridges.append((parent[i], i))
    return bridges