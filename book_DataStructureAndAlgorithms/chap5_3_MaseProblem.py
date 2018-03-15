# -*- coding: utf-8 -*- 
from chap5_1_stack import SStack
from chap5_2_queue import SQueue
# 迷宫求解问题

maze1 = [[0,1,1,1,1],
        [0,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0]]

maze2 = [[0,1,1,1,1],
        [0,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0]]

maze3 = [[0,1,1,1,1],
        [0,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0]]

# 得到相邻四个位置应加的数对，对应东西南北
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def mark(maze, pos): # 给迷宫maze的位置pos标2表示到过了
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos): # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0

# 递归实现，因为是递归调用，程序输出时候会倒序输出路径
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end: # 已到达出口
        print(pos) # 输出这个位置
        return True # 成功结束
    for i in range(4): # 注意，因为总是先探索右边位置，到边界的时候会报错，所以加个判断条件
        if pos[0] + dirs[i][0] >= len(maze) or pos[1] + dirs[i][1] >= len(maze) or pos[0] + dirs[i][0] < 0 or pos[1] + dirs[i][1] < 0:
            print 'at the edge'
            continue
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        # 考虑下一个可能方向
        if passable(maze, nextp): # 不可行的相邻位置不管
            if find_path(maze, nextp, end): # 从nextp可达出口
                print(pos) # 输出这个位置
                return True
    return False

def print_path(end, pos, st):
    print end
    print pos
    while not st.is_empty():
        print st.pop()[0]

# 迷宫的回溯法求解——基于栈
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return True
    st = SStack()
    mark(maze, start)
    st.push((start, 0)) # 入口和方向0的序对入栈
    while not st.is_empty(): # 走不通时回退
        pos, nxt = st.pop() # 取栈顶及其探查方向
        for i in range(nxt, 4): # 依次检查未探查方向，nxt表示回溯到该位置的下一探索方向，四个方向分别编码为0123
            if pos[0] + dirs[i][0] >= len(maze) or pos[1] + dirs[i][1] >= len(maze) or pos[0] + dirs[i][0] < 0 or pos[1] + dirs[i][1] < 0:
                print 'at the edge'
                continue 
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1]) # 算出下一位置
            if nextp == end: # 到达出口，打印路径
                print_path(end, pos, st)
                return True
            if passable(maze, nextp): # 遇到未探查的新位置
                st.push((pos, i+1)) # 原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp,0)) # 新位置入栈
                break # 退出内层循环，下次迭代将以新栈顶为当前位置继续  
    print 'No path found.'
    return False

# 迷宫不回溯求解——基于队列
# 队列中保存的位置和路径无关，只能判断能不能找到出口，如果需要输出路径，需要在搜索中另行记录有关信息
def maze_solver_queue(maze, start, end):
    if start == end:
        print 'Path finds.'
        return True
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            if pos[0] + dirs[i][0] >= len(maze) or pos[1] + dirs[i][1] >= len(maze) or pos[0] + dirs[i][0] < 0 or pos[1] + dirs[i][1] < 0:
                print 'at the edge'
                continue 
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print 'Path finds.'
                    return True
                mark(maze, nextp)
                qu.enqueue(nextp)
    print 'No path.'

print find_path(maze1, (0,0), (4,4))

print maze_solver(maze2, (0,0), (4,4))

print maze_solver_queue(maze3, (0,0), (4,4))
