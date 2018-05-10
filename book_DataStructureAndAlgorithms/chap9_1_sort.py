# -*- coding:utf-8 -*-

class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum

# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)): # 开始片段第一个元素已经排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1] # 反序逐个后移元素，确定插入位置
            j -= 1
        lst[j] = x

# 我写的插入排序
def insert_sort_mine(lst):
    for i in range(len(lst)-1, -1, -1):
        x = lst[i]





