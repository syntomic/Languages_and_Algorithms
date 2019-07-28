from SQueue import SQueue # pylint: disable=import-error

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False

def maze_solver_queue(maze, start, end):
    """基于队列的迷宫解法"""
    # 需要额外记录路径，可以采用字典
    if start == end:
        print("Path finds.")
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print("Path find.")
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)
    print("No Path.")

if __name__ == "__main__":
    maze = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,1,1,1]]
    start =(1, 1)
    end = (3, 3)
    maze_solver_queue(maze, start, end)