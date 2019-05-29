def print_matrix_clockwise(matrix):
    """
    顺时针打矩阵
    参数：
        martix: list[list[int]]
    """
    if not matrix:
        return 
    
    row_len = len(matrix)
    # 需要判断一下matrix[0]
    col_len = len(matrix[0])

    # 计算出打印圈数
    circle = 0
    i = 0
    while i < row_len -1 and i < col_len - 1:
        circle += 1
        i += 1
        
    # 顺时针打印
    i = 0
    while i < circle:

        for j in range(i, col_len-i):
            print(matrix[i][j], end=', ')

        for k in range(i+1, row_len-i):
            print(matrix[k][col_len-i-1], end=', ')

        for s in range(col_len-i-2,i-1,-1):
            print(matrix[row_len-i-1][s], end=', ')

        for t in range(row_len-i-2,i,-1):
            print(matrix[t][i], end=', ')

        i += 1


if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix_1 = [[1,2,3], [5,6,7], [9,10,11], [13,14,15]]
    matrix_2 = [[1,2,3],[4,5,6]]
    print_matrix_clockwise(matrix)
    print()
    print_matrix_clockwise(matrix_1)
    print()
    print_matrix_clockwise(matrix_2)