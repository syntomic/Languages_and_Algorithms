class TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    # None不是TreeNode型
    def print_tree(self):
        """前序遍历打印"""
        print("(" + str(self.val), end="")
        if self.left is None and self.right is None:
            print("^^)" , end="")
            return
        elif self.left is None:
            print("^", end="")
            self.right.print_tree()
            print(")", end="")
            return
        elif self.right is None:
            self.left.print_tree()
            print("^", end="")
            print(")", end="")
            return

        self.left.print_tree()
        self.right.print_tree()
        print(")", end="")
        return

    def print_tree_1(self):
        """前序遍历打印"""
        print(str(self.val), end=" ")
        if self.left is None and self.right is None:
            print("^ ^" , end=" ")
            return
        elif self.left is None:
            print("^", end=" ")
            self.right.print_tree_1()
            #print(")", end="")
            return
        elif self.right is None:
            self.left.print_tree_1()
            print("^", end=" ")
            #print(")", end="")
            return

        self.left.print_tree_1()
        self.right.print_tree_1()
        #print(")", end="")
        return
    
    @staticmethod
    def deserialize(s):
        """前序遍历序列转化为树"""
        flag = -1
    
        def core(s, flag):
            flag += 1
            l = s.split(' ')

            if flag >= len(s):
                return None

            root = None

            if l[flag] != '^':
                root = TreeNode(int(l[flag]))
                root.left, flag = core(s, flag)
                root.right, flag = core(s, flag)

            return root, flag

        root, flag = core(s, flag)
        return root


if __name__ == "__main__":
    s = '5 3 2 ^ ^ 4 ^ ^ 7 6 ^ ^ 8 ^ ^ '
    root = TreeNode.deserialize(s)


    root.print_tree()
    print()
    root.print_tree_1()