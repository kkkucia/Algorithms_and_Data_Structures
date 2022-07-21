def bubble_sort(T):
    n = len(T)
    if n < 2:
        return T
    for i in range(n):
        for j in range(n - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T
