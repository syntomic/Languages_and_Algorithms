class ListNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def printall(self):
        p = self
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

if __name__ == "__main__":
    head = ListNode(1)
    
    p = head
    for i in range(2, 9):
        p.next = ListNode(i)
        p = p.next
    
    head.printall()