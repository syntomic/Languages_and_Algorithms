def sum_of_1_to_n(n):
    """
    求1+2+...+n，要求不能用乘除法及条件判断语句
    """
    # 0 and n = 0
    return n and n + sum_of_1_to_n(n-1)

if __name__ == "__main__":
    print(sum_of_1_to_n(100))