def str_replace(string):
    """
    把字符串中的每个空格替换成"%20"
    """
    # 从后面开始复制和替换
    str_len1 = len(string)
    space_num = 0

    for i in range(str_len1):
        if string[i] == ' ':
            space_num += 1

    str_len2 = str_len1 + 2 * space_num
    str_list = [''] * (str_len2)
    p = str_len1 - 1
    q = str_len2 - 1 

    while p != q:
        if string[p] != ' ':
            str_list[q] = string[p]
            p -= 1
            q -= 1
        else:
            str_list[q-2:q+1] = ['%', '2', '0']
            p -= 1
            q -= 3

    return string[0:p+1] + ''.join(str_list)


if __name__ == "__main__":
    string = "We are happy"
    print(str_replace(string))

    print(string.replace(' ', '%20'))