from king import King
from player import Player

from colorama import init
from colorama import Back, Style
init()


class Board:
    def __init__(self):
        self.board = self.make_board()
        self.grid = self.make_grid()

    def __str__(self):
        return self.board_str()

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

    def update_board(self, start, end):
        self.board[end[0]][end[1]].piece = self.board[start[0]][start[1]].piece
        self.board[start[0]][start[1]].piece = None

    def get_coords(self, coords_str):
        coords_str = str(coords_str).lower()
        coords_tuple = self.grid.get(coords_str, None)
        return coords_tuple


class Space:
    def __init__(self, x, y):
        self.position = (x, y)
        self.piece = None
        self.whiteIsThreatened = None
        self.blackIsThreatened = None
        self.color = self.set_space_color(x, y)

    def __str__(self):
        return self.space_str()

    @staticmethod
    def set_space_color(x, y):
        if (x + 2) % 2 == 0 and (y + 2) % 2 == 0:
            color = Back.WHITE
        elif (x + 2) % 2 != 0 and (y + 2) % 2 != 0:
            color = Back.WHITE
        else:
            color = Back.BLACK
        return color

    def space_str(self):
        if self.piece:
            result = self.color + str(self.piece)
        else:
            result = self.color + '   '
        return result


# test cases
some_board = Board()
print(some_board.grid)
print("\n\n\n")

some_board.board[1][0].piece = King()
print(some_board)
print("\n\n\n")

a7 = some_board.get_coords('a7')
f2 = some_board.get_coords('f2')
some_board.update_board(a7, f2)
print(some_board)

player1 = Player()

player1.make_a_move(some_board)
print(some_board)
