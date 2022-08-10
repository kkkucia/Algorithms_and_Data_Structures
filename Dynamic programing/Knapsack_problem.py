# only recursion
def recursion_only(W, C, idx, limit):
    if idx == len(W):
        return 0
    if limit - W[idx] < 0:
        return 0

    maxi = 0
    for i in range(idx + 1, len(W)):
        val = recursion_only(W, C, i, limit - W[idx])
        if val > maxi:
            maxi = val
    return maxi + C[idx]


def knapsack_rec_only(W, C, limit):
    n = len(W)
    maxi = 0
    for idx in range(n):
        val = recursion_only(W, C, idx, limit)
        if val > maxi:
            maxi = val
    return maxi


# add dynamic array
def recursion_with_dynamic(DP, W, C, idx, limit):
    if idx == len(W):
        return 0
    if limit - W[idx] < 0:
        return 0
    if DP[idx][limit] != -1:
        return DP[idx][limit]
    maxi = 0
    for i in range(idx + 1, len(W)):
        val = recursion_with_dynamic(DP, W, C, i, limit - W[idx])
        if val > maxi:
            maxi = val
    DP[idx][limit] = maxi + C[idx]
    return DP[idx][limit]


def knapsack_rec_with_dynamic(W, C, limit):
    n = len(W)
    maxi = 0
    DP = [[-1] * (limit + 1) for _ in range(n)]
    for idx in range(n):
        val = recursion_with_dynamic(DP, W, C, idx, limit)
        if val > maxi:
            maxi = val
    return maxi


# print array + update start
def recursion(DP, W, C, idx, limit):
    if idx == len(W):
        return 0
    if limit - W[idx] < 0:
        return 0
    if DP[idx][limit] != -1:
        return DP[idx][limit]
    maxi = 0
    for i in range(idx + 1, len(W)):
        val = recursion(DP, W, C, i, limit - W[idx])
        if val > maxi:
            maxi = val
    DP[idx][limit] = maxi + C[idx]
    return DP[idx][limit]


def knapsack(W, C, limit):
    n = len(W)
    new_W = [0]
    new_C = [0]
    for i in range(n):
        new_W.append(W[i])
        new_C.append(C[i])
    DP = [[-1] * (limit + 1) for _ in range(n + 1)]
    maxi = recursion(DP, new_W, new_C, 0, limit)
    l = limit
    output = []

    for i in range(1, len(new_W)):
        if DP[i][l] == maxi:
            output.append(i)
            l -= new_W[i]
            maxi -= new_C[i]
    return output
