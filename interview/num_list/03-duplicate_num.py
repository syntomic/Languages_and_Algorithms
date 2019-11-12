def duplicate_num(nums):
    """
    长度为n的数组中所有数字都在0~n-1, 找出数组中一个重复的数字
    """
    nums_len = len(nums)

    for i in range(nums_len):
        if nums[i] < 0 or nums[i] > nums_len - 1:
            return False

    for i in range(nums_len):
        # 将nums[i]交换至下标为nums[i]的位置
        while nums[i] != i:

            if nums[i] == nums[nums[i]]:
                return nums[i]

            # 不能 num[i], nums[nums[i]] = nums[nums[i]], nums[i]
            temp = nums[i]
            nums[i], nums[temp] = nums[temp], nums[i]
            
    return False


def any_duplicate_num(nums):
    '''
    长度为n+1的数组中数字都在1~n, 不修改数组找出一个重复的数字
    >>> nums = []
    >>> any_duplicate_num(nums)
    'There is no elements'
    >>> nums = [2, 3, 5, 4, 3, 2, 6, 7]
    >>> any_duplicate_num(nums)
    3
    '''   
    def count_range(start, end):
        count = 0
        for i in nums:
            if i >= start and i <= end:
                count += 1
        return count

    if not nums:
        return "There is no elements"

    nums_len = len(nums)
    start = 1
    end = nums_len - 1

    while end > start:
        # 二分法, 重复数字出现在数目大于一半的范围中
        middle = start + (end - start) // 2
        count = count_range(start, middle)
        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1

    return start
 
 
if __name__ == "__main__":
    # 文档测试
    import doctest
    doctest.testmod()

    nums1 = [5, 3, 1, 0, 2, 2, 3]
    nums2 = [2,3]
    nums3 = [1, 2, 0]
    print(duplicate_num(nums1))
    print(duplicate_num(nums2))
    print(duplicate_num(nums3))