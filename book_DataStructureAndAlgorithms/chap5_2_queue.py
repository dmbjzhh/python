# -*- coding:utf-8 -*-

# 基于python的list实现顺序表示的队列

# 队列为空无法dequeue，定义异常
class QueueUnderflow(ValueError):
    pass

class SQueue():
    def __init__(self, init_len = 8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0
    
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    # 出队
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
    
    # 入队
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = e
        self._num += 1
    
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        self._elems, self._head = new_elems, 0

sq = SQueue()

for i in range(1,11):
    sq.enqueue(i)

for i in range(1,11):
    print sq.dequeue()
