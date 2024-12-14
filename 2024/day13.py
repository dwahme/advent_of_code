from helpers import *

def get_toks(a, c, b, d, p, q, add=0):
    p += add
    q += add

    x = (b*q-d*p) / (b*c - a*d)
    y = (a*q-c*p) / (a*d - b*c)

    return int(x*3 + y) if x == int(x) and y == int(y) else 0

def task1(data):
    return sum(get_toks(*d) for d in data)

def task2(data):
    return sum(get_toks(*d, add=10000000000000) for d in data)

if __name__ == "__main__":
    lines = get_input("sample-13")
    lines = get_input("13")
    lines = [l.strip() for l in lines]

    data = []
    for i in range(0, len(lines), 4):
        a, c = tuple(find_nums(lines[i]))
        b, d = tuple(find_nums(lines[i+1]))
        p, q = tuple(find_nums(lines[i+2]))

        data.append((a,c,b,d,p,q))

    # print(data)
    
    print(task1(data))
    print(task2(data))
