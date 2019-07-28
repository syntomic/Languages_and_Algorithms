from tree_node import TreeNode

def tree_depth(root):
    """二叉树的深度"""
    if root == None:
        return 0

    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)

    return left_depth + 1 if left_depth > right_depth else right_depth + 1

def is_balanced(root):
    """判断二叉树是否为平衡二叉树，后序遍历"""
    depth = 0
    return is_balanced_core(root, depth)

def is_balanced_core(root, depth):
    if root == None and depth == 0:
        return True

    left = tree_depth(root.left)
    right = tree_depth(root.right)

    if is_balanced_core(root.left, left) and is_balanced_core(root.right, right):
        diff = left - right
        if diff <= 1 & diff >= -1:
            depth = 1 + max(left, right)
            return True

    return False


if __name__ == "__main__":
    root = TreeNode(1, 
                        TreeNode(2,
                                    TreeNode(4),
                                    TreeNode(5,
                                                TreeNode(7))),
                        TreeNode(3,
                                    None,
                                    TreeNode(6)))

    #root.print_tree()
    print(tree_depth(root))
    print(is_balanced(root))