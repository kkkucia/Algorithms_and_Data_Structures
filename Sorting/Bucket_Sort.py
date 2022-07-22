def insert_sort(T):
    n = len(T)
    if n < 2:
        return T
    for i in range(1, n):
        key = T[i]
        j = i - 1
        while j > -1 and T[j] > key:
            T[j] = T[j + 1]
            j -= 1
        T[j + 1] = key
    return T


def bucket_sort(T):
    n = len(T)
    buckets = [[] for _ in range(n + 1)]
    for num in T:
        norm_num = num / n
        bucket_idx = int(n * norm_num)
        buckets[bucket_idx].append(num)
    for i in range(n):
        buckets[i] = insert_sort(buckets[i])
    output = []
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])

    return output


def bucket_sort_section(T, a, b):
    n = len(T)
    buckets = [[] for _ in range(n + 1)]
    section = (b - a) / n
    for num in T:
        idx = int((num - a) // section)
        buckets[idx].append(num)
    for i in range(len(buckets)):
        buckets[i] = insert_sort(buckets[i])
    output = []
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])

    return output