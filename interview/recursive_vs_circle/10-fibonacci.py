def Fibonacci_circle(n):
    """
    Fibonacci数列，循环解法
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    i = 0
    j = 1
    k = 2 

    while k <= n:
        i, j = j, i + j
        k += 1

    return j

def Fibonacci_recursive(n):
    """
    Fibonacci数列，递归解法
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)

    # 青蛙跳台阶问题

if __name__ == "__main__":
    print(Fibonacci_recursive(6))
    print(Fibonacci_circle(6))