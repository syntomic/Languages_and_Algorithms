def find_nums_with_sum(nums, sum_):
    """递增数组中和为sum_的两个数字"""
    p = 0
    q = len(nums) -1

    while p < q:
        if nums[p] + nums[q] == sum_:

            return nums[p], nums[q]

        elif nums[p] + nums[q] < sum_:

            p += 1

        elif nums[p] + nums[q] > sum_:

            q -= 1 
    
    return 'No such elements'


def find_continuous_sequence(sum_):
    """和为sum_的所有连续正数序列"""
    if sum_ < 3:
        return
    
    small = 1
    big = 2
    middle = (1+sum_) / 2
    cur_sum = small + big

    while small < middle:
        if cur_sum == sum_:
            print_continuous_sequence(small, big)

        while cur_sum > sum_ and small < middle:
            cur_sum -= small
            small += 1

            if cur_sum == sum_:
                print_continuous_sequence(small, big)

        big += 1
        cur_sum += big
    

def print_continuous_sequence(small, big):
    for i in range(small, big+1):
        print(i, end=", ")
    
    print('')

    
if __name__ == "__main__":
    nums = [1, 2, 4, 7, 11, 15]
    sum_ = 15
    print(find_nums_with_sum(nums, sum_))
    find_continuous_sequence(sum_)
    