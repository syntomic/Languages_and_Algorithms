import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Tree.BinTNode import BinTNode #pylint: disable=import-error, no-name-in-module
from Tree.prio_queue import PrioQueue #pylint: disable=import-error, no-name-in-module



class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)


def HuffmanTree(weights):
    """基于weights的哈夫曼树"""
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    
    return trees.dequeue()
