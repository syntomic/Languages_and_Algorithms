def reorder_odd_even(nums):
    """
    调整数组顺序使奇数位于偶数前面
    """
    if nums == []:
        return

    nums_len = len(nums)
    p = 0
    q = nums_len - 1

    while p < q:
        if is_odd(nums[p]):
            p += 1
        if not is_odd(nums[q]):
            q -= 1
        else:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1

    return nums

# 考虑扩展
def is_odd(n):
    """判断是否为奇数"""
    return n & 1 == 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(reorder_odd_even(nums))
