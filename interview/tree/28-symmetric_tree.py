from tree_node import TreeNode

def is_symmetical(root):
    """判断一棵二叉树是否对称"""
    def is_symmetrical_core(root1, root2):
        """前序遍历"""
        if root1 == None and root2 == None:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return is_symmetrical_core(root1.left, root2.right) and \
            is_symmetrical_core(root1.right, root2.left)

    return is_symmetrical_core(root, root)


if __name__ == "__main__":
    root = TreeNode(7, TreeNode(7, 
                                   TreeNode(7),
                                   TreeNode(7)),
                       TreeNode(7, 
                                   TreeNode(7)))
    #root.print_tree()

    print(is_symmetical(root))