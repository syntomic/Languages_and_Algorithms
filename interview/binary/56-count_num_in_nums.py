def find_nums_appear_once(nums):
    """
    数组中只出现一次的两个数字
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    if not nums or len(nums) < 2:
        return []

    result_exclusive_or = 0

    for i in nums:
        result_exclusive_or ^= i

    index_of_1 = find_first_bit_is_1(result_exclusive_or)

    num1 = num2 = 0

    for j in range(len(nums)):
        if is_bit_1(nums[j], index_of_1):
            num1 ^= nums[j]
        else:
            num2 ^= nums[j]

    return [num1, num2]

def find_first_bit_is_1(num):
    """找到数组每个数字异或后结果二进制表示的第一个为1的位数"""
    index_bit = 0

    while num & 1 == 0 and index_bit <= 32:

        index_bit += 1
        num = num >> 1

    return index_bit

def is_bit_1(num, index_bit):
    """判断数组中每个数字的index_bit位是否为1"""
    num = num >> index_bit

    return num & 1

def find_num_appear_once(nums):
    """
    数组中除一个数字只出现一次之外，其他数字都出现了三次
    找出出现一次的数字
    """
    if not nums or len(nums) <= 0:
        raise ValueError("Invalid input")

    len_ = len(nums)
    bit_sum = [0] * 32

    for i in range(len_):

        bit_mask = 1

        for j in range(31, 0, -1):
            bit = nums[i] & bit_mask

            if bit != 0:
                bit_sum[j] += 1

            bit_mask = bit_mask << 1

    result = 0

    for i in range(32):
        result = result << 1
        result += bit_sum[i] % 3

    return result


if __name__ == "__main__":
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    print(find_nums_appear_once(nums))
    nums_1 = [1, 1, 1, 7]
    print(find_num_appear_once(nums_1))
    
    
    from collections import Counter

    count = Counter(nums_1)
    
    for i in count.keys():
        if count[i] == 1:
            print(i)