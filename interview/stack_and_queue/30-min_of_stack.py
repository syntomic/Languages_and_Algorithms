class MinStack():
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    
    def push(self, node):       
        self.stack.append(node)

        if self.minstack==[] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())
        
    def pop(self):
        if self.stack==[] or self.minstack==[]:
            return None

        self.stack.pop()
        self.minstack.pop()

    def min(self):
        return self.minstack[-1]

if __name__ == "__main__":
    mstack = MinStack()
    mstack.push(3)
    mstack.push(4)
    mstack.push(2)
    mstack.push(1)
    mstack.pop()
    mstack.pop()
    mstack.push(0)
    print(mstack.min())

    
    