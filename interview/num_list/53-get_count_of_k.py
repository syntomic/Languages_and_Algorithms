def get_first_k(nums, k, start, end):
    """在数组中找到第一个元素为k的指标"""
    if start > end:
        return -1

    middle_index = (start + end) // 2
    middle_num = nums[middle_index]

    if middle_num == k:
        if (middle_index > 0 and nums[middle_index - 1] != k) or middle_index == 0:
            return middle_index
        else:
            end = middle_index - 1   
    elif middle_num > k:
        end = middle_index - 1
    else:
        start = middle_index + 1

    return get_first_k(nums, k, start, end)

def get_last_k(nums, k, start, end):
    """在数组中找到最后一个元素为k的指标"""
    if start > end:
        return -1

    len_ = len(nums)
    middle_index = (start + end) // 2
    middle_num = nums[middle_index]

    if middle_num == k:
        if (middle_index < len_ - 1 and nums[middle_index + 1] != k) or middle_index == len_ - 1:
            return middle_index
        else:
            start = middle_index + 1
    elif middle_num < k:
        start = middle_index + 1
    else:
        end = middle_index - 1

    return get_last_k(nums, k , start, end)
    
def get_count_of_k(nums, k):
    """计算k在排序数组中出现的次数"""
    count = 0
    len_ = len(nums)

    if nums and len_ > 0:
        first = get_first_k(nums, k, 0, len_ - 1)
        last = get_last_k(nums, k, 0, len_ - 1)

        if first > -1 and last > -1:
            count = last - first + 1

    return count

def get_missing_num(nums):
    """0~n-1递增数组中缺失的数字"""
    if not nums:
        return -1

    len_ = len(nums)
    left = 0
    right = len_ - 1

    while left <= right:
        middle = (right + left) >> 1

        if nums[middle] != middle:
            if middle == 0 or nums[middle-1] == middle - 1:
                return middle
            
            right = middle - 1
        
        else:
            left = middle + 1

    if left == len_:
        return len_

    return - 1

def get_num_same_as_index(nums):
    """递增数组中和下标相等的元素"""
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = left + ((right - left) >> 1)
        
        if nums[middle] == middle:
            return middle

        if nums[middle] > middle:
            right = middle - 1
        else:
            left = middle + 1

    return -1

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    print(get_count_of_k(nums, 3))

    nums_2 = [0, 1, 3, 4, 5]
    print(get_missing_num(nums_2))

    nums_3 = [-3, -1, 1, 3, 5]
    print(get_num_same_as_index(nums_3))