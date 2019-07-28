from tree_node import TreeNode

def has_subtree(root1, root2):
    """判断root2是否为root1的子结构"""
    result = False
    
    if root1 and root2:
        if root1.val == root2.val:
            result = does_root1_have_root2(root1, root2)

        if not result:
            result = has_subtree(root1.left, root2)

        if not result:
            result = has_subtree(root1.right, root2)

    return result

def does_root1_have_root2(root1, root2):
    """在根元素相同的情况下，判断root1是否包含root2"""
    if root2 == None:
        return True
    if root1 == None:
        return False
    if root1.val != root2.val:
        return False

    return does_root1_have_root2(root1.left, root2.left) and does_root1_have_root2(root1.right, root2.right)

if __name__ == "__main__":
    root1 = TreeNode(8, TreeNode(8,
                                    TreeNode(9),
                                    TreeNode(2, 
                                                TreeNode(4),
                                                TreeNode(7))),
                        TreeNode(7))

    root2 = TreeNode(8, 
                        TreeNode(9),
                        TreeNode(2))

    print(has_subtree(root1, root2))