import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Queue.PrioQueue import PrioQueue

def dijkstra_shortest_paths(graph, v0):
    """Dijkstra算法"""
    vnum = graph.vertex_num()

    assert 0 <= v0 < vnum

    paths = [None] * vnum
    count = 0 
    cands = PrioQueue([(0, v0, v0)])

    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()

        if paths[vmin]:
            continue

        paths[vmin] = (u, plen)

        for v, w in graph.out_edges(vmin):
            if not paths(v):
                cands.enqueue((plen + w, vmin, v)) 
                
        count += 1

    return paths

def all_shortest_paths(graph):
    """Floyd算法"""
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
    nvertex = [[-1 if a[i][j] == float('inf') else j for j in range(vnum)] for i in range(vnum)]

    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]

    return (a, nvertex)


