# -*- coding:utf-8 -*-

class SubtreeIndexError(ValueError):
    pass

def Tree(data, *subtrees):
    l = [data]
    l.extend(subtrees)
    return l

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(treem, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i+1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree

tree1 = Tree('+', 1, 2, 3)
print tree1
tree2 = Tree('*', tree1, 6, 8)
print tree2
set_subtree(tree1, 2, Tree('+', 3, 5))
print tree1

class TreeNode:
    def __init__(self, data, subs = []):
        self._data = data
        self._subtrees = list(subs)
    
    def __str__(self):
        return '[TreeNode {0} {1}]'.format(self._data, self._subtrees)

class Trees:
    def __init__(self):
        self._root = None