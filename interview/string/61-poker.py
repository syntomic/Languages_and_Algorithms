def is_continuous(nums):
    """
    从扑克牌随机抽5张牌，判断是不是一个顺子
    大小王可以看作任何数
    """
    if len(nums) != 5:
        return False
        
    dict_= {'A':1, 'J': 11, 'Q': 12, 'K': 13, 'G': 0, 'g': 0}

    for i in range(len(nums)):
        if nums[i] in dict_.keys():
            nums[i] = dict_[nums[i]]

    s_nums = sorted(nums)
    count = 0

    for i in s_nums:
        if i == 0:
            count += 1

    count_2 = 0

    for i in range(1, len(s_nums)):
        if s_nums[i] == s_nums[i-1]:
            return False

        count_2 += s_nums[i] - s_nums[i-1] - 1

    if count >= count_2:
        return True
    else:
        return False

if __name__ == "__main__":
    nums = ['g',4, 9, 5, 'A']
    nums_1 = [1, 2, 4, 5, 'g']
    print(is_continuous(nums))
    print(is_continuous(nums_1))

    