from list_node import ListNode

def merge_sorted_llist(head1, head2):
    """合并两个排序的链表"""
    if not head1:
        return head2
    elif not head2:
        return head1

    #merge_head = None

    if head1.elem < head2.elem:
        merge_head = head1
        merge_head.next = merge_sorted_llist(head1.next, head2)
    else:
        merge_head = head2
        merge_head.next = merge_sorted_llist(head1, head2.next)
        
    return merge_head

if __name__ == "__main__":
    head1 = ListNode(1)
    p = head1

    for i in range(2, 5):
        p.next = ListNode(2 * i - 1)
        p = p.next

    head1.printall()

    head2 = ListNode(2)
    q = head2

    for i in range(2, 5):
        q.next = ListNode(2 * i)
        q = q.next

    head2.printall()

    merge_head = merge_sorted_llist(head1, head2)
    merge_head.printall()