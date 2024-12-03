
import helpers
import re

def get_tokens(s):
    regex_forms = "|".join([r"mul\(([0-9]+),([0-9]+)\)", r"(do\(\))", r"(don't\(\))"])
    return re.findall(regex_forms, s)

def evaluate(tuples, ignore_dont=True):
    sum = 0
    is_on = True

    for a, b, do, dont in tuples:
        if do or dont:
            is_on = do

        if (ignore_dont or is_on) and a and b:
            sum += int(a) * int(b)

    return sum

if __name__ == "__main__":
    lines = helpers.get_input("03")

    s = "".join(lines)

    tuples = get_tokens(s)
    print(evaluate(tuples))
    print(evaluate(tuples, ignore_dont=False))
