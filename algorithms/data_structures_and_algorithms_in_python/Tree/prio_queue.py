class PrioQueueError(ValueError):
    pass

class PrioQueue:
    """用堆实现优先队列"""
    def __init__(self, elist=[]): # 可变参数作为默认值为危险操作！
        self._elems = list(elist) # 对实参进行拷贝，排除共享
        if elist:
            self.buildhead()

    def is_empty(self):
        return not self._elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None) # 添加一个虚拟元素
        self.siftup(e, len(self._elems) - 1)
    
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1              # elems[j]不大于其兄弟结点的数据
            if e < elems[j]:        # e 在三者中最小，已找到了位置
                break
            elems[i] = elems[j]     # elems[j] 在三者中最小，上移
            i, j = j, 2*j + 1
        elems[i] = e

    def buildhead(self):
        """堆的初始构建，基于已有的list建立处理堆"""
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

def heap_sort(elems):
    """堆排序"""
    def shifdown(elems, e, begin, end):
        i, j = begin, begin*2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1              # elems[j]不大于其兄弟结点的数据
            if e < elems[j]:        # e 在三者中最小，已找到了位置
                break

            elems[i] = elems[j]     # elems[j] 在三者中最小，上移
            i, j = j, 2*j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end//2, -1, -1):
        shifdown(elems, elems[i], i, end)
    
    for i in range(end-1, 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        shifdown(elems, e, 0, i)

if __name__ == "__main__":
    elems = [1,2, 5, 4, 3]
    heap_sort(elems)
    print(elems)

