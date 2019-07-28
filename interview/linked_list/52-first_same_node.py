from list_node import ListNode

def first_same_node(head1, head2):
    """两个链表的第一个公共节点"""
    len1 = get_length(head1)
    len2 = get_length(head2)
    
    if len2 > len1:
        head1, head2 = head2, head1
    
    diff = abs(len2- len1)
    
    for i in range(diff):
        head1 = head1.next
    
    while head1 != None and (head2 != None) and head1 != head2:
        head1 = head1.next
        head2 = head2.next

    return head2
        
def get_length(head):
    len_ = 0

    while head:
        head = head.next
        len_ += 1

    return len_

if __name__ == "__main__":
    head1 = ListNode(1)
    p = head1
    for i in range(2, 4):
        p.next = ListNode(i)
        p = p.next

    head2 = ListNode(4)
    q = head2
    for i in range(5, 8):
        q.next = ListNode(i)
        q = q.next

    p.next = head2.next.next

    print(first_same_node(head1, head2).elem)