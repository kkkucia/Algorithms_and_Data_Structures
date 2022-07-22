from random import randint


def partition(T, l, r):
    key = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] <= key:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_sort(T, l, r):
    if len(T) < 2:
        return
    if l < r:
        q = partition(T, l, r)
        quick_sort(T, l, q - 1)
        quick_sort(T, q + 1, r)


def quick_sort_2(T, l, r):
    while l < r:
        q = partition(T, l, r)
        quick_sort(T, l, q - 1)
        r = q + 1

def Qsort(T):
    quick_sort(T, 0, len(T) - 1)
    return T


def Qsort2(T):
    quick_sort_2(T, 0, len(T) - 1)
    return T


def randomized_quicksort(T, l, r):
    n = len(T)
    if n < 2:
        return
    if l < r:
        q = randomized_partition(T, l, r)
        randomized_quicksort(T, l, q - 1)
        randomized_quicksort(T, q + 1, r)


def randomized_partition(T, l, r):
    idx = randint(l, r)
    key = T[idx]
    i = l - 1
    for j in range(l, r):
        if T[j] <= key:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[idx] = T[idx], T[i + 1]
    return i + 1


def sort(T):
    randomized_quicksort(T, 0, len(T) - 1)
    return T

