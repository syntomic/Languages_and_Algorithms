import sys
import os
# 添加目录data_structure_and_algorithm
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

from Queue.SQueue import SQueue #pylint: disable=import-error, no-name-in-module
from Stack.SStack import SStack #pylint: disable=import-error

class BinTNode:
    """"二叉树结点类"""
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right
    
    
def count_BinTNodes(t):
    """统计树中结点个数"""
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) \
            + count_BinTNodes(t.right)

def sum_BinTNodes(t):
    """假设结点中保存数值，求这种二叉树里的所有数值和"""
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) \
            + sum_BinTNodes(t.right)

def preorder(t, proc): # proc是具体的结点数据操作
    """先序遍历二叉树"""
    # assert(isinstance(t, BinTNode))
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)

def levelorder(t, proc):
    """"深度优先遍历"""
    qu = SQueue(t)
    qu.enqueue()
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:        # 弹出的树为空则直接跳过
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)

def preorder_nonrec(t, proc):
    """先序循环法"""
    s = SStack()
    while t is not None or not s.is_empty():  
        while t is not None:                  # 沿左分支下行
            proc(t.data)                      # 先根序先处理根数据            
            s.push(t.right)                   # 右分支如栈
            t = t.left                         
        t = s.pop()                           # 遇到空树，回溯

# preorder_nonrec(tree, lambda x: print(x, end=" "))

def preorder_elements(t):
    """生成器遍历"""
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()

def postorder_nonrec(t, proc):
    """非递归后序遍历"""
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:     # 下行循环，直到栈顶的两子树空
            s.push(t)
            t = t.left if t.left is not None else t.right
                                 # 能左就左，否则向右一步

        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right    # 栈不空且当前结点是栈顶的左子结点
        else:
            t = None             # 没有右子树或右子树遍历完毕，强迫退栈


def print_BinSTNodes(t):
    """打印结点数据"""
    if t is None:
        print("^", end="")  # 空树输出 ^
        return
    print("(" + str(t.data), end="")           
    print_BinSTNodes(t.left)
    print_BinSTNodes(t.right)
    print(")" , end="")


if __name__ == "__main__":
    t = BinTNode(1,BinTNode(2),BinTNode(3))
    print(count_BinTNodes(t))
    print_BinSTNodes(t)
    print('')
    preorder_nonrec(t, lambda x: print(x, end=" "))