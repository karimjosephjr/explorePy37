from colorama import init
from colorama import Back, Style
init()


class Board:
    def __init__(self):
        self.board = self.make_board()
        self.grid = self.make_grid()

    @staticmethod
    def make_board():
        board = []
        for y in range(8):
            board.append([])
            for x in range(8):
                board[y].append(Space(x, y))
        return board

    @staticmethod
    def make_grid():
        grid = {}
        for coord_2, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            for coord_1, num in enumerate(range(7, -1, -1)):
                grid[f'{letter}{num}'] = (coord_1, coord_2)
        return grid

    def __str__(self):
        board_array = [[str(x) for x in y] for y in self.board]
        board_array2 = []
        for y in board_array:
            board_array2.append(''.join(y) + Style.RESET_ALL)
        return Back.BLACK + '\n'.join(board_array2)

    def update_board(self, start, end):
        self.board[end[1]][end[0]].piece = self.board[start[1]][start[0]].piece
        self.board[start[1]][start[0]].piece = None


class Space:
    def __init__(self, x, y):
        self.position = (x, y)
        self.piece = None
        self.whiteIsThreatened = None
        self.blackIsThreatened = None
        self.color = None
        if (x + 2) % 2 == 0 and (y + 2) % 2 == 0:
            self.color = Back.WHITE
        elif (x + 2) % 2 != 0 and (y + 2) % 2 != 0:
            self.color = Back.WHITE
        else:
            self.color = Back.BLACK

    def __str__(self):
        if self.piece:
            return self.color + self.piece
        else:
            return self.color + '   '


# test cases
some_board = Board()
print(some_board.grid)
# print(some_board)
# print("\n\n\n")
#
# some_board.board[1][0].piece = Style.BRIGHT + " K "
# print(some_board)
# print("\n\n\n")
#
# some_board.update_board((0, 1), (0, 7))
# print(some_board)
# print("\n\n\n")
#
# some_board.update_board((1, 0), (6, 7))
# print(some_board)
# print("\n\n\n")
#
# some_board.update_board((6, 7), (6, 6))
# print(some_board)
#
#
# (3, 5)