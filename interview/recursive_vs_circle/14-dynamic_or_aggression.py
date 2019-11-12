def max_product_after_cutting_dynamic(length):
    """
    长度为length的绳子，求把它剪成若干段后的最大乘积，动态规划算法
    """
    if length == 0:#当长度为0时，返回0
        return 0
    if length == 1:#当长度为1时，返回1
        return 1
    if length == 2:#当长度为2时，返回1
        return 1
    if length == 3:#当长度为3时，返回2，虽然最优解数组里为2，但是每次必须得切一刀，这样1*2=2，所以长度为3时还是2
        return 2
        
    products = [0, 1, 2, 3]

    for j in range(4, length+1):
        max_ = 0
        for i in range(1, j // 2 + 1):

            temp=products[i] * products[j-i] # f(n) = max(f(i)*f(n-i))

            if temp > max_:
                max_ = temp

        products.append(max_)

    return products[-1]

def max_product_after_cutting_aggression(length):
    """
    长度为length的绳子，求把它剪成若干段后的最大乘积，贪婪算法
    """

    # 当n=length>5时，3(n-3)>=2(n-2)>n，尽可能剪成长度为3的绳子段
    # 当n=4时，2 * 2 > 1 * 3, 长度为4时不需要剪
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    timesOf3 = length // 3

    if length - timesOf3 * 3 == 1:
        timesOf3 -= 1

    timesOf2 = (length - timesOf3 * 3) // 2

    return pow(3, timesOf3) * (pow(2, timesOf2))

if __name__ == "__main__":
    print(max_product_after_cutting_aggression(100))
    print(max_product_after_cutting_dynamic(100))