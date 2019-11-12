def print_number(n):
    """从1到最大的n位数"""
    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    # 生成器
    number = ( x for x in range(1, pow(10, n)))
    for i in number:
        print(i, end=',')

if __name__ == "__main__":
    n = 3
    print_number(n)