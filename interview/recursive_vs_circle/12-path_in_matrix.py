def has_path(matrix, rows, cols, path):
    """
    判断路径是否在矩阵中
    参数：
        matrix:list[int]
        rows:int
        cols:int
        path:str
    返回值：
        bool:Ture or False
    """
    if matrix == None or rows < 1 or cols < 1 or path == None:
        return False

    visited = [0] * (rows * cols)
    path_length = 0

    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, path, path_length, visited):
                return True
    return False

def has_path_core(matrix, rows, cols, row, col, path, path_length, visited):
    """
    第path_length开始的path是否在第row行，第col列开始的矩阵中
    """
    if len(path) == path_length:
        return True

    found  = False

    if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[path_length] and not \
    visited[row * cols + col]:

        path_length += 1
        visited[row * cols + col] = True

        found = has_path_core(matrix, rows, cols, row, col - 1, path, path_length, visited) or \
                    has_path_core(matrix, rows, cols, row - 1, col, path, path_length, visited) or \
                    has_path_core(matrix, rows, cols, row, col + 1, path, path_length, visited) or \
                    has_path_core(matrix, rows, cols, row + 1, col, path, path_length, visited)

        if not found:
            path_length -= 1
            visited[row * cols + col] = False

    return found

if __name__ == "__main__":
    matrix = ['a', 'b', 't', 'g', 'c', 'f', 'c', 's', 'j', 'd', 'e', 'h']
    print(has_path(matrix, 3, 4, 'btg'))
    print(has_path(matrix, 3, 4, 'bw'))
    
