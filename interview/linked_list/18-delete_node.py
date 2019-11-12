from list_node import ListNode

def delete_node(head, node):
    """
    在O(1)时间内删除指定节点
    """
    if not (head and node):
        return "链表和节点必须不为空"

    #要删除的节点不是尾节点
    if node.next:
        next_node = node.next
        node.elem = next_node.elem
        node.next = next_node.next
        next_node.elem = None
        next_node.next = None

    
    #链表只要一个节点，删除头节点（也是尾节点）
    elif head == node:
        node = None
        head = None

    #链表中有多个节点，删除尾节点
    else:
        p = head
        while p.next != node:
            p = p.next

        p.next = None
        node = None
        
    return head

def delete_duplicated_node(head):
    """
    删除重复节点
    """
    first = ListNode(-1)
    first.next = head # first.next 为第一个不重复的结点
    last = first # last 为 head 前一个结点
    
    while head and head.next:

        if head.elem == head.next.elem:
            elem = head.elem

            while head and head.elem == elem:
                head = head.next

            last.next = head
        
        else:
            last = head
            head = head.next

    return first.next

if __name__ == "__main__":
    head = ListNode(1)
    p = head
    
    i = 2
    while i <= 5:
        if i == 3 or i == 4 :
            for j in range(2):
                p.next = ListNode(i)
                p = p.next
            i += 1
        else:
            p.next = ListNode(i)
            p = p.next
            i += 1
        
    head.printall()

    node = head.next

    delete_node(head, node).printall()

    delete_duplicated_node(head).printall()





    
    
