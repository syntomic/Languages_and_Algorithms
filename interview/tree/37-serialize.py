from tree_node import TreeNode

class Solution:
    def __init__(self):
        self.flag = -1

    def serialize(self, root):
        """前序遍历二叉树"""
        if not root:
            return '#,'
        
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, s):
        """前序遍历序列转化为二叉树"""
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None

        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.deserialize(s)
            root.right = self.deserialize(s)

        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, 
                        TreeNode(2, 
                                    TreeNode(4)),
                        TreeNode(3, 
                                    TreeNode(5),
                                    TreeNode(6)))

    s = sol.serialize(root)
    print(s)
    Tree = sol.deserialize(s)
    Tree.print_tree()