class Vertex:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0


def make(v):
    return Vertex(v)


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_edges(G):
    n = len(G)
    edges = []
    for i in range(n):
        for v in range(len(G[i])):
            if (G[i][v][0], i, G[i][v][1]) not in edges:
                edges.append((i, G[i][v][0], G[i][v][1]))
    return edges


def kruskal(G):
    n = len(G)
    edges = make_edges(G)
    edges.sort(key=lambda x: x[2])
    MST = []
    Ver = [make(i) for i in range(n)]
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(Ver[u]) != find(Ver[v]):
            MST.append(edges[i])
            union(Ver[u], Ver[v])
    return MST
