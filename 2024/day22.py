from helpers import *
from grid import *
from functools import cache

def mix(num, secret):
    return num ^ secret

def prune(num):
    return num % 16777216

@cache
def next_secret(secret):
    # secret = prune(mix(secret, secret << 6))
    # secret = prune(mix(secret, secret >> 5))
    # secret = prune(mix(secret, secret << 10))
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))

    return secret

def price(x):
    return x % 10

def task1(nums):

    tot = 0

    for n in nums:
        x = n
        for _ in range(2000):
            x = next_secret(x)
        tot += x

    return tot

def task2(nums):
    d = {}

    for n in nums:
        x = n
        prev = None
        deltas = []
        found = set()

        for _ in range(2000):
            prev = x
            x = next_secret(x)

            deltas.append(price(x) - price(prev))

            if len(deltas) > 4:
                deltas.pop(0)

            if len(deltas) == 4:
                t = tuple(deltas)
                if t not in found:
                    d[t] = d.get(t, 0) + price(x)
                    found.add(t)

    # print(d)

    return max(d.items(), key=lambda t: t[1])[1]

if __name__ == "__main__":
    lines = get_input("sample-22")
    lines = get_input("22")
    nums = [int(l.strip()) for l in lines]
    
    print(task1(nums))
    print(task2(nums))
