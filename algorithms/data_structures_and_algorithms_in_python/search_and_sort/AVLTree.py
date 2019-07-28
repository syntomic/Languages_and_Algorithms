import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from save_and_search.association import Assoc 
from save_and_search.BSTree import DictBinTree #pylint: disable=import-error
from Tree.BinTNode import BinTNode #pylint: disable=import-error, no-name-in-module

class AVLNode(BinTNode):
    """平衡二叉树结点类"""
    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0

class DictAVL(DictBinTree):
    """平衡二叉树字典类"""
    def __init__(self):
        DictBinTree.__init__(self)

    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0

        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = -1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c

    
    def insert(self, key, value):
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return

        pa = q = None

        while p is not None:
            if key == p.data.key:
                p.data.value
                return
            if p.bf != 0:
                pa, a = q, p
            
            q = p

            if key < p.data.key:
                p = p.left
            else:
                p = p.right

        node = AVLNode(Assoc(key, value))
        if key < q.data.key:
            q.left = node
        else:
            q.right = node

        if key < a.data.key:
            p = b = a.left
            d = 1
        else:
            p = b = a.right
            d = -1

        while p != node:
            if key < p.data.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right

        if a.bf == 0:
            a.bf = d
            return 
        
        if a.bf == -d:
            a.bf = 0
            return

        if d == 1:
            if b.bf == 1:
                b = DictAVL.LL(a, b)
            else:
                b = DictAVL.LR(a, b)
        else:
            if b.bf == -1:
                b = DictAVL.RR(a, b)
            else:
                b = DictAVL.RL(a, b)

        if pa is None:
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b
 