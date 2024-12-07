import helpers

def try_op(target, cur_total, lst, allow_bar=False):
    # print(f"trying to hit {target} from {cur_total}... {lst}")
    if not lst:
        # if cur_total == target:
            # print("found!")
        return cur_total == target

    x, rest = lst[0], lst[1:]

    add = try_op(target, cur_total + x, rest, allow_bar=allow_bar)
    mul = try_op(target, cur_total * x, rest, allow_bar=allow_bar)

    bar = False
    if allow_bar:
        bar = try_op(target, int(str(cur_total) + str(x)), rest, allow_bar=allow_bar)

    return add or mul or bar

def task1(data):

    total = 0
    for target, lst in data:
        # print(target, lst, try_operations(target, lst))
        # total += target if try_operations(target, lst) else 0
        total += target if try_op(target, 0, lst) else 0

    return total

def task2(data):

    total = 0
    for target, lst in data:
        # print(target, lst, try_operations(target, lst))
        total += target if try_op(target, 0, lst, allow_bar=True) else 0
    return total

if __name__ == "__main__":
    lines = helpers.get_input("07")
    lines = [l.strip().split() for l in lines]

    data = [(int(l[0][:-1]), [int(i) for i in l[1:]]) for l in lines]
    for d in data:
        print(d)
    
    print(task1(data))
    print(task2(data))
