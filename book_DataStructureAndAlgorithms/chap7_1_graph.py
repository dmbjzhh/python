# -*- coding:utf-8 -*-

class GraphError(ValueError):
    pass

# 邻接矩阵的实现
class Graph: # 基本图类，采用邻接矩阵表示，mat是邻接矩阵list套list，unconn是无关联情况的特殊值
    def __init__(self, mat, unconn=0):
        vnum = len(mat) # 顶点个数
        for x in mat:
            if len(x) != vnum: # 检查是否为方阵
                raise ValueError('Argument for "Graph".')
        self._mat = [mat[i][:] for i in range(vnum)] # 将mat数组拷贝一份
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v): # 检查下标合法性
        return 0 > v or v >= self._vnum
    
    def add_vertex(self):
        raise GraphError('Adj-Matrix does not support add_vertex.')
    
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('vi or vj is not a valid vertex.')
        self._mat[vi][vj] = val
    
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('vi or vj is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError('vi is not a valid vertex.')
        return self._out_edges(self._mat[vi], self._unconn) 

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges
    
    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nUnconnected symbol: " + str(self._unconn)


g = Graph([[0,1,0,1,1],[1,0,1,0,1],[0,1,0,0,0],[1,0,0,0,1],[1,1,0,1,0]])

print g
print g.out_edges(1)

# g.add_edge(0,2)
# print g

# 邻接表的实现，支持增加新结点
class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0): # mat空表作为默认值，支持从空表出发构造所需图对象
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argument for GraphAL.')
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        print self._mat
        self._vnum = vnum
        self._unconn = unconn

    
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1
    
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('vi or vj is not valid vertex')
        
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj: # 修改mat[vi][vj]的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj: # 原来没有到vj的边，退出循环后加入边
                break
        
        i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('vi or vj is not a valid vertex.')
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn
    
    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError('vi is not a valid vertex.')
        return self._mat[vi]

print '---------------------------'
gl = GraphAL([[0,1,0],[1,0,1],[0,1,0]])
print gl
gl.add_vertex()
print gl
gl.add_edge(3, 1)
print gl

# 图的深度优先非递归算法
from chap5_1_stack import SStack
def DFS_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum # visited记录已访问顶点
    visited[v0] = 1
    DFS_seq = [v0] # DFS_seq 记录遍历序列
    st = SStack()
    st.push((0, graph.out_edges(v0))) # 入栈(i, edges)说明下次应该访问边edge[i]
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i+1, edges)) # 下次回来将访问edges[i+1]
            if not visited[v]: # v未访问，访问并记录其可达顶点
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq

print DFS_graph(g, 0)

span_forest=[]

# 构造DFS生成树：递归算法，不懂啊，跑这个看起来好像不是对的
def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    global span_forest
    span_forest = [None] * vnum

    def dfs(graph, v): # 递归遍历函数，在递归中记录经由边
        global span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)
    
    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest
print DFS_span_forest(g)

# Kruskal算法
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)] # 代表元，可以常数时间判断两个顶点是否连通
    mst, edges = [], []
    for vi in range(vnum): # 所有的边加入表edges
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort() # 边按权值排序，O(n log n)的时间
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]: # 两端点属于不同的连通分量
            mst.append(((vi, vj), w)) # 记录此边
            if len(mst) == vnum - 1: # v-1条边，构造完成
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum): # 合并连通分量，统一代表元
                if reps[i] == orep:
                    reps[i] = rep
    return mst

print Kruskal(g)

# Prim算法
from chap6_2_priorityQueue import PrioQue_heap
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQue_heap([(0,0,0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue() # 取当时的最短边
        if mst[v]:
            continue # 邻接点v已经在mst里，继续
        mst[v] = ((u,v), w) # 记录新的MST边和顶点
        count += 1
        for vi, w in graph.out_edges(v): # 考虑v的邻接顶点vi
            if not mst[vi]: # 如果vi不在mst中，则这条边是候选边
                cands.enqueue((w, v, vi))
    return mst
print Prim(g)

gd = Graph([[0,0,10,0,30,100],[0,0,5,0,0,0],[0,0,0,50,0,0],[0,0,0,0,0,10],[0,0,0,20,0,60],[0,0,0,0,0,0]])

# Dijkstra算法求解单源点最短路径
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 <= vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQue_heap([(0, v0, v0)]) # 初始队列
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue() # 取其路径最短顶点
        if paths[vmin]: # 如果最短路径已知则继续
            continue
        paths[vmin] = (u, plen) # 记录新确定的最短路径
        for v, w in graph.out_edges(vmin): # 考察经由新U顶点的路径
            if not paths[v]: # 是到尚未知最短路径的顶点的路径，记录它
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths

print dijkstra_shortest_paths(gd, 0)

# Floyd算法
inf = float("inf")
gf = Graph([[inf,inf,10,inf,30,100],[inf,inf,5,inf,inf,inf],[inf,inf,inf,50,inf,inf],[inf,inf,inf,inf,inf,10],[inf,inf,inf,20,inf,60],[inf,inf,inf,inf,inf,inf]])

def all_shortest_path(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i,j) for j in range(vnum)] for i in range(vnum)] # graph复制一份
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j] # a记录已知最短路径长度
                    nvertex[i][j] = nvertex[i][k] # nvertex记录已知最短路径上的下一顶点    
    return (a, nvertex)

print all_shortest_path(gf)

# 拓扑排序
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0] * vnum, []
    zerov = -1
    for vi in range(vnum): # 建立初始的入度表
        for v, w in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum): # 建立初始的0度表
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1: # 不存在拓扑序列
            return False
        vi = zerov # 从0度表弹出顶点vi
        zerov = indegree[zerov]
        toposeq.append(vi) # 把一个vi加入拓扑序列
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1 # 入度表减一
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq

gt = Graph([[0,1,1,1,0,0],[0,0,0,0,0,0],[0,1,0,0,1,0],[0,0,0,0,1,0],[0,0,0,0,0,0],[0,0,0,1,1,0]])
print toposort(gt)

# 关键路径
def critical_path(graph):
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0] * vnum
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]: # 事件j更晚结束？
                    ee[j] = ee[i] + w
        print("ee: ", ee)
        return ee
    
    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast] * vnum
        for k in range(vnum-2, -1, -1): # 逆拓扑排序
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]: # 事件i应更早开始？
                    le[i] = le[j] - w
        print("le: ",le)
        return le
    
    def crt_paths(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w: # 关键活动
                    crt_actions.append((i, j, ee[i]))
        return crt_actions
    
    toposeq = toposort(graph)
    if not toposeq: # 不存在拓扑序列，失败结束
        return False
    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])
    return crt_paths(vnum, graph, ee, le)

gc = Graph([[0,3,2,0,0,0],[0,0,0,2,3,0],[0,0,0,4,0,3],[0,0,0,0,0,2],[0,0,0,0,0,1],[0,0,0,0,0,0]])
print critical_path(gc)