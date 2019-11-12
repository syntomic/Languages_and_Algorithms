def max_sum_of_continous_subnums(nums):
    """连续子数组的最大和"""
    if nums == []:
        return None

    cur_sum = 0
    max_sum = nums[0]
    
    for i in range(len(nums)):
        if i == 0 or cur_sum <= 0:
            cur_sum = nums[i]
        else:
            cur_sum += nums[i]
        
        if  max_sum < cur_sum:
            max_sum = cur_sum

    return max_sum

if __name__ == "__main__":
    nums_1 = [1, -2, 3, 10, -4, 7, 2, -5]
    nums_2 = [-1,-2, -3]
    nums_3 = [1, 2, 3]
    nums_4 = []
    print(max_sum_of_continous_subnums(nums_1))
    print(max_sum_of_continous_subnums(nums_2))
    print(max_sum_of_continous_subnums(nums_3))
    print(max_sum_of_continous_subnums(nums_4))
