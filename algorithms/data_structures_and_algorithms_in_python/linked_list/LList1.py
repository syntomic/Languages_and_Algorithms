from random import randint

import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from linked_list.LList import LList
from linked_list.Node import LNode
from linked_list.LinkedListUnderflow import LinkedListUnderflow


class LList1(LList):
    """带有尾节点引用的单链表类"""
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
    # 继承保持一致性
        #self._head = LNode(elem, self._head)
        #if self._rear is None:
            #self._rear = self._head
            
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

if __name__ == "__main__":
    mlist1 = LList1()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    for x in mlist1.filter(lambda y : y % 2 == 0 ):
        print(x)
