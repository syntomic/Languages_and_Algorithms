import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Queue.QueueUnderflow import QueueUnderflow

class SQueue():
    """队列的list实现"""
    def __init__(self, init_len = 8):
        self._len = init_len        # 存储区长度
        self._elems = [0]*init_len  # 元素存储
        self._head = 0              # 表头元素下标
        self._num = 0               # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        """取得队列首元素"""
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num +=1

    def __extend(self):
        """加倍存储区长度"""
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

if __name__ == "__main__":
    qu = SQueue()
    qu.peek()
        

