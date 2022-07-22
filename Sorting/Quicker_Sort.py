def partition(T, left, right):
    key = T[right]
    i = left - 1
    k = i
    for j in range(left, right):
        if T[j] < key:
            i += 1
            k += 1
            T[j], T[k] = T[k], T[j]
            T[i], T[k] = T[k], T[i]
        elif T[j] == key:
            k += 1
            T[j], T[k] = T[k], T[j]
    T[right], T[k + 1] = T[k + 1], T[right]
    return i + 1, k +1


def quicker_sort(T, left, right):
    if left < right:
        q1, q2 = partition(T, left, right)
        quicker_sort(T, left, q1 - 1)
        quicker_sort(T, q2 + 1, right)

    return T
