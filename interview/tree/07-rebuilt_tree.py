from tree_node import TreeNode

def rebuilt_binary_tree(pre, ino):
    """前序遍历和中序遍历确定二叉树"""
    if not pre and not ino:
        return None
    
    root = TreeNode(pre[0])

    if set(pre) != set(ino):
        return None
    
    i = ino.index(pre[0])
    root.left = rebuilt_binary_tree(pre[1:i+1], ino[:i])
    root.right = rebuilt_binary_tree(pre[i+1:], ino[i+1:])

    return root

if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]

    root = rebuilt_binary_tree(pre, ino)
    root.print_tree()