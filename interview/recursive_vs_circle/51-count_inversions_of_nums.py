def count_inversions_and_sort(nums1, nums2):
    """合并两个排序数组并计算逆序数"""
    nums = []
    num_inv = 0
    i = 0
    j = 0
    l1 = len(nums1)
    l2 = len(nums2)

    for _ in range(l1 + l2):
        if i == l1:
            nums += [nums2[x] for x in range(j, l2)]
            break
        if j == l2:
            nums += [nums1[x] for x in range(i, l1)]
            break
            
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1          
            num_inv += (l1 - i)
            
    return (num_inv, nums)

    
def sort_and_count_inversions(nums):
    """数组中的逆序对"""
    if len(nums) == 1:
        return (0, nums)
    
    i = len(nums) >> 1

    l_inv, left = sort_and_count_inversions(nums[0:i])
    r_inv, right = sort_and_count_inversions(nums[i:])
    split_inv, merged = count_inversions_and_sort(left, right)

    return (l_inv + r_inv + split_inv, merged)

if __name__ == "__main__":
    nums = [2, 3, 5, 4, 1]
    print(sort_and_count_inversions(nums))