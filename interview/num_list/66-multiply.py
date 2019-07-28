def multiply(A):
    """
    构建乘积数组，不能使用除法
    B[i] = A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
    """
    n = len(A)
    B = [1] * n
    C = [1] * n
    D = [1] * n

    # 自上而下
    for i in range(1, n):
        C[i] = C[i-1] * A[i-1]

    # 自下而上
    for j in range(n-2, -1, -1):
        D[j] = D[j+1] * A[j+1]

    for k in range(n):
        B[k] = C[k] * D[k]

    return B


if __name__ == "__main__":
    nums_A = [i for i in range(1,6)]
    print(multiply(nums_A))