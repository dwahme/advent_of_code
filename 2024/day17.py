from helpers import *
from math import floor

class Computer:

    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.instr_pointer = 0
        self.std_out = []
    
    def combo(self, input):
        if 0 <= input <= 3:
            return input
        if input == 4:
            return self.a
        if input == 5:
            return self.b
        if input == 6:
            return self.c
    
    def instr(self, op, input):
        next_instr = None

        match op:
            # adv (div)
            case 0:
                self.a = floor(self.a / (2 ** self.combo(input)))
            # bxl (bit xor)
            case 1:
                self.b = self.b ^ input
            # bst (bit mod)
            case 2:
                self.b = self.combo(input) % 8
            # jnz
            case 3:
                if self.a != 0:
                    next_instr = input
            # bxc (bit xor)
            case 4:
                self.b = self.b ^ self.c
            # out
            case 5:
                self.std_out.append(self.combo(input) % 8)
            # bdv
            case 6:
                self.b = floor(self.a / (2 ** self.combo(input)))
            # cdv
            case 7:
                self.c = floor(self.a / (2 ** self.combo(input)))
        
        if next_instr is None:
            next_instr = self.instr_pointer + 2
        
        self.instr_pointer = next_instr

    def run(self):
        while self.instr_pointer < len(program):
            self.instr(program[self.instr_pointer], program[self.instr_pointer + 1])
        
        return self.std_out
    
    def __repr__(self):
        return f"A: {self.a}\nB: {self.b}\nC: {self.c}\n{self.instr_pointer} -> {self.program}\n{self.std_out}"


def task1(a, b, c, program):
    com = Computer(a, b, c, program)
    out = com.run()

    return ",".join(str(s) for s in out)

def make_a(chunks):
    return sum(c << (3 * i) for i, c in enumerate(chunks[::-1]))

def solve(program, found, b, c):
    if len(found) > len(program):
        return None
    
    for i in range(8):

        a = make_a(found + [i])
        out = Computer(a, b, c, program).run()

        if out == program:
            return a

        check_digits = program[-(len(found) + 1):]
        if out == check_digits:
            s = solve(program, found + [i], b, c)
            if s is not None:
                return s

def task2(_, b, c, program):
    return solve(program, [], b, c)

if __name__ == "__main__":
    lines = get_input("sample-17-01")
    lines = get_input("sample-17-02")
    lines = get_input("17")
    lines = [l.strip() for l in lines]

    a = find_nums(lines[0], int)[0]
    b = find_nums(lines[1], int)[0]
    c = find_nums(lines[2], int)[0]
    program = find_nums(lines[4], int)

    c = Computer(a, b, c, program)

    print(task1(a, b, c, program))
    print(task2(a, b, c, program))
