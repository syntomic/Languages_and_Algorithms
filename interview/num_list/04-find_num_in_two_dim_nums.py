def find_num_in_two_dim_nums(num, matrix, rows, columns):
    """
    二位数组，行，列递增，判断一个整数是否在该数组中
    参数：
        num: int
        matrix: list[int]
        rows: int
        columns: int
    返回：
        boolean:True or False
    """
    found = False

    # 从左上角开始查找
    if matrix and rows > 0 and columns > 0:

        row = 0
        column = columns - 1

        while row < rows and column >= 0: 
            if matrix[row * columns + column] == num:
                found = True
                break
            elif matrix[row * columns + column] > num:
                column -= 1
            else:
                row += 1
    
    return found

if __name__ == "__main__":
    num = 7
    matrix = [1, 2, 8, 9, 2, 4, 9, 12, 4, 8, 10, 13, 7, 9, 11, 15]
    # 没有查找的数字
    # 空数组
    print(find_num_in_two_dim_nums(num, matrix, 4, 4))
