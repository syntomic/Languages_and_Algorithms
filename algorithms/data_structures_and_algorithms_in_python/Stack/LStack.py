import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from linked_list import Node

from Stack.StackUnderflow import StackUnderflow

class LStack():
    """
    基于链接表技术实现的栈类，用LNode作为节点
    """
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = Node.LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem

if __name__ == "__main__":
    st1 = LStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())