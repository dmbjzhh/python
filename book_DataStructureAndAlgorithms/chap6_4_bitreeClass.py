# -*- coding:utf-8 -*-

from chap5_2_queue import SQueue
from chap6_2_priorityQueue import PrioQue_heap

# 链接实现，而不是之前的基于list或tuple实现

# 二叉树结点类
class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


# 统计树中结点个数
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)
   
# 假设结点中保存数值，求这种二叉树里所有数值的和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

# 递归遍历算法

# 前序遍历
def print_BinTNodes_pre(t):
    if t is None:
        print '^',
        return None
    print '(' + str(t.data),
    print_BinTNodes_pre(t.left)
    print_BinTNodes_pre(t.right)
    print ')',

# 中序遍历
def print_BinTNodes_mid(t):
    if t is None:
        print '^',
        return None
    print '(',
    print_BinTNodes_mid(t.left)
    print str(t.data),
    print_BinTNodes_mid(t.right)
    print ')',

# 后序遍历
def print_BinTNodes_post(t):
    if t is None:
        print '^',
        return None
    print '(',
    print_BinTNodes_post(t.left)
    print_BinTNodes_post(t.right)
    print str(t.data),
    print ')',

# 层次遍历
def levelorder(t):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None: # 弹出为空树直接跳过
            print '^',
            continue
        print n.data,
        qu.enqueue(n.left)
        qu.enqueue(n.right)

# 非递归的先序遍历，用栈
from chap5_1_stack import SStack

def preorder_nonrec(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None: # 沿着左分支下行
            s.push(t.right)
            print t.data, # 把print改成yield，就成了一个二叉树迭代器
            t = t.left
        t = s.pop()

# 非递归的后序遍历
# 总的来说，内层循环会先找到当前子树的最下最左结点，将入栈后终止；
# 如果访问的是其父的左子结点，则直接跳转到其右兄弟结点继续
# 如果被处理的是其父的右子结点，设t为None将强迫外层循环的下次迭代弹出并访问更上一层的结点
def postorder_nonrec(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None: # 下行循环，直到栈顶的两子树空
            s.push(t)
            t = t.left if t.left is not None else t.right # 能往左就往左，否则向右一步
        
        t = s.pop() # 栈顶是应该访问的结点
        print t.data,
        if not s.is_empty() and s.top().left == t: # 栈不空且当前结点是栈顶的左子结点
            t = s.top().right
        else:
            t = None # 没有右子树或右子树遍历完毕，强迫退栈

class BinTree:
    def __init__(self):
        self._root = None
    
    def is_empty(self):
        return self._root is None
    
    def root(self):
        return self._root
    
    def leftchild(self):
        return self._root.left
    
    def rightchild(self):
        return self._root.right
    
    def set_root(self, rootnode):
        self._root = rootnode
    
    def set_left(self, leftchild):
        self._root.left = leftchild
    
    def set_right(self, rightchild):
        self._root.right = rightchild
    
    def preorder_elements(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()

# 二叉树的应用——哈夫曼树

class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data
    
class HuffmanPrioQ(PrioQue_heap):
    def number(self):
        return len(self._elems)

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()

if __name__ == "__main__":
    # 测试前中后序遍历
    t = BinTNode(1, BinTNode(2,None,BinTNode(5)), BinTNode(3))
    print_BinTNodes_pre(t)
    print ''
    print_BinTNodes_mid(t)
    print ''
    print_BinTNodes_post(t)
    # 测试层次遍历
    print ''
    levelorder(t)
    print ''
    # 测试非递归先序遍历
    preorder_nonrec(t)
    # 测试非递归后序遍历
    print ''
    postorder_nonrec(t)
    print ''
    # 测试二叉树类
    bt = BinTree()
    bt.set_root(BinTNode(1, BinTNode(2,None,BinTNode(5)), BinTNode(3)))

    for i in bt.preorder_elements():
        print i,
    # 测试哈夫曼树
    print_BinTNodes_pre(HuffmanTree([2,2,5,10,4,3,7]))



