import helpers

def look_in_direction(grid, i, j, x, y):
    if not (0 <= y + j*3 < len(grid)) or not (0 <= x + i*3 < len(grid[y + j*3])):
        return False

    s = "".join([grid[y + j*idx][x + i*idx] for idx in range(len("XMAS"))])
    return s == "XMAS" or s[::-1] == "XMAS"

def task1(grid):
    base_dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    return len([1 for y in range(len(grid)) for x in range(len(grid[y])) for (i, j) in base_dirs if look_in_direction(grid, i, j, x, y)])

def check_cross(grid, x, y):
    if grid[y][x] != "A":
        return False

    return ["M", "S"] == sorted(grid[y+1][x+1] + grid[y-1][x-1]) == sorted(grid[y+1][x-1] + grid[y-1][x+1])

def task2(grid):
    return len([1 for y in range(1, len(grid) - 1) for x in range(1, len(grid[y]) - 1) if check_cross(grid, x, y)])

if __name__ == "__main__":
    lines = helpers.get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
