def permutation_of_string(string):
    """字符串的排列"""
    list_ = []

    if len(string) <= 1:
        return string

    for i in range(len(string)):
        # 第一个字符为为string[i], 再置换剩余字符
        for j in map(lambda x: string[i]+x, permutation_of_string(string[:i]+string[i+1:])):
            if j not in list_:
                list_.append(j)

    return list_
            
def permutation_of_nums(nums):
    """数组的重排"""

    permutation_list = []

    if len(nums) == 1:
        permutation_list.append(nums) # append没有返回值!
        return permutation_list

    for i in range(len(nums)):
        for j in map(lambda x: x + [nums[i]], permutation_of_nums(nums[:i] + nums[i+1:])):
            if j not in permutation_list:
                permutation_list.append(j)

    return permutation_list

if __name__ == "__main__":
    nums = 'abc'
    print(permutation_of_string(nums))