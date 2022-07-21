def select_sort(T):
    n = len(T)
    if n < 2:
        return T
    for idx in range(n):
        minimal_idx = idx
        for curr_idx in range(idx + 1, n):
            if T[curr_idx] < T[minimal_idx]:
                minimal_idx = curr_idx
        T[minimal_idx], T[idx] = T[idx], T[minimal_idx]
    return T