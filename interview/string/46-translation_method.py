def get_translation_count(num):
    """
    把数字翻译成字符串，计算有多少不同的翻译方法
    :type number: int
    :rtype: int
    """
    if num < 0:
        return 0

    str_ = str(num)
    length = len(str_)
    counts = [0] * length

    # 从数字的末尾开始
    for i in range(length-1, -1, -1):
        count = 0

        if i < length-1:
            count += counts[i+1]
        else:
            count = 1
        
        if i < length-1:

            digit1 = int(str_[i])
            digit2 = int(str_[i+1])
            converted = digit1*10 + digit2

            if converted >= 10 and converted <= 25:
                if i < length-2:
                    count += counts[i+2]
                else:
                    count += 1
        counts[i] = count
        
    return counts[0]

        
if __name__=="__main__":
    print(get_translation_count(12258))
    print(get_translation_count(12319))
    print(get_translation_count(-3))
    print(get_translation_count(0))
    print(get_translation_count(5))

    