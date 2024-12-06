import helpers

def get_next_move(grid, guard_x, guard_y):
    if grid[guard_y][guard_x] == "^":
        return guard_x, guard_y - 1
    if grid[guard_y][guard_x] == ">":
        return guard_x + 1, guard_y
    if grid[guard_y][guard_x] == "V":
        return guard_x, guard_y + 1
    if grid[guard_y][guard_x] == "<":
        return guard_x - 1, guard_y

def dump_grid(grid):
    # return
    for line in grid:
        print("".join(line))


def run_sim(grid):

    cur_y = [y for y in range(len(grid)) if "^" in grid[y]][0]
    cur_x = [x for x in range(len(grid[cur_y])) if "^" in grid[cur_y][x]][0]

    guards = "^>V<"

    move_list = set()

    # for _ in range(10000000000):
    while True:
        # input("Press Enter to continue...")
        new_x, new_y = get_next_move(grid, cur_x, cur_y)

        move = ((cur_x, cur_y), (new_x, new_y))
        if move in move_list:
            # print("loop detected")
            return grid, True

        # if new_y >= len(grid) or new_x >= len(grid[new_y]):
        if not (0 <= new_y < len(grid)) or not (0 <= new_x < len(grid[new_y])):
            grid[cur_y][cur_x] = "X"
            break

        if grid[new_y][new_x] == "#" or grid[new_y][new_x] == "O":
            # print("rotating guard")
            # print(guards.index(grid[cur_y][cur_x]) + 1)
            # print(len(guards))
            grid[cur_y][cur_x] = guards[(guards.index(grid[cur_y][cur_x]) + 1) % len(guards)]

            # infinite loop detected
        else:
            # print("moving guard")
            grid[new_y][new_x] = grid[cur_y][cur_x]
            grid[cur_y][cur_x] = "X"
            move_list.add(move)
            cur_x, cur_y = new_x, new_y
        
    #     dump_grid(grid)
    # dump_grid(grid)

    return grid, False

def task1(grid):

    new_grid, _ = run_sim(grid)
        
    return sum([c == "X" for row in new_grid for c in row])


def task2(grid):

    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                new_grid = [l.copy() for l in grid]
                new_grid[y][x] = "O"
                _, loop_detected = run_sim(new_grid)
                
                if loop_detected:
                    # dump_grid(new_grid)
                    total += 1

    return total

if __name__ == "__main__":
    lines = helpers.get_input("06")
    lines = [list(l.strip()) for l in lines]
    
    print(task1(lines))
    print(task2(lines))
