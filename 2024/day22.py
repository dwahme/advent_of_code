from helpers import *
from grid import *

def next_secret(secret):
    secret = (secret ^ secret << 6) % 16777216
    secret = (secret ^ secret >> 5) % 16777216
    secret = (secret ^ secret << 11) % 16777216

    return secret

def task1(nums):

    tot = 0

    for x in nums:
        for _ in range(2000):
            x = next_secret(x)
        tot += x

    return tot

def task2(nums):
    d = {}

    for x in nums:
        prev = None
        deltas = []
        found = set()

        for _ in range(2000):
            prev = x
            x = next_secret(x)

            deltas.append(x % 10 - prev % 10)

            if len(deltas) > 4:
                deltas.pop(0)

            if len(deltas) == 4:
                t = tuple(deltas)
                if t not in found:
                    d[t] = d.get(t, 0) + x % 10
                    found.add(t)

    return max(d.values())

if __name__ == "__main__":
    lines = get_input("sample-22")
    lines = get_input("22")
    nums = [int(l.strip()) for l in lines]
    
    print(task1(nums))
    print(task2(nums))
