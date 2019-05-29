def max_sum_of_continous_subnums(nums):
    """连续子数组的最大和"""
    if nums == []:
        return None

    list_ = []
    sum_ = 0
    
    for i in range(len(nums)):
        if i == 0 or sum_ <= 0:

            sum_ = nums[i]
            list_.append(sum_)

        elif i !=0 and sum_ > 0:
            
            sum_ += nums[i]
            list_.append(sum_)

    return max(list_)

if __name__ == "__main__":
    nums_1 = [1, -2, 3, 10, -4, 7, 2, -5]
    #nums_2 = [-1,-2, -3]
    #nums_3 = [1, 2, 3]
    #nums_4 = []
    print(max_sum_of_continous_subnums(nums_1))
