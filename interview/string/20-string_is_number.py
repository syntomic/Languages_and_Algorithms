def is_numeric(string):
    """
    判断字符串是否表示数值
    其中数值形如A[.[B]][e|E C]或.B[e|E C]，A，B，C为整数，B无符号，C可能有符号
    """
    allow_dot = True
    allow_e = True

    for i in range(len(string)):
        # 处理 '+-'
        if string[i] in "+-" and (i==0 or string[i-1] in "eE") and i < len(string)-1:
            continue
        # 处理 '.'
        elif allow_dot and string[i] == ".":
            allow_dot = False
            if i >= len(string)-1 or string[i+1] not in "0123456789":
                return False
        # 处理 'Ee'
        elif allow_e and string[i] in "Ee":
            allow_dot = False
            allow_e = False
            if i >= len(string)-1 or string[i+1] not in "0123456789+-":
                return False
        # 处理整数
        elif string[i] not in "0123456789":
            return False
    return True
    
"""
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
"""

if __name__ == "__main__":
    string1 = '3.1212e+5'
    string2 = '+-5'
    print(is_numeric(string1))
    print(is_numeric(string2))
