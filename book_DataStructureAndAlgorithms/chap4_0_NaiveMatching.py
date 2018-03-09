# -*- coding:utf-8 -*-

'''朴素的串匹配算法，暴力'''

def naive_matching(t, p):
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

def MINE_naive_matching(t, p):
    i, j = 0, 0
    lt = len(t)
    lp = len(p)
    while i < lt:
        if t[i] == p[j]:
            if j == lp - 1:
                return i - lp + 1
            else:
                i, j = i+1, j+1
        else:
            i, j = i+1, 0    
    return -1

a = 'abcdsfgsdffvdegfgh'
b = 'gs'

print(naive_matching(a, b))
print(MINE_naive_matching(a, b))
            