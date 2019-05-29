from collections import deque

stack1 = deque()
stack2 = deque()

class Queue():
    def __init__(self):
        self.stack1 = stack1
        self.stack2 = stack2

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "There is no element"
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

# 两个队列模拟一个栈

if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.push(i)

    for i in range(5):
        print(queue.pop(), end=' ')


        
