from list_node import ListNode

def find_kth_to_tail(head, k):
    """
    求链表的倒数第k个节点
    """
    if not head or k == 0:
        return None

    ahead = head
    behind = None

    for i in range(k-1):
        # 判断节点个数是否大于k
        if ahead.next:
            ahead = ahead.next
        else:
            return None

    behind = head

    while ahead.next:
        ahead = ahead.next
        behind = behind.next

    return behind

if __name__ == "__main__":
    
    head = ListNode(1)
    p = head
    
    for i in range(2,10):
        p.next = ListNode(i)
        p = p.next

    head.printall()

    print(find_kth_to_tail(head, 3).elem)