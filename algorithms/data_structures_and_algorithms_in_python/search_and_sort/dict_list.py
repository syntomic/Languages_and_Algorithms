class DictList:
    """字典的list实现"""
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    ## 待完成

class DictOrdList(DictList):
    """有序字典类"""

    def __init__(self):
        DictList.__init__(self)


def bisearch(lst, key):
    """二分查找"""
    low, high = 0, len(lst)-1
    while low <= high:
        mid = low + (high - low)//2
        if key == lst[mid].key:
            return lst[mid].value
        if key < lst[mid].value:
            high = mid - 1
        else:
            low = mid + 1