class TreeNode:
    """树结点类"""
    def __init__(self, data, subs=[]):
        self._data = data
        self._subtrees = list(subs)

    def __str__(self):
        return "[TreeNode {0} {1}".format(self._data, self._subtrees)


class Tree:
    """"树类"""
    def __init__(self):
        self.__root = None

    ## 待完成

