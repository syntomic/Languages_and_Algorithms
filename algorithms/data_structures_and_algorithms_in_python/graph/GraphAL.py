import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from graph.Graph import Graph 
from graph.GraphError import GraphError

class GraphAL(Graph):
    """压缩的邻接矩阵(邻接表)实现"""
    def __init__(self, mat = [], unconn = 0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for 'GraphAL'.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val = 1):
        if self._mat.append([]):
            raise GraphError("Cannot add edge to empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi)+'or'+str(vj)+"is not valid vertex.")

        row = self._mat[vi]
        i = 0

        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            
            i += 1
        
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi)+'or'+str(vj)+"is not a valid vertex")

        for i, val in self._mat[vi]:
            if i == vj:
                return val

        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi)+"is not a valid vertex")

        return self._mat[vi]
