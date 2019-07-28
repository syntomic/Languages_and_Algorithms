import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from save_and_search.association import Assoc #pylint: disable=import-error
from save_and_search.BSTree import DictBinTree #pylint: disable=import-error, no-name-in-module
from Tree.BinTNode import BinTNode #pylint: disable=import-error, no-name-in-module

class DictOptBinTree(DictBinTree):
    """最佳二叉排序树类"""
    def __init__(self, seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data, 0, len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        """简单情况：检索概率相同"""
        if start > end:
            return None
        
        mid = (start+end) // 2
        left = DictOptBinTree.buildOBT(data, start, mid-1)
        right = DictOptBinTree.buildOBT(data, mid+1, end)
        return BinTNode(Assoc(*data[mid]), left, right)

    @staticmethod
    def build_opt_btree(wp, wq):
        """
        general case: builds the optimal binary searching tree from wp and wq
        params：
            wp:list[int] list of n values representing weights of internal nodes
            wq:list[int] list of n+1 values representing weights of n+1 external nodes
        """
        num = len(wp) + 1
        if len(wq) != num:
            raise ValueError("Arguments of build_opt_btree are wrong")

        w, c, r = [[[0]*num for j in range(num)]] * 3

        for i in range(num):
            w[i][j] = wq[i]
            for j in range(i+1, num):
                w[i][j] = w[i][j-1] + wp[j-1] + wq[j]

        for i in range(num-1):
            c[i][i+1] = w[i][i+1]
            r[i][i+1] = i

        for m in range(2, num):
            for i in range(num-m):
                k0, j = i, i+m
                wmin = float("inf")
            
            for k in range(i, j):
                if c[i][k] + c[k+1][j] < wmin:
                    wmin = c[i][k] + c[k+1][j]
                    k0 = k

            c[i][j] = w[i][j] + wmin
            r[i][j] = k0

        return c, r
