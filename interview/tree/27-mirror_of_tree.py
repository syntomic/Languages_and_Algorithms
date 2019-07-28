from tree_node import TreeNode

def mirror_of_tree(root):
    """二叉树的镜像"""
    if root == None:
        return
    if root.left == None:
        return root

    root.left, root.right = root.right, root.left
    mirror_of_tree(root.left)
    mirror_of_tree(root.right)


if __name__ == "__main__":
    root = TreeNode(8,TreeNode(6,TreeNode(5),TreeNode(7)),
                    TreeNode(10,TreeNode(9),TreeNode(11)))

    root.print_tree()
    mirror_of_tree(root)
    print()
    root.print_tree()