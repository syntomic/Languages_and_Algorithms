from tree_node import TreeNode

from collections import deque

def find_path(root, sum_):
    """打印二叉树中节点值的和为输入整数的所有路径"""
    if root == None:
        return
    
    path = []
    current_sum = 0
    find_path_current(root, sum_, path, current_sum)

def find_path_current(root, sum_, path, current_sum):
    current_sum += root.val
    path.append(root.val)

    is_leaf = (root.left == None and root.right == None)

    if current_sum == sum_ and is_leaf:
        print("A path is found")
        for i in path:
            print(i, end=' ')

        print("")

    if root.left != None:
        find_path_current(root.left, sum_, path, current_sum)

    if root.right != None:
        find_path_current(root.right, sum_, path, current_sum)

    path.pop()

if __name__ == "__main__":
    root = TreeNode(10, 
                        TreeNode(5, 
                                    TreeNode(4),
                                    TreeNode(7)),
                        TreeNode(12))

    find_path(root, 22)
