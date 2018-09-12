from colorama import init
from colorama import Fore, Back, Style
init()


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append("space")

    def __str__(self):
        return str(self.board)


some_board = Board()
print(some_board)
