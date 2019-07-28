from list_node import ListNode


def entry_node_of_loop(head):
    """
    找出链表中环的入口节点
    """
    meet_node = meeted_node(head)

    if not meet_node:
        return None

    # 得到环中节点的数目
    node_in_loop = 1
    p = meet_node

    while p.next != meet_node:
        node_in_loop += 1
        p = p.next

    # 先移动p，次数为环中节点的数目  
    p = head
    for i in range(node_in_loop):
        p = p.next

    # 再移动p和q
    q = head
    while q != p:
        p = p.next
        q = q.next

    return p

def meeted_node(head):
    """
    在链表中存在环的前提下找到相遇节点
    如果不存在环，就返回None
    """
    if not head:
        return None

    slow = head.next

    if slow == None:
        return None

    fast = slow.next

    while fast and slow:
        if slow == fast:
            return slow
        
        slow = slow.next

        fast = fast.next
        if fast:
            fast = fast.next
    
    return None

if __name__ == "__main__":
    head = ListNode(1)
    p = head

    for i in range(2,7):
        p.next = ListNode(i)
        p = p.next

    p.next = head.next.next

    q = head
    for i in range(7):
        print(q.elem, end=' ')
        q = q.next

    print('')
    print(entry_node_of_loop(head).elem)