import helpers

GUARDS = "^>V<"
DX_DYS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_next_move(grid, guard_x, guard_y):
    dx, dy = DX_DYS[GUARDS.index(grid[guard_y][guard_x])]
    return guard_x + dx, guard_y + dy

def dump_grid(grid):
    for line in grid:
        print("".join(line))

def run_sim(starting_grid, cur_x, cur_y, barrier_x=None, barrier_y=None):

    grid = [l.copy() for l in starting_grid]
    
    if barrier_x is not None and barrier_y is not None:
        grid[barrier_y][barrier_x] = "O"

    move_list = set()

    while True:
        new_x, new_y = get_next_move(grid, cur_x, cur_y)

        # infinite loop detected
        move = ((cur_x, cur_y), (new_x, new_y))
        if move in move_list:
            return grid, True

        # guard walked off grid
        if not (0 <= new_y < len(grid)) or not (0 <= new_x < len(grid[new_y])):
            grid[cur_y][cur_x] = "X"
            return grid, False

        # rotate the guard
        if grid[new_y][new_x] == "#" or grid[new_y][new_x] == "O":
            grid[cur_y][cur_x] = GUARDS[(GUARDS.index(grid[cur_y][cur_x]) + 1) % len(GUARDS)]

        # move the guard
        else:
            grid[new_y][new_x], grid[cur_y][cur_x] = grid[cur_y][cur_x], "X"
            move_list.add(move)
            cur_x, cur_y = new_x, new_y

    return None

def task1(grid, start_x, start_y):
    new_grid, _ = run_sim(grid, start_x, start_y)
    return sum([c == "X" for row in new_grid for c in row])


def task2(grid, start_x, start_y):

    total = 0

    solved_grid, _ = run_sim(grid, start_x, start_y)
    solved_grid[start_y][start_x] = "^"

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if solved_grid[y][x] == "X":
                new_grid = [l.copy() for l in grid]
                _, loop_detected = run_sim(new_grid, start_x, start_y, x, y)
                
                if loop_detected:
                    # dump_grid(new_grid)
                    total += 1

    return total

if __name__ == "__main__":
    lines = helpers.get_input("06")
    lines = [list(l.strip()) for l in lines]

    start_y = [y for y in range(len(lines)) if "^" in lines[y]][0]
    start_x = [x for x in range(len(lines[start_y])) if "^" in lines[start_y][x]][0]
    
    print(task1(lines, start_x, start_y))
    print(task2(lines, start_x, start_y))
