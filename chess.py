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
        for x in range(8):
            board.append([])
            for y in range(8):
                board[x].append(Space(x, y))
        return board

    @staticmethod
    def make_grid():
        grid = {}
        for coord_2, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            for coord_1, num in enumerate(range(8, 0, -1)):
                grid[f'{letter}{num}'] = (coord_1, coord_2)
        return grid

    def board_str(self):
        letters = ['  ', ' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ', '\n']
        array_of_array_of_str_spaces = [[str(x) for x in y] for y in self.board]
        array_of_str_spaces = []
        for row, label in enumerate(range(8, 0, -1)):
            array_of_str_spaces.append(str(label) + ' ' + ''.join(array_of_array_of_str_spaces[row]) + Style.RESET_ALL)
        return ''.join(letters) + '\n'.join(array_of_str_spaces)

    def __str__(self):
        return self.board_str()

    def update_board(self, start, end):
        self.board[end[0]][end[0]].piece = self.board[start[0]][start[1]].piece
        self.board[start[0]][start[1]].piece = None


class Space:
    def __init__(self, x, y):
        self.position = (x, y)
        self.piece = None
        self.whiteIsThreatened = None
        self.blackIsThreatened = None
        self.color = self.set_space_color(x, y)

    @staticmethod
    def set_space_color(x, y):
        if (x + 2) % 2 == 0 and (y + 2) % 2 == 0:
            color = Back.WHITE
        elif (x + 2) % 2 != 0 and (y + 2) % 2 != 0:
            color = Back.WHITE
        else:
            color = Back.BLACK
        return color

    def __str__(self):
        if self.piece:
            return self.color + str(self.piece)
        else:
            return self.color + '   '


# test cases
some_board = Board()
print(some_board.grid)
print(some_board)
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