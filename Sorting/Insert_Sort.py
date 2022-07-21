def insert_sort(T):
    n = len(T)
    if n < 2:
        return T
    for idx in range(1, n):
        value = T[idx]
        curr_idx = idx - 1
        while curr_idx != -1 and value < T[curr_idx]:
            T[curr_idx + 1] = T[curr_idx]
            curr_idx -= 1
        T[curr_idx + 1] = value
    return T
