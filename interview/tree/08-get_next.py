from tree_node import TreeNode

def get_next(node):
    """
    给定二叉树和一个结点，找出中序遍历序列的下一个节点
    节点有一个指向父节点的指针
    """
    if not node:
        return 

    #节点有右子树， 下一个节点就是它右子树的最左节点
    elif node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node

    #节点没有右子树， 且为它父节点的右子节点， 则一直寻找它的父节点， 知道它是它父节点的左子树
    elif node.right == None and node.parent.right == node:
        while node.parent != None and node.parent.left != node:
            node = node.parent
        return node.parent

    #节点没有右子树， 且为它父节点的左节点， 下一个节点就是它父节点
    elif node.right == None and node.parent.left == node:
        return node.parent

if __name__ == "__main__":
    root = TreeNode('a', TreeNode('b', 
                                       TreeNode('d'), 
                                       TreeNode('e', 
                                                     TreeNode('h'), 
                                                     TreeNode('i'))), 
                         TreeNode('c', 
                                       TreeNode('f'), 
                                       TreeNode('g')))
    # 需要加入指向父节点的指针
    root.print_tree()