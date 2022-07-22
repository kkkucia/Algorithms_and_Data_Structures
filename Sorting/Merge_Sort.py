
def merge(tab1, tab2):
    p1, p2 = 0, 0
    n1 = len(tab1)
    n2 = len(tab2)
    T = []
    while p1 < n1 and p2 < n2:
        if tab1[p1] < tab2[p2]:
            T.append(tab1[p1])
            p1 += 1
        else:
            T.append(tab2[p2])
            p2 += 1
    while p1 < n1:
        T.append(tab1[p1])
        p1 += 1
    while p2 < n2:
        T.append(tab2[p2])
        p2 += 1

    return T


def Merge_Sort(tab):
    n = len(tab)
    if n < 2:
        return tab
    center = (n + 1) // 2
    left = tab[:center]
    right = tab[center:]
    L = Merge_Sort(left)
    R = Merge_Sort(right)
    T = merge(L, R)
    
    return T
