def print_min_num(nums):
    """把数组排成最小的数"""
    l = len(nums)
    
    if l == 0:
        return 
    
    sorted_numbers = sorted(map(my_int, nums))
    
    return "".join(map(str, sorted_numbers))

    
class my_int(int):
    """重新定义序"""
    def __lt__(self, another):
        return str(self) + str(another) <  str(another) + str(self)


if __name__ == "__main__":
    nums = [0, 30]
    print(print_min_num(nums))
    nums1 = [11, 5, 41]
    print(print_min_num(nums1))





