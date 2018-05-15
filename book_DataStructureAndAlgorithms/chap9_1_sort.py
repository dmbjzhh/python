# -*- coding:utf-8 -*-

# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)): # 开始片段第一个元素已经排序
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1] # 反序逐个后移元素，确定插入位置
            j -= 1
        lst[j] = x

# 我写的插入排序
def insert_sort_mine(lst):
    for i in range(len(lst)-1, -1, -1):
        x = lst[i]
        j = i
        while j < len(lst) - 1 and lst[j+1] < x:
            lst[j] = lst[j+1]
            j += 1
        lst[j] = x

# 我写的选择排序
def select_sort_mine(lst):
    for i in range(0, len(lst)-1):
        min = lst[i]
        m = i
        for j in range(i+1, len(lst)):
            if min > lst[j]:
                min = lst[j]
                m = j
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]   

# 书中的选择排序
def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i, len(lst)):
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]

# 我的冒泡排序
def bubble_sort_mine(lst):
    for j in range(0, len(lst)-1):
        for i in range(0, len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

# 冒泡排序
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]

# 改进后的冒泡排序
def bubble_sort_improve(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break

# 我的快速排序
def quick_sort_mine(lst):
    
    def change(left, right):
        if left >= right:
            return
        pivot = lst[left]
        i, j = left+1, right
        while i < j:
            while i < j and lst[j] >= pivot:
                j -= 1
            while i < j and lst[i] <= pivot:
                i += 1
            lst[i], lst[j] = lst[j], lst[i]
        lst[i], lst[left] = pivot, lst[i]
        change(left, i-1)
        change(i+1, right)
    change(0, len(lst)-1)

# 书中的快速排序
def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)

def qsort_rec(lst, l, r):
    if l >= r: return # 分段无记录或者只有一个记录
    i = l
    j = r
    pivot = lst[i] # lst[i]是初始空位
    while i < j: # 找pivot最终位置
        while i < j and lst[j] >= pivot:
            j -= 1 # 用j向左扫描找小于pivot的记录
        if i < j:
            lst[i] = lst[j]
            i += 1 # 小记录移到左边
        while i < j and lst[i] <= pivot:
            i += 1 # 用i向右查找大于pivot的记录
        if i < j: 
            lst[j] = lst[i]
            j -= 1 # 大记录移到右边
    lst[i] = pivot # 将pivot存入最终位置
    qsort_rec(lst, l, i-1) # 递归处理左半区间
    qsort_rec(lst, i+1, r) # 递归处理右半区间
                    
# 另一种快速排序
def quick_sort_another(lst):
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin]
        i = begin
        for j in range(begin+1, end+1):
            if lst[j] < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i-1)
        qsort(lst, i+1, end)

# 书中的归并排序
def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high: # 反复赋值两分段首记录中较小的
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid: # 复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high: # 复制第二段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1
def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen < llen: # 归并长slen的两段
        merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2 * slen
    if i + slen < llen: # 剩下两段，后段长度小于slen
        merge(lfrom, lto, i, i+slen, llen)
    else: # 只剩下一段，复制到表lto
        for j in range(i, llen):
            lto[j] = lfrom[j]
def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None]*llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen) # 结果存回原位
        slen *= 2
    
# 书中的分配排序
class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum
        
def radix_sort(lst, d):
    rlists = [[] for i in range(10)]
    llen = len(lst)
    for m in range(-1, -d-1, -1):
        for j in range(llen):
            rlists[lst[j].key[m]].append(lst[j])
        j = 0
        for i in range(10):
            tmp = rlists[i]
            for k in range(len(tmp)):
                lst[j] = tmp[k]
                j += 1
            rlists.remove(rlists[i])

if __name__ == "__main__":
    l1 = [2, 3, 1, 4, 9, 6, 5, 8, 7]
    insert_sort(l1)
    print l1
    l2 = [2, 3, 1, 4, 9, 6, 5, 8, 7]
    insert_sort_mine(l2)
    print l2
    l3 = [2, 3, 1, 4, 9, 6, 5, 8, 7]
    select_sort_mine(l3)
    print l3
    l4 = [2, 3, 1, 4, 9, 6, 5, 8, 7]
    bubble_sort_mine(l4)
    print l4
    l5 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort_mine(l5)
    print l5
    l6 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    merge_sort(l6)
    print l6




