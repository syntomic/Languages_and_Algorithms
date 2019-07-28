def last_remaining(n, m):
    """
    n个数排成一个圆圈，从数字0开始，每次删除第m个数字，
    求出这个圆圈里剩下的最后一个数字
    """
    if n < 1 or m < 1:
        return -1

    last = 0

    for i in range(2, n+1):
        ## math, go, math!
        last = (last + m) % i

    return last

if __name__ == '__main__':
    print(last_remaining(5, 3))