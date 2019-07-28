def string_to_int(string):
    """将字符串转化为整数"""
    str_num = [str(i) for i in range(10)]

    sum_ = 0
    label = 1
    len_ = len(string)

    for i in range(len_):
        if i == 0:
            if string[i] == '-':
                label = -1
                continue
            if string[i] == '+':
                continue
        
        if string[i] in str_num:
            sum_ = sum_ * 10 + str_num.index(string[i])
        else:
            break
        
    return sum_ * label

if __name__ == "__main__":
    string = '-12123'
    print(string_to_int(string))
    print(int(string))

