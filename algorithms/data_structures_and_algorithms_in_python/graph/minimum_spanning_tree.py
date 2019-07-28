import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Tree.prio_queue import PrioQueue

def Kruskal(graph):
    """最小生成树的Kruskal算法"""
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []

    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))

    edges.sort()

    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj), w)

            if len(mst) == vnum - 1:
                break
            
            rep, orep = reps[vi], reps[vj]

            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] == rep

    return mst

def Prim(graph):
    """"Prim算法"""
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQueue([(0, 0, 0)])
    count = 0

    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        
        mst[v] = ((u, v), w)
        count += 1

        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))

        return mst

## 可以改进

    