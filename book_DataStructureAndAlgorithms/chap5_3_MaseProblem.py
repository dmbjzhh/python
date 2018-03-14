# -*- coding: utf-8 -*- 
from chap5_1_stack import SStack
# 迷宫求解问题

# 得到相邻四个位置应加的数对，对应东西南北
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def mark(maze, pos): # 给迷宫maze的位置pos标2表示到过了
    maze[pos[0], pos[1]] = 2

def passable(maze, pos): # 检查迷宫maze的位置pos是否可行
    return maze[pos[0], pos[1]] == 0

# 递归实现
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end: # 已到达出口
        print(pos) # 输出这个位置
        return True # 成功结束
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        # 考虑下一个可能方向
        if passable(maze, nextp): # 不可行的相邻位置不管
            if find_path(maze, nextp, end): # 从nextp可达出口
                print(pos) # 输出这个位置
                return True
    return False

# 迷宫的回溯法求解——栈
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0)) # 入口和方向0的序对入栈
    while not st.is_empty(): # 走不通时回退
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            pass
