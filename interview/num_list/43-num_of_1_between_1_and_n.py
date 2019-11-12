def num_of_1_between_1_and_n(n):
    """1~n整数1出现的次数"""
    if not isinstance(n, int):
        raise TypeError("input is not a integer")

    if n <= 0:
        return 0

    return number_of_1(str(n))

def number_of_1(str_n):
    """转化为字符便于操作"""
    len_ = len(str_n)
    first = int(str_n[0])

    if len_ == 1 and first == 0:
        return 0

    if len_ == 1 and first > 0:
        return 1

    num_first_digit = 0

    # 最高位出现1的次数 
    if first > 1:
        num_first_digit = pow(10, len_-1)  # 1346 ~ 21345
    elif first == 1:
        num_first_digit = int(str_n[1:]) + 1 # 12345

    # 出现在最高位之外的其他位为1的次数
    num_other_digits = first * (len_ - 1) * pow(10, len_ - 2)

    # 去掉最高位递归
    num_recursive = number_of_1(str_n[1:]) # 2345

    return num_first_digit + num_other_digits + num_recursive


if __name__ == "__main__":
    print(num_of_1_between_1_and_n(12))
    print(num_of_1_between_1_and_n(21345))