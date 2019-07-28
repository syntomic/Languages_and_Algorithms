def least_num_in_rotation_nums(nums):
    """
    递增排序的数组的一个旋转，输出旋转数组的最小元素
    """
    # 二分查找
    nums_len = len(nums)

    if nums_len == 0:
        return -1

    if nums[0] < nums[-1]:
        return nums[0]

    p_1 = 0
    p_2 = nums_len - 1

    while (p_2 - p_1) > 1:
        
        mid = (p_1 + p_2) // 2
        
        if nums[p_1] < nums[mid]:
            p_1 = mid
        elif nums[p_2] > nums[mid]:
            p_2 = mid
        elif nums[p_1] == nums[mid] == nums[p_2]:
            # 如果三个数字相等，只能顺序查找
            return min_in_order(nums, p_1, p_2)
            
    return nums[p_2]

def min_in_order(nums, p_1, p_2):
    """顺序查找"""
    min_ = nums[p_1]
    for i in range(p_1+1, p_2+1):
        if min_ > nums[i]:
            min_ = nums[i]

    return min_

if __name__ == "__main__":
    nums_0 = [3, 4, 5, 1, 2]
    nums_1 = [1, 0, 1, 1, 1]
    # goal = min(nums)
    print(least_num_in_rotation_nums(nums_0))
    print(least_num_in_rotation_nums(nums_1))