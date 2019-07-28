class SubtreeIndexError(ValueError):
    pass

def Tree(data, *subtrees):
    """树的list实现"""
    return [data].extend(subtrees)

def is_empty_tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError

    return tree[i+1]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree

if __name__ == "__main__":
    tree1 = Tree('+', 1, 2, 3)
    tree2 = Tree('*', tree1, 6, 8)
    set_subtree(tree1, 2, Tree('+', 3, 5))