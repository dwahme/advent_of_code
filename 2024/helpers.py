
def _reduce_list(arg):
    if type(arg) == list and len(arg) > 2:
        return [_reduce_list(a) for a in arg[:2]] + ["..."]

    return arg

def _get_str_arg(arg):
    return str(_reduce_list(arg)).replace("'...'", "...")

def call_and_print(fn, *args):
    str_args = ", ".join(_get_str_arg(arg) for arg in args)

    result = fn(*args)

    print(f"{fn.__name__}({str_args}) = {result}")
    return result

def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines

def get_input(file_code):
    return get_lines(f"inputs\{file_code}.in")

def find_string_in_grid(grid: list[list[str]], string: str, x: int, y: int, dx: int, dy: int, allow_backwards=False):
    """
    grid: a list of lists where the char at position (x, y) can be accessed with grid[y][x]
    string: the string to find in the grid
    x, y: the starting position to begin searching for the string (the first letter of the string)
    dx, dy: the direction to search. (0, 1) will search one character to the right, etc
    allow_backwards: if the string is allowed to be backwards

    returns true if the string is found in that direction starting at that x, y in the grid
    false otherwise
    """
    
    str_end = len(string) - 1
    if not (0 <= y + dy*str_end < len(grid)) or not (0 <= x + dx*str_end < len(grid[y + dy*str_end])):
        return False

    s = "".join([grid[y + dy*idx][x + dx*idx] for idx in range(len(string))])
    return s == string or (allow_backwards and s[::-1] == string)
