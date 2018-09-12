from colorama import init
from colorama import Fore, Back, Style
init()


class Board:
    def __init__(self):
        self.board = []
        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append(Space(x, y))

    def __str__(self):
        board_array = [[str(Back.WHITE + Fore.BLACK + ' K ' if x.color == "white"
                            else Back.BLACK + ' K ') for x in y] for y in self.board]
        board_array2 = []
        for y in board_array:
            board_array2.append(''.join(y) + Style.RESET_ALL)
        return Back.BLACK + '\n'.join(board_array2)

    def get_space(self, x, y):
        return self.board[y][x]


class Space:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        self.piece = None
        if (self.x + 2) % 2 == 0 and (self.y + 2) % 2 == 0:
            self.color = "white"
        elif (self.x + 2) % 2 != 0 and (self.y + 2) % 2 != 0:
            self.color = "white"
        else:
            self.color = "black"

    def __str__(self):
        return self.color


some_board = Board()
print(some_board)
