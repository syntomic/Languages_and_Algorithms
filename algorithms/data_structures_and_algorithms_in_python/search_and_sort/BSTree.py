import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from save_and_search.association import Assoc #pylint: disable=import-error
from Tree.BinTNode import BinTNode #pylint: disable=import-error, no-name-in-module
from Stack.SStack import SStack #pylint: disable=import-error

## 二叉排序树的检索
def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None


class DictBinTree:
    """二叉排序树字典类"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def bt_search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                
                bt = bt.left
            
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                
                bt = bt.right
            
            else:
                bt.data.value = value
                return
    
    def values(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            
            t = s.pop()

            yield t.data.value

            t = t.right

    def entries(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            
            t = s.pop()

            yield t.data.key, t.data.value

            t = t.right

    def delete(self, key):
        p, q = None, self._root   # 维持p为q的父节点
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right

            if q is None:
                return            # 树中没有关键码 

            if q.left is None:
                if p is None:
                    self._root = q.right
                elif q is p.left:
                    p.left = q.right
                else:
                    p.right = q.right
                return

            r = q.left
            while r.right is not None:
                r = r.right
            
            r.right = q.right
            if p is None:
                self._root = q.left

            r.right = q.right

            if p is None:
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left

    def print(self):
        for k, v in self.entries():
            print(k, v)

        
def build_dictBinTree(entries):
    """基于一系列数据项建立起一棵二叉排序树"""
    dict_ = DictBinTree()
    for k, v in entries:
        dict_.insert(k, v)

    return dict_