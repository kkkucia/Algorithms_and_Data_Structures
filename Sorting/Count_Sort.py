def count_sort(T):
    n = len(T)
    count = [0 for _ in range(10)]
    result = [0 for _ in range(n)]
    for number in T:
        count[number] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        count[T[i]] -= 1
        result [count[T[i]]] = T[i]
        
    return result
