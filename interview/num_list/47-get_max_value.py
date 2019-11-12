def get_max_value(values, rows, cols):
    """礼物的最大价值"""
    if not values or rows <= 0 or cols <= 0:
        return 0

    # [f(i,0),f(i,1),...,f(i,j-1),f(i-1,j),f(i-1,j+1),...,f(i-1,n-1)]
    max_values = [0]* cols

    for i in range(rows):
        for j in range(cols):
            left = 0
            up = 0

            if i > 0:
                up = max_values[j]

            if j > 0:
                left = max_values[j-1]
                
            # f(i, j) = max(f(i-1,j),f(i,j-1)) + gift[i,j]
            max_values[j] = max(left, up) + values[i*cols+j]

    max_value = max_values[-1]

    return max_value

if __name__ == "__main__":
    values = [1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5]
    print(get_max_value(values, 4, 4))