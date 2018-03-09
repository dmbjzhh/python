# -*- coding:utf-8 -*-

from __future__ import print_function

# 异常
class LinkedListUnderflow(ValueError):
    pass

# 单链表节点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
    
'''
# 测试单链表节点类
llist1 = LNode(1)
p = llist1

for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1

while p is not None:
    print(p.elem)
    p = p.next
'''

# 单链表类
class LList:
    def __init__(self):
        self._head = None
        self.length = 0
    
    # 链表长度
    def __len__(self):
        return self.length

    # 判空
    def is_empty(self):
        return self._head is None

    # 前端插入
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self.length += 1
    
    # 后端插入
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        self.length += 1

    # 插入指定位置
    def insert_data(self, elem, index):
        if index > self.length:
            raise LinkedListUnderflow('in insert_data')
        p = self._head
        if index == 1:
            self.prepend(elem)
        for i in range(1, index-1):
            p = p.next
        n = LNode(elem)
        n.next = p.next
        p.next = n
        self.length += 1

    # 弹出表头元素
    def pop(self):
        if self._head == None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        self.length -= 1
        return e

    # 弹出表尾元素
    def pop_last(self):
        if self._head is None: # 空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next == None: # 表中只有一个元素
            e = p.elem
            self._head = None
            self.length -= 1
            return e
        while p.next.next is not None: # 直到p.next是最后节点
            p = p.next
        e = p.next.elem
        p.next = None
        self.length -= 1
        return e
    
    # 删除指定位置的元素
    def del_index(self, index):
        if index > self.length:
            raise LinkedListUnderflow('in del_index')
        if index == 1:
            self.pop()
        p = self._head
        for i in range(1, index-1):
            p = p.next
        e = p.next.elem
        p.next =  p.next.next
        self.length -= 1
        return e

    # 查找指定位置的表元素
    def find_data(self, index):
        if index > self.length:
            raise LinkedListUnderflow('in find_data')
        p = self._head
        for i in range(1, index):
            p = p.next
        return p.elem
    
    # 查找指定元素的位置
    def find_index(self, data):
        if self._head is None:
            raise LinkedListUnderflow('in find_index')
        p = self._head
        count = 1
        while p.next is not None:
            if data == p.elem:
                return count
            else:
                count += 1

    # 打印所有表元素
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')
    


    # 定义遍历函数
    def for_each(self, func):
        p = self._head
        while p is not None:
            p.elem = func(p.elem) # func的实参是可以作用于表元素的操作函数
            p = p.next
            
    # 定义迭代器
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next
    
    # 筛选生成器
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next
    
    # 删除链表
    def del_list(self):
        self._head = None
        self.length = 0
    
l = LList()
# 头插法生成链表
for i in range(1, 11):
    l.prepend(i)

# 测试插入表头
l.prepend(3)

# 测试插入111到第一个位置,插入12到第3个位置
l.insert_data(111, 1)
l.insert_data(12, 3)

# 测试删除第三个位置的12，删除第一个位置的111
print(l.del_index(3))
print(l.del_index(1))

# 测试链表长度
print(len(l))

# 打印所有元素
l.printall()

# 查找第三个元素
print(l.find_data(3))

# 查找元素7的位置
print(l.find_data(7))

# 测试遍历函数
l.for_each(lambda x: x*x)
l.printall()

# 测试迭代器
for x in l.elements():
    print(x)

# 测试筛选生成器，打印多个符合条件的元素
def pr(y):
    if y == 9:
        return y
for x in l.filter(pr):
    print(x)

# 单链表的简单改进版本——带有尾结点引用的单链表，因为之前的单链表尾端加入元素操作效率低
class LList_improve(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None # 尾指针
    
    # 头插法的重新定义
    def prepend(self, elem):
        if self._head is None: # 是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
    # 尾插法的重新定义
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem) # next为空，因为是最后一个结点
            self._rear = self._rear.next

    # pop无需重新定义，因为同一使用_head为None判断空表有关

    # 弹出末元素的操作
    def pop_last(self):
        if self._head is None: # 是空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None: # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None: # 直到p.next是最后结点
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

# 测试带尾指针的单链表
print('-------------')
mlist1 = LList_improve()
mlist1.prepend(99)
for i in range(11, 20):
    mlist1.append(i)
mlist1.printall()

for x in mlist1.filter(lambda y: y % 2 == 0):
    print(x)

# 循环单链表的类，最后一个结点指向不为空，而是指向头结点
# 选择尾指针而不是头指针，访问头尾会更方便
class LCList:
    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None

    # 前端插入
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 尾端插入    
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next # 相当于先头插了，然后再把尾指针移过去，反正是个循环，想怎么指都行咯
    
    # 前端弹出
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop of LCList')
        p = self._rear.next
        if self._rear is p: # 只有一个结点
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem
    
    # 输出表元素
    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

# 测试循环单链表
print('-------------')
mlist2 = LCList()
mlist2.prepend(99)
for i in range(11, 20):
    mlist2.append(i)
mlist2.printall()
