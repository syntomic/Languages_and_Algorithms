import heapq

class MinHeap(object):
    """最小堆"""
    def __init__(self, list_):
        self.heap = list_
        heapq.heapify(self.heap)

    def get_min(self):
        return self.heap[0]

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        heapq.heappop(self.heap)

class MaxHeap(object):
    """最大堆"""
    def __init__(self, list_):
        self.heap = [-i for i in list_]
        heapq.heapify(self.heap)

    def get_max(self):
        return -self.heap[0]

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

min_ = MinHeap([])
max_ = MaxHeap([])

def get_median(nums, len_):
    """
    数据流的中位数
    若读出奇数个数值，中位数就是排序后的中间值
    若为偶数，中间数就是排序后中间两个数的平均值
    """
    if not nums or len_ <= 0:
        return

    max_.push(nums[0])

    for i in range(1, len_):
        if i & 1 == 1:
            if max_.get_max() > nums[i]:
                max_.push(nums[i])
                min_.push(max_.pop())
            else:
                min_.push(nums[i])
        else:
            if min_.get_min() < nums[i]:
                min_.push(nums[i])
                max_.push(min_.pop())
            else:
                max_.push(nums[i])

    if len_ & 1 == 1:
        return max_.get_max()
    else:
        return (max_.get_max() + min_.get_min()) / 2
            

if __name__ == "__main__":
    nums = [4, 3, 2, 5, 1, 6, 7]
    print(get_median(nums, 5))