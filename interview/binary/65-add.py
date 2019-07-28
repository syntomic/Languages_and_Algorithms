def add(num1, num2):
    """不用四则运算做加法"""

    while num2: # 直到不产生进位

        # 相加不进位
        sum_ = num1 ^ num2
        # 记下进位
        carry = (num1 & num2) << 1
        num1 = sum_
        num2 = carry
        
    # 也许需要做越界检查
    return num1
    

if __name__ == "__main__":
    num1 = 5
    num2 = 17
    print(add(num1, num2))