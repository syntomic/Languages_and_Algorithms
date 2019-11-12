def partition(nums, start, end):
    pivot = nums[start]
    i = start
    for j in range(start+1, end+1):
        if nums[j] <=  pivot:
            i += 1
            if j != i:                
                nums[i], nums[j] = nums[j], nums[i]
    
    nums[start], nums[i] = nums[i], nums[start]
    
    return i

def get_least_k_nums_1(nums, k):
    """数组的最小k个数，基于partition，需要修改数组"""
    if k < 1 or k > len(nums):
        raise ValueError("k is not correct")

    if nums==[]:
        raise ValueError("nums is None")

    nums_len = len(nums)
    start = 0
    end = nums_len - 1
    index = partition(nums, start, end)

    while index != k-1:
        if index > k - 1:
            end = index - 1
            index = partition(nums, start, end)
        else:
            start = index + 1
            index = partition(nums, start, end)

    return nums[:index+1]


def get_least_k_nums_2(nums, k):
    """
    利用容器，不修改数组，适合处理海量数据
    """
    if k < 1 or k > len(nums):
        raise ValueError("k is not correct")
        
    if nums==[]:
        raise ValueError("nums is None")

    nums_len = len(nums)
    list_ = []

    for i in range(nums_len):
        if len(list_) < k:
            list_.append(nums[i])
        else:
            # 利用堆或红黑树
            max_idx = list_.index(max(list_))
            if nums[i] < max(list_):
                list_[max_idx] = nums[i]

    return list_


if __name__ == "__main__":
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    #nums =[1,2,2,3]
    #nums = []
    # k = 1 or k = nums_len
    # k < 1 or k > nums_len
    print(get_least_k_nums_2(nums, 4))
    print(get_least_k_nums_1(nums, 4))