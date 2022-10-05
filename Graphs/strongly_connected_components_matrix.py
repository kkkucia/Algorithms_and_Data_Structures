from collections import deque


def components(G):
    n = len(G)
    Q = deque()
    visited = [False] * n
    num_of_component = [0] * n
    count = 0
    for idx in range(n):
        if num_of_component[idx] == 0:
            Q.append(idx)
            visited[idx] = True
            count += 1
            num_of_component[idx] = count
            while Q:
                u = Q.popleft()
                for v in range(n):
                    if G[u][v] != 0 and not visited[v]:
                        num_of_component[v] = count
                        visited[v] = True
                        Q.append(v)
    return count, num_of_component
