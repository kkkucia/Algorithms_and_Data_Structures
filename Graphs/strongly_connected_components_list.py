def DFS1(G, visited, first_dfs, u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFS1(G, visited, first_dfs, v)
    first_dfs.append(u)


def reverse_edges(G):
    n = len(G)
    reversed_G = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            reversed_G[v].append(u)
    return reversed_G


def DFS2(reversed_G, visited, components, u, num_of_component):
    visited[u] = True
    components[num_of_component].append(u)
    for v in reversed_G[u]:
        if not visited[v]:
            DFS2(reversed_G, visited, components, v, num_of_component)


def strongly_connected_components(G):
    n = len(G)
    visited = [False for _ in range(n)]
    first_dfs = []

    for u in range(n):
        if not visited[u]:
            DFS1(G, visited, first_dfs, u)

    reversed_G = reverse_edges(G)
    visited = [False for _ in range(n)]
    components = []
    num_of_component = 0

    for u in reversed(first_dfs):
        if not visited[u]:
            components.append([])
            DFS2(reversed_G, visited, components, u, num_of_component)
            num_of_component += 1

    return components
