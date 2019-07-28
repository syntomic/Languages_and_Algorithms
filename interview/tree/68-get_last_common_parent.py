from tree_node import TreeNode

"""
树中两个节点的最低公共祖先
"""
# BST case
def BST(root, node1, node2):
    """二叉搜索树情形"""
    if root == None or node1 == None or node2 == None:
        return

    if node1.val < root.val > node2.val:
        return BST(root.left, node1, node2)

    elif node1.val > root.val < node2.val:
        return BST(root.right, node1, node2)

    else:
        return root

# Has parent case
# Convert to find common node of two llist 


# general case
def find_node(root, node):
    if root == None or node == None:
        return False

    if root.val == node.val:
        return True

    found = find_node(root.left, node)
    if not found:
        return find_node(root.right, node)

    return found

def general(root, node1, node2):
    """一般情形"""
    if find_node(root.left, node1):
        if find_node(root.right, node2):
            return root
        else:
            return general(root.left, node1, node2)

    else:
        if find_node(root.left, node2):
            return root
        else:
            return general(root.right, node1, node2)


if __name__ == "__main__":
    binary_search_tree = TreeNode(5, 
                                     TreeNode(3,
                                                 TreeNode(2),
                                                 TreeNode(4)),
                                     TreeNode(7,
                                                 TreeNode(6),
                                                 TreeNode(8)))

    general_tree = TreeNode(1, 
                                TreeNode(2,
                                            TreeNode(4),  
                                            TreeNode(5,
                                                        TreeNode(7))),
                                TreeNode(3,
                                            None,
                                            TreeNode(6)))


    print(BST(binary_search_tree, TreeNode(8), TreeNode(6)).val)
    print(find_node(general_tree, TreeNode(2)))
    print(general(general_tree, TreeNode(4), TreeNode(7)).val)


    

    