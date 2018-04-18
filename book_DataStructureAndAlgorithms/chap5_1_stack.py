# -*- coding:utf-8 -*-

class StackUnderflow(ValueError): # 栈下溢，空栈访问
    pass

# 栈的顺序表实现
# 用list对象 _elems存储栈中元素
# 所有栈操作都映射到list操作
class SStack():
    def __init__(self):
        self._elems = []
    
    def is_empty(self):
        return self._elems == []
    
    # 取栈顶元素但不弹出
    def top(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]
    
    # 压栈
    def push(self, elem):
        self._elems.append(elem)
    
    # 出栈
    def pop(self):
        if self._elems == []:
            raise StackUnderflow('in SStack.pop()')
        return self._elems.pop()


# 栈的链接表实现，用LNode作为结点

class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):
        self._top = None
    
    def is_empty(self):
        return self._top is None
    
    def top(self):
        if self._top is None:
            raise StackUnderflow('in LStack.top()')
        return self._top.elem
    
    def push(self, elem):
        self._top = LNode(elem, self._top)
    
    def pop(self):
        if self._top is None:
            raise StackUnderflow('in LStack.pop()')
        p = self._top
        self._top = p.next
        return p.elem

# 栈的应用--反转链表
def reverse_list(args):
    str3 = SStack()
    for x in args:
        str3.push(x)
    new_list = []
    while not str3.is_empty():
        new_list.append(str3.pop())
    return new_list

# 栈的应用--括号匹配

def check_parens(text):
    '''括号配对检查函数，text是被检查的正文串'''
    parens = '()[]{}' # 所有括号字符
    open_parens = '([{' # 开括号字符
    opposite = {')':'(', ']':'[', '}':'{'} # 表示配对关系的字典

    def parentheses(text):
        '''括号生成器，每次调用返回text里的下一括号及其位置'''
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    
    st = SStack() # 保存括号的栈
    for pr, i in parentheses(text): # 对text里各括号和位置迭代
        if pr in open_parens:
            st.push(pr)
        # 书上的代码，在只出现一个左括号的时候不会报错，在只出现一个右括号的时候，会出现空栈访问的异常
        # elif st.pop() != opposite[pr]: # 不匹配就是失败，退出
        #     print 'Unmatching is found at {0} for {1}'.format(i, pr)
        #     return False
        # else: # 这是一次括号配对成功，什么也不做，继续
        #     pass
        else:
            try:
                e = st.pop()
            except:
                print 'Unmatching is found at {0} for {1}'.format(i, pr)
                return False
            else:
                if e != opposite[pr]:
                    print 'Unmatching is found at {0} for {1}'.format(i, pr)
                    return False
                else: # 这是一次括号配对成功，什么也不做，继续
                    pass
    if st.is_empty():
        print 'All parentheses are correctly matched.'
        return True
    else:
        print 'Unmatching is found at {0} for {1}'.format(i, pr)
        return False

# 栈的应用--后缀表达式的计算

# 定义一个函数把表示表达式的字符串转化为项的表，要求后缀表达式每个元素之间有空格
def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2: # x必为运算符，如果栈中元素不够两个就引发异常
            raise SyntaxError('Short of operand(s).')
        a = st.pop()
        b = st.pop()
        
        if x == '+':
            c = b + a
        elif x == '*':
            c = b * a
        elif x == '-':
            c = b - a
        elif x == '/':
            c = b / a
        else: # 其实else分支不会出现
            break
        
        st.push(c)
    
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError('Extra operand(s).')

# 和用户交互用的主函数
def suffix_exp_calculator():
    while True:
        try:
            line = input('Suffix Expression: ')
            if line == 'end': return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print 'Error: ', type(ex), ex.args

#print suffix_exp_evaluator('3 5 - 6 17 4 * + * 3 /')
# suffix_exp_calculator()

# 栈的应用--中缀转后缀
# 思路：遇到运算对象直接输出；左括号总进栈，右括号特殊处理；遇到运算符时与栈顶元素比较并根据情况处理，最后将运算符进栈

priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5} # 设置优先级
infix_operators = '+-*/()'

# 生成器函数tokens逐一产生输入表达式的各个项，line是一个中缀表达式
def tokens(line):
    '''生成器函数，逐一生成line中的各个项，项是浮点数或运算符，
    本函数不能处理一元运算符，也不能处理带符号的浮点数'''
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace(): # 遇空格跳过
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators: # 运算符的情况
            yield line[i]
            i += 1
            continue
        
        j = i + 1
        while(j < llen and not line[j].isspace() and line[j] not in infix_operators):
            if((line[j] == 'e' or line[j] == 'E') and j+1 < llen and line[j+1] == '-'): # 处理负指数
                j += 1
            j += 1
        yield line[i:j] # 生成运算对象子串
        i = j
def trans_infix_suffix(line):
    st = SStack()
    exp = []

    for x in tokens(line):
        if x not in infix_operators: # 不是符号而是运算对象的话，直接送出
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x == ')': # 处理右括号的分支
            while not st.is_empty() and st.top() != '(': # 当没遇到左括号时，不停弹出栈中的运算符
                exp.append(st.pop())
            if st.is_empty(): # 没找到左括号就是不配对
                raise SyntaxError("Missing '('.")
            st.pop() # 弹出左括号，右括号也不进栈
        else:
            while (not st.is_empty() and priority[st.top()] >= priority[x]): # 当栈中不为空，而且下一个运算符(x)的优先级不高于本运算符时
                exp.append(st.pop()) # 这时才能把本运算符送入后缀表达式
            st.push(x) # 算术运算符进栈
    
    while not st.is_empty(): # 送出栈中剩下的运算符
        if st.top() == '(': # 如果还有左括号就是不匹配
            raise SyntaxError('Extra "(".')
        exp.append(st.pop())
    
    return exp

def test_trans_infix_suffix(s):
    print s
    print trans_infix_suffix(s)
    print 'value: ', suf_exp_evaluator(trans_infix_suffix(s))


# 栈的应用--递归，求阶乘

# 递归方法
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


# 非递归方法
def norec_fact(n):
    res = 1
    st = SStack()
    while n > 0:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res


# 背包问题
# 问题描述：一个背包可以放入重量为weight的物品，现有n件物品的集合S，其中物品的重量分别为w0,w1...wn-1
# 能否从中选出若干件物品，重量之和刚好为weight

# 递归解决方案：n个物品的背包问题可以归结为两个n-1件物品的背包问题，一个针对同样重量但物品数量减一，另一个重量减少，物品种类也减一
# 任意一个子问题有解，原问题就有解

def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1): # 没有物品可用
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print('item ' + str(n) + ':', wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False


# 测试合集
if __name__ == '__main__':
    # 测试顺序栈类
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())

    # 测试链接栈类
    st2 = LStack()
    st2.push(2)
    st2.push(1)
    while not st2.is_empty():
        print(st2.pop())

    # 测试反转链表
    l = [1,2,3,4,5,6]
    print reverse_list(l)

    # 测试括号匹配
    p1 = '(a+n){}[]{}(adsd)'
    print check_parens(p1)

    p2 = '{}('
    print check_parens(p2)

    p3 = '{})'
    print check_parens(p3)

    # 测试中缀转后缀
    s1 = '(3-5) * (6+17 * 4)/2'
    test_trans_infix_suffix(s1)

    # 测试递归和非递归求阶乘
    print fact(5)
    print norec_fact(5)

    # 测试背包问题
    print knap_rec(5, [3,1,2], 3)
