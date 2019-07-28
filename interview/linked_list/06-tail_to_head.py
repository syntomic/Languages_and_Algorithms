from collections import deque

from list_node import ListNode


def tail_to_head_stack(head):
    """
    从尾到头打印出每个节点的值，利用栈的方法
    """
    if not head:
        return []

    result = []    
    q = deque()

    while head:
        q.append(head.elem)
        head = head.next

    while q:
        result.append(q.pop())
    
    return result

def tail_to_head_recursive(head):
    """
    从尾到头打印出每个节点的值，利用递归的方法
    """
    if not head.elem:
        return []
    
    if not head.next:
        return [head.elem]
    
    elm = head.elem
    head = head.next
    rev_list = tail_to_head_recursive(head)
    rev_list.append(elm)

    return rev_list


if __name__ == "__main__":
    head = ListNode(1)
    p = head
    for i in range(2, 10):
        p.next = ListNode(i)
        p = p.next
    
    print(tail_to_head_recursive(head))
    print(tail_to_head_stack(head))

    