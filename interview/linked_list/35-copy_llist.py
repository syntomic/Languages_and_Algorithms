class RandomListNode:
    def __init__(self, elem, next_ = None, random = None):
        self.elem = elem
        self.next = next_
        self.random = random


def clone(head):
    """复制复杂链表"""
    if head == None:
        return None

    clone_nodes(head)
    connect_random_nodes(head)

    return reconnect_nodes(head)

def clone_nodes(head):
    '''
    复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    '''
    node = head

    while node:
        cloned = RandomListNode(0)
        cloned.elem = node.elem
        cloned.next = node.next

        node.next = cloned
        node = cloned.next

def connect_random_nodes(head):
    '''
    将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点
    '''
    node = head
    while node:
        cloned = node.next
        if node.random != None:
            cloned.random = node.random.next
        node = cloned.next

def reconnect_nodes(head):
    '''
    拆分链表：将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    '''
    node = head
    cloned_head = cloned_node = node.next
    node.next = cloned_node.next
    node = node.next

    while node:
        cloned_node.next = node.next
        cloned_node = cloned_node.next
        node.next = cloned_node.next
        node = node.next

    return cloned_head

def clone_recursive(head):
    """递归方法"""
    if head == None:
        return None

    clone_node = RandomListNode(head.elem)
    clone_node.random = head.random
    clone_node.next = clone_recursive(head.next)

    return clone_node

if __name__ == "__main__":
    # 人生苦短，我用python
    def clone2(head):
        import copy
        # deepcopy 拷贝对象及其子对象
        return copy.deepcopy(head)
