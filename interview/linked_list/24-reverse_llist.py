from list_node import ListNode

def reverse_llist(head):
    """反转链表"""
    if head is None:
        return "No element"

    reversed_llist = None
    left_llist = head

    while left_llist is not None:
        q = left_llist
        left_llist = q.next
        q.next = reversed_llist
        reversed_llist = q

    return reversed_llist

if __name__ == "__main__":
    head = ListNode(1)

    p = head
    for i in range(2, 5):
        p.next = ListNode(i)
        p = p.next

    head.printall()

    # head = ListNode(1)
    # head = None
    q = reverse_llist(head)
    q.printall()

    