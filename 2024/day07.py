import helpers

def try_op(target, cur, lst, bar=False):
    if not lst:
        return cur == target

    x, *rest = lst
    return try_op(target, cur + x, rest, bar) or try_op(target, cur * x, rest, bar) or (bar and try_op(target, int(f"{cur}{x}"), rest, bar))

def task1(data):
    return sum(target for target, lst in data if try_op(target, 0, lst))

def task2(data):
    return sum(target for target, lst in data if try_op(target, 0, lst, bar=True))

if __name__ == "__main__":
    lines = helpers.get_input("07")
    lines = [l.strip().split() for l in lines]
    data = [(int(l[0][:-1]), [int(i) for i in l[1:]]) for l in lines]
    
    print(task1(data))
    print(task2(data))
