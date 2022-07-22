def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(T, n, idx):
    l = left(idx)
    r = right(idx)
    curr_idx = idx
    if l < n and T[curr_idx] < T[l]:
        curr_idx = l
    if r < n and T[curr_idx] < T[r]:
        curr_idx = r
    if curr_idx != idx:
        T[idx], T[curr_idx] = T[curr_idx], T[idx]
        heapify(T, n, curr_idx)


def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    return T


def insert_to_heap(T, key):
    T = heap_sort(T)
    n = len(T)
    idx = n
    T.append(key)
    while idx > -1:
        parent_idx = parent(idx)
        if T[parent_idx] > key:
            T[idx], T[parent_idx] = T[parent_idx], T[idx]
            idx = parent_idx
        else:
            return idx


def heap_pop(T):
    n = len(T)
    T = heap_sort(T)
    T[0] = T.pop(n - 1)
    heapify(T, n - 1, 0)
    return T[0]

