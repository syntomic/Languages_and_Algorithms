def max_profit(nums):
    """
    股票价格按照时间先后顺序存储在数组中，
    求买卖股票一次可能获得的最大利润
    """
    if nums == [] or len(nums) < 2:
        return 0

    min_ = nums[0]
    max_ = nums[1] - min_

    for i in range(2, len(nums)):
        if nums[i-1] < min_:
            min_ = nums[i-1]

        cur = nums[i] - min_

        if cur > max_:
            max_ = cur

    return max_ 

if __name__ == "__main__":
    nums = [9, 11, 8, 5, 7, 12, 16, 14]
    print(max_profit(nums))