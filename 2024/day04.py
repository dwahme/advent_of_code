import helpers

def task1(grid):
    base_dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    return sum([helpers.find_string_in_grid(grid, "XMAS", x, y, dx, dy, allow_backwards=True) for y in range(len(grid)) for x in range(len(grid[y])) for (dx, dy) in base_dirs])

def check_cross(grid, x, y):
    if grid[y][x] != "A":
        return False

    return set(list("MS")) == set(grid[y+1][x+1] + grid[y-1][x-1]) == set(grid[y+1][x-1] + grid[y-1][x+1])

def task2(grid):
    return sum([check_cross(grid, x, y) for y in range(1, len(grid) - 1) for x in range(1, len(grid[y]) - 1)])

if __name__ == "__main__":
    lines = helpers.get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
