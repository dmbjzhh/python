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