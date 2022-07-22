from random import randint


def count_sort(T, divider):
    n = len(T)
    count = [0 for _ in range(10)]
    result = [0 for _ in range(n)]
    for i in range(n):
        idx = int((T[i] // divider) % 10)
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        idx = int((T[i] // divider) % 10)
        result[count[idx] - 1] = T[i]
        count[idx] -= 1

    for i in range(n):
        T[i] = result[i]

    return T


def radix_sort(T):
    n = len(T)
    max_number = 0
    for i in range(n):
        max_number = max(max_number, T[i])
    divider = 1
    while max_number / divider > 0:
        count_sort(T, divider)
        divider *= 10
        
    return T

