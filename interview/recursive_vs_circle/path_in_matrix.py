from collections import deque

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(matrix, pos):
    matrix[pos[0]][pos[1]] = 1

def passable(matrix, pos, path, path_length):
    return matrix[pos[0]][pos[1]] == path[path_length]

def has_path(matrix, path):

    rows = len(matrix) + 2
    cols = len(matrix[0]) + 2

    matrix_with_1 = [0] * rows

    for i in range(rows):
        if i == 0 or i == rows - 1:
            matrix_with_1[i] = [1] * cols
        else:
            matrix_with_1[i] = [1] + matrix[i-1] + [1]
 
    path_length = 0

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if matrix_with_1[row][col] == path[0]:
                return has_path_core(matrix_with_1, row, col, path, path_length)

    return False

def has_path_core(matrix, row, col, path, path_length):
    if len(path) == 1:
        return True

    st = deque()
    pos = (row, col)
    mark(matrix, pos)
    path_length += 1
    st.append(pos)

    while st:
        pos = st.pop()
        
        found = False

        for i in range(4):
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if passable(matrix, nextp, path, path_length):
                if path_length == len(path) - 1:
                    return True

                found = True
                mark(matrix, nextp)
                st.append(nextp)

        if found:
            path_length += 1

    
    return False


if __name__ == "__main__":
    matrix = [['a', 'b', 't', 'g'],
              ['c', 'f', 'c', 's'],
              ['j', 'd', 'e', 'h']]

    path = 'gsh'

    print(has_path(matrix, path))