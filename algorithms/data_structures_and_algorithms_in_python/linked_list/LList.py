from random import randint

import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from linked_list.Node import LNode
from linked_list.LinkedListUnderflow import LinkedListUnderflow


class LList:
    """单链表类"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        
    def pop_last(self):
        if self._head is None: # 无节点，引发异常
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
        return e

    # 只能找到第一个元素
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
        
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')
        
    # 生成器，找到所有元素
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next # for x in list1.elments():  print(x)

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
        crt.elem = x
        crt = crt.next
            

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        #while rem is not None:
        p = self._head
        q = None
        while p is not None and p.elem <= rem.elem:
            q = p
            p = p.next
        if q is None:
            self._head = rem
        else:
            q.next = rem
            print(q.next.next.elem)
        x = rem
        print(q.next.next.elem)
        rem = rem.next
        print(q.next.next.elem)
        x.next = p
        print(q.next.elem)
        
        
if __name__ == "__main__":          
    mlist1 = LList()
    mlist1.prepend(3)
    mlist1.prepend(5)
    mlist1.prepend(0)
    mlist1.prepend(1)
    mlist1.printall()
    
    def print_elem_rev(llist):
        if llist._head == None:
            return "There is no element"
        elif llist._head.next == None:
            q = llist._head.elem
            return q 
        
        p = llist._head.elem
        llist._head = llist._head.next
        #print(print_elem_rev(llist))
        return p   
    
    
    print_elem_rev(mlist1)






