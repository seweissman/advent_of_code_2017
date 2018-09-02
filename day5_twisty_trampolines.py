"""
Day 5: A Maze of Twisty Trampolines, All Alike
"""

def maze_steps(maze, jump_fun):
    steps = 0
    loc = 0
    while loc < len(maze) and loc >= 0:
        # print(maze, loc)
        jump = maze[loc]
        maze[loc] = jump_fun(jump)
        loc = loc + jump
        steps += 1
    return steps

maze = [0, 3, 0, 1, -3]
def add_one(j):
    return j + 1

def strange(j):
    if j >= 3:
        return (j - 1)
    return (j + 1)

assert maze_steps(maze.copy(), add_one) == 5
assert maze_steps(maze.copy(), strange) == 10

if __name__ == "__main__":
    file_in = open("day5.input.txt")
    INPUT = file_in.read()
    INPUT = INPUT.strip()
    maze_list = INPUT.split("\n")
    maze_list = [int(x) for x in maze_list]
    print(maze_steps(maze_list.copy(), add_one))
    print(maze_steps(maze_list.copy(), strange))
