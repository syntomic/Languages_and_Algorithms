import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Stack.SStack import SStack


def DFS_graph(graph, v0):
    """"深度优先的非递归算法"""
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))

    while not st.is_empty():
        i, edges = st.pop()

        if i < len(edges):
            v, e = edges[i] # pylint: disable=unused-variable
            st.push((i+1, edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))

    return DFS_seq