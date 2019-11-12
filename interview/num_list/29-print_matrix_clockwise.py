def print_matrix_clockwise(matrix, columns, rows):
    """
    顺时针打矩阵
    参数：
        martix: list[list[int]]
    """
    def print_matrix_in_circle(martix, columns, rows, start):
        end_x = columns - 1 - start
        end_y = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, end_x+1):
            number = martix[start][i]
            print(number, end=', ')

        # 从上到下打印一行
        if start < end_y:
            for i in range(start+1, end_y + 1):
                number = martix[i][end_x]
                print(number, end=', ')

        # 从右到左打印一行
        if start < end_x and start < end_y:
            for i in range(end_x-1, start-1, -1):
                number = matrix[end_y][i]
                print(number, end=', ')

        # 从下到上打印一列
        if start < end_x and start < end_y - 1:
            for i in range(end_y-1, start, -1):
                number = martix[i][start]
                print(number, end=', ')

    if matrix == None or columns <= 0 or rows <= 0:
        return

    start = 0

    while columns > start * 2 and rows > start * 2:
        print_matrix_in_circle(matrix, columns, rows, start)
        start += 1
    

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix_1 = [[1,2,3], [5,6,7], [9,10,11], [13,14,15]]
    matrix_2 = [[1,2,3],[4,5,6]]
    print_matrix_clockwise(matrix, 4, 4)
    print()
    print_matrix_clockwise(matrix_1, 3, 4)
    print()
    print_matrix_clockwise(matrix_2, 3, 2)
    print()