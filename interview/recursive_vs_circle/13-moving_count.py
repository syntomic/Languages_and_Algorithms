from collections import deque

dirs = [(0,1), (1,0), (0,-1), (-1, 0)]

def judge(threshold, i, j):
    """
    判断能否到达(i,j)
    """
    if sum(map(int,str(i)+str(j))) <= threshold:
        return True
    else:
        return False

def findgrid_recursive(threshold, rows, cols, matrix, i, j):
    """
    从位置(i,j)开始机器人活动范围，递归方法
    """
    # 容易导致栈溢出，最好改成循环，添加辅助栈
    count = 0
    if i<rows and j<cols and i>=0 and j>=0 and judge(threshold,i,j) and matrix[i][j]==0:

        matrix[i][j] = 1

        count = 1 + findgrid_recursive(threshold, rows, cols, matrix, i, j+1) \
        + findgrid_recursive(threshold, rows, cols, matrix, i, j-1) \
        + findgrid_recursive(threshold, rows, cols, matrix, i+1, j) \
        + findgrid_recursive(threshold, rows, cols, matrix, i-1, j)
    return count

def findgrid_circle(threshold, rows, cols, matrix, i, j):
    """
    从位置(i,j)开始机器人活动范围，循环方法
    """
    st = deque()
    matrix[i][j] = 1
    st.append((i,j))
    count = 1

    while st:
        pos = st.pop()
        for i in range(4):

            m, n = pos[0] + dirs[i][0], pos[1] + dirs[i][1]

            if m < rows and n < cols and m >= 0 and n >= 0 and judge(threshold, m, n) and matrix[m][n]==0:

                count += 1
                matrix[m][n] = 1
                st.append((m,n))

    return count


def moving_count(threshold, rows, cols):
    """
    机器人的活动范围
    参数：
        threshold:int 最大坐标位数之和
        rows:int 行数
        cols:int 列数
    返回：
        count:int 到达格子的数码
    """
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    #count = findgrid_recursive(threshold, rows, cols, matrix, 0, 0)
    count = findgrid_circle(threshold, rows, cols, matrix, 0, 0)
    #print(matrix)
    return count

if __name__ == "__main__":
    threshold = 18
    rows = 40
    cols = 40
    print(moving_count(threshold, rows, cols))
