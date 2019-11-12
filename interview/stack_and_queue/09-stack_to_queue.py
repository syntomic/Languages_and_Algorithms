from collections import deque


class Queue():
    """两个栈实现队列"""
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "There is no element"
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


class Stack():
    """两个队列模拟一个栈"""
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, node):
        self.queue1.appendleft(node)

    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return "There is no element"
        elif len(self.queue2) == 0:
            while len(self.queue1) > 1:
                self.queue2.appendleft(self.queue1.pop())
            
            return self.queue1.pop()
            
        elif len(self.queue1) == 0:
            while len(self.queue2) > 1:
                self.queue1.appendleft(self.queue2.pop())

            return self.queue2.pop()
        

if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.push(i)

    for i in range(5):
        print(queue.pop(), end=' ')

    print()

    stack = Stack()
    for i in range(5):
        stack.push(i)

    for i in range(5):
        print(stack.pop(), end=' ')


        
