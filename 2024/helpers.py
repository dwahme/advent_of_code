
def _get_str_arg(arg):
    str_arg = str(arg)
        
    if type(arg) == list and len(arg) > 2:
        str_arg = str(arg[:2])
        str_arg = str_arg[:-1] + ", ...]"

    return str_arg

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
