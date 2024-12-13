from helpers import *
import re
import cmath

def task1(data):

    toks = 0

    for a, c, b, d, p, q in data:

        x = (b*q-d*p) / (b*c - a*d)
        y = (a*q-c*p) / (a*d - b*c)

        # j = int(j)

        # print(i, j)

        if a * int(x) + b * int(y) == p and c * int(x) + d * int(y) == q:
            # print(x, y)
            toks += x*3 + y

    return toks

def task2(data):

    toks = 0

    for a, c, b, d, p, q in data:

        p += 10000000000000
        q += 10000000000000

        x = (b*q-d*p) / (b*c - a*d)
        y = (a*q-c*p) / (a*d - b*c)

        # j = int(j)

        # print(i, j)

        if a * int(x) + b * int(y) == p and c * int(x) + d * int(y) == q:
            # print(x, y)
            toks += x*3 + y

    return toks

if __name__ == "__main__":
    lines = get_input("sample-13")
    lines = get_input("13")
    lines = [l.strip() for l in lines]

    data = []
    for i in range(0, len(lines), 4):
        a, c = re.findall("Button A: X\+([0-9]*), Y\+([0-9]*)", lines[i])[0]
        b, d = re.findall("Button B: X\+([0-9]*), Y\+([0-9]*)", lines[i+1])[0]
        p, q = re.findall("Prize: X=([0-9]*), Y=([0-9]*)", lines[i+2])[0]

        

        data.append((float(a), float(c), float(b), float(d), float(p), float(q)))

    # print(data)
    
    print(task1(data))
    print(task2(data))
