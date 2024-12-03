
import helpers
import re

def get_tokens(s):
    valid_tokens = ["mul", "\\(", "\\)", ",", "[0-9]*", "don\\'t\\(\\)", "do\\(\\)"]
    return re.findall("|".join(valid_tokens), s)

def evaluate(tokens, ignore_dont=True):
    sum = 0
    is_on = True

    for i, tok in enumerate(tokens):
        if tok == "don't()":
            is_on = False
        if tok == "do()":
            is_on = True

        if tok == "mul" and tokens[i+1] == "(" and tokens[i+2].isnumeric() and tokens[i+3] == "," and tokens[i+4].isnumeric() and tokens[i+5] == ")":
            if is_on or ignore_dont:
                sum += int(tokens[i+2]) * int(tokens[i+4])

    return sum


if __name__ == "__main__":
    lines = helpers.get_input("03")

    s = "".join(lines)

    tokens = get_tokens(s)
    print(evaluate(tokens))
    print(evaluate(tokens, ignore_dont=False))
