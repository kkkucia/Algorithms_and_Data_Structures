# Given two strings str1 and str2 and 3 operations(insert, remove, replace) that can be performed. 
# Find minimum number of edits.(operations) required to convert ‘str1’ into ‘str2’.  
# All of the above operations are of equal cost. 


def recursion(DP, string1, string2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if DP[m][n] != -1:
        return DP[m][n]

    if string1[n - 1] == string2[m - 1]:
        DP[m][n] = recursion(DP, string1, string2, m - 1, n - 1)
        return DP[m][n]

    DP[m][n] = min(recursion(DP, string1, string2, m - 1, n - 1), \
                   recursion(DP, string1, string2, m - 1, n), \
                   recursion(DP, string1, string2, m, n - 1)) + 1
    return DP[m][n]


def edit_distance_problem(string1, string2):
    n = len(string1)
    m = len(string2)
    DP = [[-1] * (n + 1) for _ in range(m + 1)]

    return recursion(DP, string1, string2, m, n)