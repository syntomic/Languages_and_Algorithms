def count_of_1(n):
    """
    整数的二进制表示中1的个数(补码表示)
    """
    count = 0

    # 转化为正数，1的个数不变
    if n < 0:
        n = n & 0xff

    while n != 0:

        count += 1
        n = (n - 1) & n # 把n的最左边的1变为0

    return count

if __name__ == "__main__":
    # -8的补码为 11111000
    print(count_of_1(-8))