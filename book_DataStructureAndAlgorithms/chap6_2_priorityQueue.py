# -*- coding:utf-8 -*-

class PrioQueueError(ValueError):
    pass

# 优先队列的list实现，按位置决定优先顺序
class PrioQue_list:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    # 插入元素
    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in pop')
        return self._elems.pop()

# 基于堆的优先队列
class PrioQue_heap:
    '''Implementing priority queues usign heaps
    '''
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
    
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]
    # 入队操作
    def enqueue(self, e):
        self._elems.append(None) # None被添加到末尾
        self.siftup(e, len(self._elems) -1)
    
    # 拿着新元素找位置，而不是先存入元素再逐个交换，这样节省开销
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2 # //是取整数，返回商的整数部分，i指向最后一个结点，j指向父结点
        while i > 0 and e < elems[j]: # 这是一个小顶堆
            elems[i] = elems[j] # 结点交换，elems[i]其实是None
            i, j = j, (j-1)//2 # 继续上升
        elems[i] = e
    
    # 出队操作
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
    
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1 # j指向左孩子
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1 # elems[j]不大于其兄弟节点的数据
            if e < elems[j]: # e在三者中最小，找到了位置
                break
            elems[i] = elems[j] # elems[j]在三者中最小，上移
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

# 堆排序
def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1]<elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
        elems[i] = e
    
    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end-1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)