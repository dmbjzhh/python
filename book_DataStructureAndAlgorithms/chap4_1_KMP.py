# -*- coding:utf-8 -*-

# 构造next数组函数
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1]*m  # 初始数组元素全为-1
    while i < m-1: # 生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            pnext[i] = k # 设置pnext元素
        else:
            k = pnext[k] # 退到更短相同前缀
    return pnext

# KMP算法的改进
def gen_pnext_improve(p):
    '''改进一点的版本，在下一跳字符和当前相同时，跳到下一跳的下一跳，跳的更远'''
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

# 自己的神他喵麻烦构建next数组版本
def MINE_gen_pnext(p):
    '''生成针对p中各个未知的i的下一跳位置表'''
    pnext = [-1, 0]
    pnext=[]
    count = 0
    for j in range(0, len(p)+1):
        ps = p[0:j]
        if ps == '':
            continue
        for i in range(len(ps), 1, -1):
            if ps[0: i-1] == ps[-i+1:]:
                pnext.append(len(ps[0: i-1]))
                
        if count<len(pnext):
            count += 1
        else:
            pnext.append(0)
            count += 1
    for i in range(len(pnext)-1, 0, -1):
        pnext[i] = pnext[i-1]
    pnext[0] = -1
    return pnext 

# kmp匹配主函数
def matching_KMP(t, p):
    '''KMP Main fuction, t for target, p for pattern'''
    i, j = 0, 0
    n, m = len(t), len(p)
    pnext = gen_pnext(p)
    while j < n and i < m: # i == m说明找到了匹配
        if i == -1 or t[j] == p[i]: # 刚开始或者字符匹配时，考虑p中的下一字符
            j, i = j+1, i+1
        else: # 字符不匹配，则考虑pnext对应的下一字符
            i = pnext[i]
    if i == m: # 找到匹配，返回其下标
        return j - i
    return -1 # 无匹配

print matching_KMP('ABCDEFG', 'EFG')