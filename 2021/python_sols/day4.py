

def parse_numbers(line, splitchar=" "):
    return [int(i) for i in line.split(splitchar) if i not in ["", "\n"]]


class Board:

    def __init__(self, lines):
        self.board = Board.parse_board(lines)
        self.markers = [[False] * 5 for _ in range(5)]

    def parse_board(lines):
        board = []

        for line in lines:
            board.append(parse_numbers(line))

        return board

    def call_number(self, number):
        for i, line in enumerate(self.board):
            for j, x in enumerate(line):
                if number == x:
                    self.markers[i][j] = True

    def is_winner(self):
        # check horizontal
        for line in self.markers:
            if all(x == True for x in line):
                return True

        # check vertical
        for j in range(len(self.markers[0])):
            cur = True
            for i in range(len(self.markers)):
                cur = cur and self.markers[i][j]
            
            if cur == True:
                return True

        return False

    def print_board(self):
        for i, line in enumerate(self.board):
            for j, num in enumerate(line):
                s = "*" if self.markers[i][j] else " "
                s += str(num)
                s = " " * (3-len(str(num))) + s
                print(s, end = "")
            print("")
    
    def board_sum(self):
        board_sum = 0
        
        for i, line in enumerate(self.board):
            for j, x in enumerate(line):
                if self.markers[i][j] == False:
                    board_sum += x

        return board_sum

def parse(lines):

    numbers = parse_numbers(lines[0], splitchar=",")

    boards = []
    for i in range(2, len(lines), 6):

        board_lines = lines[i:i+5]
        boards.append(Board(board_lines))

    return numbers, boards

def play_bingo(numbers, boards):

    last_board = None
    last_called = None

    for n in numbers:
        print("------------------------")
        print(f"calling: {n}")
        for b in boards:
            b.call_number(n)
            if b.is_winner():
                last_board = b
                last_called = n
        
        boards = [b for b in boards if not b.is_winner()]

    return last_board, last_called


if __name__ == "__main__":

    lines = None
    with open("../inputs/day4.txt", "r") as f:
        lines = f.readlines()

    numbers, boards = parse(lines)
    winner, last_number = play_bingo(numbers, boards)

    print("\n\nwinner:")
    winner.print_board()
    print(winner.board_sum() * last_number)
