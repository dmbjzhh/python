# -*- coding:utf-8 -*-

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key
    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)

# 基于线性表实现dict
class DictList:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        return len(self._elems)

    def search(self, key):
        for elem in self._elems:
            if elem.key == key:
                return elem.value
            else:
                return False
    
    def insert(self, key, value):
        flag = False
        for elem in self._elems:
            if elem.key == key:
                elem.value = value
                flag = True
        if flag == False:
            ass = Assoc(key, value)
            self._elems.append(ass)
        
    def delect(self, key):
        for elem in self._elems:
            if elem.key == key:
                self._elems.remove(elem)

    def values(self):
        for elem in self._elems:
            yield elem.value

    def entries(self):
        for elem in self._elems:
            yield elem

# 基于二分查找的线性字典类
class DictOrdList(DictList):
    def search(self, key):
        low, high = 0, len(self._elems)-1
        while low <= high:
            mid = low + (high - low) // 2
            if key == self._elems[mid].key:
                return self._elems[mid].value
            elif key < self._elems[mid].key:
                high = mid - 1
            else:
                low = mid + 1
        return False
    
    def insert(self, key, value):
        ass = Assoc(key, value)
        flag = False
        for i in range(0, len(self._elems)):
            if self._elems[i].key > key:
                self._elems.insert(i, ass)
                flag = True
                break
            elif self._elems[i].key == key:
                self._elems[i].value = value
                flag = True
                break
        if not flag:
            self._elems.append(ass)
    
    def delect(self, key):
        low, high = 0, len(self._elems)-1
        while low <= high:
            mid = low + (high - low) // 2
            if key == self._elems[mid].key:
                self._elems.remove(self._elems[mid])
            elif key < self._elems[mid].key:
                high = mid - 1
            else:
                low = mid + 1

from chap6_4_bitreeClass import BinTNode, BinTree
from chap5_1_stack import SStack
# 基于二叉排序树的字典类
class DictBinTree:
    def __init__(self):
        self._root = None
    
    def is_empty(self):
        return self._root is None
    
    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None
    
    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return
    
    # 中序迭代器，生成其中所有值的序列
    def values(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right
    
    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right
    
    def delect(self, key):
        p, q = None, self._root # 维持p为q的父结点
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None: # 树中没有关键码key
                return
            
        # 到这里q引用要删除结点，p是其父结点或 None(这时q是根节点)
        if q.left is None: # 如果q没有左子结点
            if p is None: # q是根结点，修改_root
                self._root = q.right
            elif q is p.left: # 根据pq关系修改p的子树引用
                p.left = q.right
            else:
                p.right = q.right
            return
        r = q.left # 找p左子树的最右结点
        while r.right is not None:
            r = r.right
        r.right = q.right
        if p is None: # q是根结点，修改_root
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def print_info(self):
        for k, v in self.entries():
            print(k, v)

def build_dicBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic

# 最佳二叉排序树类，每个结点访问概率相等的情况
class DictOptBinTree(DictBinTree):
    def __init__(self, seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.build_OPT(data, 0, len(data)-1)
    
    @staticmethod
    def build_OPT(data, start, end):
        if start > end:
            return None
        mid = (end + start) // 2
        left = DictOptBinTree.build_OPT(data, start, mid-1)
        right = DictOptBinTree.build_OPT(data, mid+1, end)
        return BinTNode(Assoc(*data[mid]), left, right)

# 最佳二叉排序树，一般情况
def build_opt_btree(wp, wq):
    '''假设wp是有n个值的list，代表着内部结点的权重，wq是有n+1个值的list，代表着n+1个外部结点的权重
    这个函数会根据wp和wq生成最佳二叉排序树'''
    num = len(wp) + 1
    if len(wq) != num:
        raise ValueError("Arguments of build_opt_btree are wrong.")
    w = [[0]*num for j in range(num)]
    c = [[0]*num for j in range(num)]
    r = [[0]*num for j in range(num)]
    for i in range(num): # 计算所有的w[i][j]
        w[i][j] = wq[i]
        for j in range(i+1, num):
            w[i][j] = w[i][j-1] + wp[j-1] + wq[j]
    for i in range(0, num-1): # 直接设置只包含一个内部结点的树
        c[i][i+1] = w[i][i+1]
        r[i][i+1] = i
    
    inf = float("inf")
    for m in range(2, num):
        # 计算包含m个内部结点的最佳树(n-m+1)棵
        for i in range(0, num-m):
            k0, j = i, i+m
            wmin = inf
            for k in range(i, j):
                # 在(i, j)里找使C[i][k] + C[k+1][j]最小的k
                if c[i][k] + c[k+1][j] < wmin:
                    wmin = c[i][k] + c[k+1][j]   
                    k0 = k
            c[i][j] = w[i][j] + wmin
            r[i][j] = k0
    
    return c, r
if __name__ == "__main__":
    # 测试线性字典类
    d1 = DictList()
    d1.insert("xy", "Dress foremost.")
    d1.insert("root", "You can call me root.")
    d1.insert("shaw", "You are my safe place.")
    print d1.search("xy")
    for i in d1.values():
        print i

    d1.insert("xy", "hhhhhhhhhh")
    print d1.search("xy")

    for i in d1.entries():
        print i

    d1.delect("xy")
    print d1.num()
    print "----------------"

    # 测试二分线性字典
    d2 = DictOrdList()
    d2.insert(3, "hhh")
    d2.insert(8, "hhhhhhhh")
    d2.insert(1, "h")
    d2.insert(4, "hhhh")
    d2.insert(2, "hh")
    d2.insert(6, "hhhhhh")

    print d2.is_empty()
    for i in d2.entries():
        print i
    
    print d2.search(4)
    d2.delect(4)
    print d2.num()
    for i in d2.values():
        print i

    print "----------------"

    # 测试二叉排序树字典类
    e = [(3, "hhh"),(8, "hhhhhhhh"),(1, "h"),(4, "hhhh"),(2, "hh"),(6, "hhhhhh")]
    d3 = build_dicBinTree(e)
    d3.print_info()