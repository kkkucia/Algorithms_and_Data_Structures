def partition(T, left, right):
    key = T[right]
    i = left - 1
    for j in range(left, right):
        if T[j] <= key:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[right] = T[right], T[i + 1]
    return i + 1


def select_rec(T, k, left, right):
    if left == right:
        return T[left]
    if left < right:
        q = partition(T, left, right)
        if q == k:
            return T[q]
        elif q < k:
            return select(T, k, q + 1, right)
        else:
            return select(T, k, left, q - 1)


def select(T, k, left, right):
    while left <= right:
        if left == right:
            return T[left]
        q = partition(T, left, right)
        if q == k:
            return T[q]
        elif q > k:
            right = q - 1
        else:
            left = q + 1
