def count_sort(T, i):
    n = len(T)
    k = ord('z') - ord('a') + 1
    count = [0 for _ in range(k)]
    result = [0 for _ in range(n)]
    for j in range(n):
        idx = ord(T[j][i]) - ord('a')
        count[idx] += 1
    for j in range(1, k):
        count[j] += count[j - 1]
    for j in range(n - 1, -1, -1):
        idx = ord(T[j][i]) - ord('a')
        result[count[idx] - 1] = T[j]
        count[idx] -= 1

    return result


def radix_sort(T):
    n = len(T[0])
    for i in range(n-1, -1, -1):
        T = count_sort(T, i)

    return T


def string_sort(T):
    n = len(T)
    max_length = 0
    for i in range(n):
        max_length = max(max_length, len(T[i]))
    buckets = [[]for _ in range(max_length)]
    for string in T:
        length = len(string)
        buckets[length-1].append(string)
    for i in range(max_length):
        if len(buckets[i]) > 1:
            buckets[i] = radix_sort(buckets[i])
    output = []
    for i in range(max_length):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])

    return output
