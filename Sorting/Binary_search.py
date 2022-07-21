def binary_search(T, key):
    left = 0
    right = len(T) - 1
    while left <= right:
        middle = (right + left)//2
        if T[middle] == key:
            return middle
        elif T[middle] > key:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def bsearch_floor(T, left, right, key):
    while left < right:
        middle = (left + right + 1) // 2
        if key >= T[middle]:
            left = middle
        else:
            right = middle - 1
    return left


def bsearch_roof(T, left, right, key):
    while left < right:
        middle = (left + right) // 2
        if key <= T[middle]:
            right = middle
        else:
            left = middle + 1
    return right
