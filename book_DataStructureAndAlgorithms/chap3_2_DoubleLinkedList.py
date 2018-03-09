# -*- coding: utf-8 -*-

# 异常
class LinkedListUnderflow(ValueError):
    pass

# 双链表结点类
class DLNode():
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.next = next_
        self.prev = prev

# 带有尾结点引用的双链表类
class DLList():
    def __init__(self):
        self._head = None
        self.length = 0
        self._rear = None
    
    def is_empty(self):
        return self._head is None

    # 头插法
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None: # 空表
            self._rear = p
        else: # 非空表，设置prev引用
            p.next.prev = p
        self._head = p
    
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop of DLList')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None: # _head是空的时候不需要做任何事
            self._head.prev = None
        return e
    
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last of DLList')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None # 设置_head是保证is_empty正常工作
        else:
            self._rear.next = None
        return e
    
    def printall(self):
        if self.is_empty():
            return
        p = self._head
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

mlist3 = DLList()
mlist3.prepend(99)
for i in range(11, 20):
    mlist3.append(i)
mlist3.printall()
