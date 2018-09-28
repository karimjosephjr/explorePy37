from king import King
from bishop import Bishop
from knight import Knight
from rook import Rook
from queen import Queen
from player import Player

from colorama import init
from colorama import Back, Style
init()


class Board:
    def __init__(self):
        self.board = self.make_board()
        self.grid = self.make_grid()
        self.inverted_grid = self.invert_grid()

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

    def invert_grid(self):
        inverted_grid = {}
        for k, v in self.grid.items():
            inverted_grid[v] = k
        return inverted_grid

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

thing1 = Bishop(color='white')
thing2 = King(color='white')
print(thing1.check_direction((3, 3), (1, 1), some_board))
print("\n\n\n")

#Knight and Rook tests
some_board.board[7][1].piece = Knight()
some_board.board[7][0].piece = Rook()
some_board.board[3][4].piece = Queen()
some_board.board[4][3].piece = Queen(color='black')
some_board.board[2][3].piece = Queen(color='black')
some_board.board[4][5].piece = Queen(color='black')
some_board.board[2][5].piece = Queen(color='black')

player1 = Player()
print(some_board)
print("\n\n\n")
while not some_board.board[0][0].piece:
    player1.make_a_move(some_board)
    print(some_board)
    print("\n\n\n")

# Piece pretty print test
# print(some_board.inverted_grid)
# print(Player.print_move_options((7, 1), some_board))


# print(some_board.board[3][3].piece.move_options((3, 3)))
# a7 = some_board.get_coords('a7')
# f2 = some_board.get_coords('f2')
# some_board.update_board(a7, f2)
# print(some_board)
#
# player1 = Player()
#
# player1.make_a_move(some_board)
# print(some_board)
