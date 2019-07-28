import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Stack.StackUnderflow import StackUnderflow

class SStack():
    """
    基于顺序表技术实现的栈类，用list对象_elems储存栈中元素，所有栈操作都映射到list操作
    """
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)
    
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

if __name__ == "__main__":
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
