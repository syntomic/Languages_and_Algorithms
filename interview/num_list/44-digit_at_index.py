def digit_at_index(index):
    """数字序列0123456789101112...的某一位数字"""
    if index < 0:
        return -1

    digits = 1

    while True:
        count = count_of_integers(digits)

        if index < count * digits: # n位数一共有 count*digits 个数
            return digit_at_index_with_count(index, digits)

        index -= count * digits
        digits += 1


def count_of_integers(digits):
    """m位的数字总共有多少"""
    if digits == 1:
        return 10

    count = 9 * pow(10, digits - 1)

    return count
    

def digit_at_index_with_count(index, digits):
    """知道index指向的数是m位数的前提下，返回index指向的数字"""

    number = begin_number(digits) + index // digits
    index_from_right = digits - index % digits

    for i in range(1, index_from_right):
        number //= 10

    return number % 10
    
    
def begin_number(digits):
    """返回m位数的第一个数"""
    if digits == 1:
        return 0

    return pow(10, digits - 1)

if __name__ == "__main__":
    print(digit_at_index(5))
    print(digit_at_index(13))
    print(digit_at_index(19))