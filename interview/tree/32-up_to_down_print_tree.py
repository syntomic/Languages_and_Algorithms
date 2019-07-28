from tree_node import TreeNode

from collections import deque

def print_from_top_to_bottom(root):
    """从上到下打印树"""
    if not root:
        return

    queue = deque()
    queue.appendleft(root)

    while queue:
        node = queue.pop()
        print(node.val, end = ' ')

        if node.left:
            queue.appendleft(node.left)
        
        if node.right:
            queue.appendleft(node.right)


def print_from_top_to_bottom_stratified(root):
    """分层从上到下打印树"""
    if root == None:
        return

    queue = deque()
    queue.appendleft(root)
    next_level = 0
    to_be_printed = 1

    while queue:
        node = queue.pop()
        print(node.val, end = ' ')

        if node.left:
            queue.appendleft(node.left)
            next_level += 1

        if node.right:
            queue.appendleft(node.right)
            next_level += 1

        to_be_printed -= 1

        if to_be_printed == 0:
            print('')
            to_be_printed = next_level
            next_level = 0

def print_zig_zag(root):
    """之字形打印树"""
    if root == None:
        return

    stack = [deque(), deque()]
    current = 0
    next_ = 1

    stack[current].append(root)

    while stack[current] or stack[next_]:
        node = stack[current].pop()
        print(node.val, end=' ')

        if current == 0:
            if node.left:
                stack[next_].append(node.left)
            if node.right:
                stack[next_].append(node.right)
        else:
            if node.right:
                stack[next_].append(node.right)
            if node.left:
                stack[next_].append(node.left)

        if not stack[current]:
            print('')
            current = 1 - current
            next_ = 1 - next_

def print_from_bottom_to_top(root):
    """从下到上打印树"""
    def mid(root):
        if not root.left and not root.right:
            return

        queue = deque()
        queue.appendleft(root.left.val)
        queue.appendleft(root.right.val)

        mid(root.left)
        mid(root.right)

        while queue:
            print(queue.pop(), end = ' ')
            
    mid(root)
    print(root.val)
    

if __name__ == "__main__":
    root = TreeNode(8, 
                       TreeNode(6,
                                   TreeNode(5),
                                   TreeNode(7)),
                       TreeNode(10, 
                                    TreeNode(9),
                                    TreeNode(11)))
    #root.print_tree()
    print_from_top_to_bottom(root)
    print('')
    print_from_bottom_to_top(root)

    print_from_top_to_bottom_stratified(root)

    print_zig_zag(root)
