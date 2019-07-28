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
        return str(self) + str(another) < str(self) + str(another)

if __name__ == "__main__":
    nums = [3, 32, 321]
    print(print_min_num(nums))





