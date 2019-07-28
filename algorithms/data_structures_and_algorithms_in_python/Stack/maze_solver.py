from SStack import SStack # pylint: disable=import-error

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def maze_solver_recursive(maze, pos, end):
    """"迷宫的递归解法"""
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if maze_solver_recursive(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False
        

def maze_solver_stack(maze, start, end):
    """"迷宫的栈解法"""
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if nextp == end:
                #print_path(end, pos, st) 将nextp和pos两个位置和栈中的位置一起输出
                return True
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, nextp)
                st.push((nextp, 0))
                break
    print("No path found.")

    #def print_path():

if __name__ == "__main__":
    maze = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,1,1,1]]
    start =(1, 1)
    end = (3, 3)
    print(maze_solver_recursive(maze, start, end))