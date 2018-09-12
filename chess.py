from colorama import init
from colorama import Fore, Back, Style
init()


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Space(i, j))

    def __str__(self):
        return str(self.board)


class Space:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        self.piece = None
        if (self.x + 2) % 2 == 0 and (self.y + 2) % 2 == 0:
            self.color = "white"
        else:
            self.color = "black"


some_board = Board()
print(some_board)
