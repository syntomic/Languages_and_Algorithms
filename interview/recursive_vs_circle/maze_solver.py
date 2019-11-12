from collections import deque

dirs = [(0,1), (1,0), (0,-1), (-1, 0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def maze_solver_recursive(maze, pos, end):
    """迷宫问题的递归解法"""
    mark(maze, pos)
    if pos == end:
        return True

    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if maze_solver_recursive(maze, nextp, end):
                return True
    
    return False

def maze_solver_stack(maze, pos, end):
    """迷宫问题利用栈"""
    if pos == end:
        return True

    st = deque()
    mark(maze, pos)
    st.append(pos)
    while st:
        pos = st.pop()
        for i in range(4):
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if passable(maze, nextp):
                if nextp == end:
                    return True
                print(pos)
                mark(maze, nextp)
                st.append(nextp)

    return False

def maze_solver_queue(maze, pos, end):
    """迷宫问题利用队列"""
    if pos == end:
        return True

    qu = deque()
    mark(maze, pos)
    qu.appendleft(pos)
    while qu:
        pos = qu.pop()
        for i in range(4):
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if passable(maze, nextp):
                if nextp == end:
                    return True
                mark(maze, nextp)
                qu.appendleft(nextp)

    return False

if __name__ == "__main__":
    maze_1 = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,1,1,1]]
    maze_2 = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,1,1,1]]
    maze_3 = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,1,1,1]]
    start =(1, 1)
    end = (3, 3)
    print(maze_solver_recursive(maze_1, start, end))
    print(maze_solver_queue(maze_2, start, end))
    print(maze_solver_stack(maze_3, start, end))
