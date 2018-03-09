# -*- coding:utf-8 -*-

'''
一个简单的正则表达式处理程序
'''

def match(re, text):
    def match_here(re, i, text, j):
        '''检查从text[j]开始的目标串是否与re[i]开始的模式匹配'''
        while True:
            if i == rlen: # 表示模式串已经处理完了，说明找到了匹配
                return True
            if re[i] == '$': # 如果模式串和目标串都结束了就是匹配成功
                return i+1 == rlen and j == tlen
            if i+1 < rlen and re[i+1] == '*': # 有*号就调用处理该符号的函数，跳过0个或多个re[i]
                return match_star(re[i], re, i+2, text, j)
            if j == tlen or (re[i] != '.' and re[i] != text[j]): # 匹配失败的情况
                return False
            i, j = i+1, j+1
        
    def match_star(c, re, i, text,j):
        '''在text里跳过0个或多个c后检查匹配'''
        for n in range(j, tlen):
            if match_here(re, i, text, n): # 0个的情况，从目标串中剩下的每个位置开始检查是否能和*号之后的模式串匹配
                return True
            if text[n] != c and c != '.': # 检查1个或多个的情况，如果重复就跳过重复字符并继续
                break
        return False
    
    rlen, tlen = len(re), len(text)
    if re[0] == '^': # 先考虑开头是否为'^'，是的话就只考虑与目标串前缀的匹配，否则就会对text中的各个位置调用match_here 
        if match_here(re, 1, text, 0):
            return 1
    for n in range(tlen):
        if match_here(re, 0, text, n):
            return n
    return -1 # 表示无匹配

a = 'abcdefg'
b = 'fg$'
print(match(b, a))