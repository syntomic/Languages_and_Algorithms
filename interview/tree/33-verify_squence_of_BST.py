def verify_sequence_of_BST(nums):
    """判断数组nums是否为二叉搜索树的后序遍历结果"""
    if nums == None or len(nums) <= 0:
        return False

    length = len(nums)
    root = nums[-1]

    # 二叉搜索树中左子树节点的值小于根节点的值
    i = 0
    for i in range(length-1):
        if nums[i] > root:
            break

    # 二叉搜索树中右子树节点的值大于根节点的值
    j = i
    for j in range(i, length-1):
        if nums[j] < root:
            return False
            
    left = True
    if i > 0:
        left = verify_sequence_of_BST(nums[:i])

    right = True
    if i < length -1:
        right = verify_sequence_of_BST(nums[i+1:])

    return left and right

if __name__ == "__main__":
    nums = [5, 7, 6, 9, 11, 10, 8]
    print(verify_sequence_of_BST(nums))