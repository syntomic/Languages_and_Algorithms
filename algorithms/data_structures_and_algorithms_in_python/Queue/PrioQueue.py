class PrioQueueError(ValueError):
    pass

class PrioQueue:
    """list实现优先队列"""
    def __init__(self, elist=[]): # 可变参数作为默认值为危险操作！
        self._elems = list(elist) # 对实参进行拷贝
        self._elems.sort(reverse=True)

    def is_empty(self):
        return not self._elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]

    def enqueue(self, e):
        """插入元素，需要找到正确的插入位置"""
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] < e:
                i -= 1
            else:
                break

        self._elems.insert(i+1, e)

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")

        return self._elems.pop()

if __name__ == "__main__":
    prio_queue = PrioQueue()
    prio_queue.enqueue(5)
    prio_queue.enqueue(7)
    prio_queue.enqueue(6)

    prio_queue.dequeue()
    
    print(prio_queue.peek())