from tree_node import TreeNode

# 中序遍历
def kth_node(root, k):
    """二叉搜索树的第k大节点"""
    if root == None or k == 0:
        return None

    res = []
    def in_order(root):
        if len(res) >= k or not root:
            return

        in_order(root.left)
        res.append(root)
        in_order(root.right)

    in_order(root)
    if len(res) < k:
        return
    
    return res[k-1]

    
if __name__ == "__main__":
    root = TreeNode(5, 
                        TreeNode(3,
                                    TreeNode(2),
                                    TreeNode(4)),
                        TreeNode(7,
                                    TreeNode(6),
                                    TreeNode(8)))
    
    print(kth_node(root, 3).val)


