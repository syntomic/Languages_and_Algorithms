class LNode:
    """链表结点类"""
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class DLNode(LNode):
    """双链表结点类"""
    def __init__(self, elem, prev = None, next_ = None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

if __name__ == "__main__":
    llist1 = LNode(1)

    p = llist1
    for i in range(2, 4):
        p.next = LNode(i)
        p = p.next

    print(llist1.next.next.next)
    p = llist1
    while p is not None:
        print(p.elem)
        p = p.next