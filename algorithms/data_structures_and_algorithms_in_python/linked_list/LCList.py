from random import randint

import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from linked_list.LinkedListUnderflow import LinkedListUnderflow
from linked_list.Node import LNode 


class LCList:
    """循环单链表类"""
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p 
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p = p.next
    
if __name__ == "__main__":
    mlist1 = LCList()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    mlist1.printall()

