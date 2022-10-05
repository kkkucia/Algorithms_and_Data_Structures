class Flag:
    def __init__(self):
        self.exist = True


def DFS(Gend, G, cycle, i):
    for j in range(Gend[i], len(G[i])):
        u = G[i][j]
        if u[1].exist:
            u[1].exist = False
            Gend[i] = j + 1
            DFS(Gend, G, cycle, u[0])
    cycle.append(i)


def Euler(G):
    n = len(G)
    cycle = []
    for i in range(n):
        if len(G[i]) % 2 != 0:
            return []
    graph = [[] for _ in range(n)]
    G_end = [0 for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            if u < v:
                flag = Flag()
                graph[u].append((v, flag))
                graph[v].append((u, flag))
    DFS(G_end, graph, cycle, 0)
    cycle = cycle[::-1]
    return cycle
    