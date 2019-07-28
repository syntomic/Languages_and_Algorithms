def naive_matching(t, p):
    """朴素匹配算法"""
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i+1, j+1
        else:
            i, j = 0, j-i+1
    if i == m:
        return j - i
    return -1

if __name__ == '__main__':
    p = 'abcac'
    t = 'ababcabcacbab'
    print(naive_matching(t, p))    