from tree_node import TreeNode

def convert(root):
    """将二叉搜索树转变为双向链表"""
    last_node_in_head = None

    last_node_in_head = convert_node(root, last_node_in_head)

    head = last_node_in_head

    while head != None and head.left != None:
        head = head.left

    return head


def convert_node(root, last_node_in_head):
    """寻找转换后双向链表的最后一个节点""" 
    if root == None:
        return last_node_in_head

    current = root

    if current.left != None:
        last_node_in_head = convert_node(current.left, last_node_in_head)

    current.left = last_node_in_head

    if last_node_in_head != None:
        last_node_in_head.right = current

    last_node_in_head = current

    if current.right != None:
        last_node_in_head = convert_node(current.right, last_node_in_head)

    return last_node_in_head

# 可变对象与不可变对象， local vs global, 最好不用global
"""
def other_function(parameter):
    return parameter + 5

def main_function():
    x = 10
    print(x)    
    x = other_function(x)
    print(x)

a = 1
def f(x):
    x = 3

>>>f(a)
>>>a
1
"""

if __name__ == "__main__":
    root = TreeNode(10, TreeNode(6, 
                                    TreeNode(4),
                                    TreeNode(8)),
                        TreeNode(14, 
                                     TreeNode(12),
                                     TreeNode(16)))
    #root.print_tree()
    head = convert(root)
    print(head.val, head.right.val, head.right.left.val)
