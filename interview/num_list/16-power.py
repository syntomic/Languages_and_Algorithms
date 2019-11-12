def power(base, exponent):
    """数值的整数次方"""
    if base == exponent == 0:
        return 1
        
    if base == 0 and exponent < 0 :
        raise ValueError("Denominator cannot be error")

    # 统一成正数计算
    abs_exp = abs(exponent)
    result = abs_exponent_power(base, abs_exp)

    if exponent < 0:
        result = 1.0 / result

    return result



def abs_exponent_power(base, exponent):
    """数值的正数次方"""
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    # 二分
    result = abs_exponent_power(base, exponent >> 1)
    result *= result

    if exponent & 1 == 1:
        result *= base
    
    return result

if __name__ == "__main__":
    base = 2
    exponent = -1
    print(power(base, exponent))