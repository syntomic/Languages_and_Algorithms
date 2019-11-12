def partition(nums, start, end):
    """
    把nums[start:end]以nums[start]为界划分成两部分
    返回：
        nums[start]的指标
    """
    pivot = nums[start]
    i = start

    for j in range(start+1, end+1):
        if nums[j] <=  pivot:
            i += 1
            # 避免不必要的交换
            if j != i:                
                nums[i], nums[j] = nums[j], nums[i]
    
    nums[start], nums[i] = nums[i], nums[start]
    
    return i

def check_more_than_half(nums, num):
    """
    检查num在nums中是否超过一半
    """
    times = 0

    for i in range(len(nums)):
        if nums[i] == num:
            times += 1

    if times > (len(nums) >> 1):
        return True
    else:
        return False

def more_than_half_num(nums):
    """
    数组中出现次数超过一半的数字，基于partition，需要修改数组
    """
    if nums == []:
        return "There is no elments"

    if len(nums) == 1:
        return "Must more than two elements"

    nums_len = len(nums)
    start = 0
    end = nums_len - 1
    middle = nums_len >> 1
    index = partition(nums, start, end)

    while index != middle:
        if index > middle:
            end = index - 1
            index = partition(nums, start, end)
        else:
            start = index + 1
            index = partition(nums, start, end)

    result = nums[middle]

    if check_more_than_half(nums, result):
        return result
    else:
        return "There is no elements more than half of nums"

def more_than_half_num_2(nums):
    """
    数组中超过一半的数字，基于数组特点
    """
    if nums == []:
        return "There is no elments"
    if len(nums) == 1:
        return "Must more than two elements"

    result = nums[0]
    times = 1
    
    for i in range(1,len(nums)):
        if times == 0: 
            result = nums[i]
            times = 1
        elif nums[i] == result:
            times += 1
        else:
            times -= 1

    if check_more_than_half(nums, result):
        return result
    else:
        return "There is no elements more than half of nums"


if __name__ == "__main__":
    nums_1 = [1,2,3,2,2,2,5,4,2]
    nums_2 = [1,2,3,4,2]
    nums_3 = [1]
    nums_4 = []
    print(more_than_half_num(nums_1), more_than_half_num_2(nums_1))
    print(more_than_half_num(nums_2), more_than_half_num_2(nums_2))
    print(more_than_half_num(nums_3), more_than_half_num_2(nums_3))
    print(more_than_half_num(nums_4), more_than_half_num_2(nums_4))