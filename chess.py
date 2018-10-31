from king import King
from bishop import Bishop
from knight import Knight
from rook import Rook
from queen import Queen
from pawn import Pawn
from player import Player

from chesstools import assess_threat

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

    def pawn_promotion(self, pawn, end):
        options = ("q", "r", "b", "k")
        new_piece = "None"
        while new_piece.lower()[0] not in options:
            new_piece = input("What piece would you like to promote your pawn to? Your options are:\n[Q]ueen\n[R]ook\n[B]ishop\n[K]night ")
        if new_piece.lower()[0] == "q":
            self.board[end[0]][end[1]].piece = Queen(color=pawn.color)
        if new_piece.lower()[0] == "r":
            self.board[end[0]][end[1]].piece = Rook(color=pawn.color)
        if new_piece.lower()[0] == "b":
            self.board[end[0]][end[1]].piece = Bishop(color=pawn.color)
        if new_piece.lower()[0] == "k":
            self.board[end[0]][end[1]].piece = Knight(color=pawn.color)

    def update_board(self, start, end):
        self.board[end[0]][end[1]].piece = self.board[start[0]][start[1]].piece
        self.board[start[0]][start[1]].piece = None
        
        #special instructions for moving Kings
        if isinstance(self.board[end[0]][end[1]].piece, King):
            current_king = self.board[end[0]][end[1]].piece        
            # update has_moved once the king has moved
            if not current_king.has_moved:
                current_king.has_moved = True
            #if the King castled, the corresponding Rook must be moved as well
            if end == (start[0],start[1]-2):
               self.board[end[0]][end[1]+1].piece = self.board[start[0]][start[1]-4].piece
               self.board[end[0]][end[1]+1].piece.has_moved = True
               self.board[start[0]][start[1]-4].piece = None
            if end == (start[0],start[1]+2):
               self.board[end[0]][end[1]-1].piece = self.board[start[0]][start[1]+3].piece
               self.board[end[0]][end[1]-1].piece.has_moved = True
               self.board[start[0]][start[1]+3].piece = None
               
        #update has_moved attribute for Rooks
        if isinstance(self.board[end[0]][end[1]].piece, Rook):
            if not self.board[end[0]][end[1]].piece.has_moved:
                self.board[end[0]][end[1]].piece.has_moved = True
                
        # Reset double_move_flag to False for all Pawns
        for row in self.board:
            for space in row:
                if space.piece and isinstance(space.piece, Pawn):
                    space.piece.double_move_flag = False

        # Special instructions for moving Pawns
        if isinstance(self.board[end[0]][end[1]].piece, Pawn):
            current_pawn = self.board[end[0]][end[1]].piece
            # Update double_move_flag by comparing start and end
            if end in ((start[0]+2, start[1]), (start[0]-2, start[1])):
                current_pawn.double_move_flag = True
            # update has_moved once the pawn has moved
            if not current_pawn.has_moved:
                current_pawn.has_moved = True
            # if a pawn reaches the top or bottom of the board it must be promoted
            if end[0] in (0, 7):
                self.pawn_promotion(current_pawn, end)
            # if a pawn takes an en passant move, it captures the pawn that was adjacent to it's starting position
            if current_pawn.passant_left and end == (start[0] + current_pawn.color_mod, start[1] - 1):
                self.board[start[0]][start[1]-1].piece = None
            if current_pawn.passant_right and end == (start[0] + current_pawn.color_mod, start[1] + 1):
                self.board[start[0]][start[1] + 1].piece = None

    def get_coords(self, coords_str):
        coords_str = str(coords_str).lower()
        coords_tuple = self.grid.get(coords_str, None)
        return coords_tuple

    def board_setup(self):
        w = "White"
        b = "Black"
        for space in self.board[1]:
            self.board[space.position[0]][space.position[1]].piece = Pawn(color=b)
        for space in self.board[6]:
            self.board[space.position[0]][space.position[1]].piece = Pawn(color=w)
        self.board[0][0].piece = Rook(color=b)
        self.board[0][1].piece = Knight(color=b)
        self.board[0][2].piece = Bishop(color=b)
        self.board[4][1].piece = Queen(color=b)
        self.board[0][4].piece = King(color=b)
        self.board[0][5].piece = Bishop(color=b)
        self.board[0][6].piece = Knight(color=b)
        self.board[0][7].piece = Rook(color=b)
        self.board[7][0].piece = Rook(color=w)
        self.board[7][1].piece = Knight(color=w)
        self.board[7][2].piece = Bishop(color=w)
        self.board[7][3].piece = Queen(color=w)
        self.board[7][4].piece = King(color=w)
        self.board[7][5].piece = Bishop(color=w)
        self.board[7][6].piece = Knight(color=w)
        self.board[7][7].piece = Rook(color=w)
            
    @staticmethod
    def threats_to_king(future_board, color):  # future_board is a deep copy
        # for my opponent pieces
        for row in range(8):
            for col in range(8):
                threats = assess_threat(future_board, color, row, col)
                for threat in threats:
                    # if they threaten my king
                    if (future_board.board[threat[0]][threat[1]].piece and
                        isinstance(future_board.board[threat[0]][threat[1]].piece, King) and
                            future_board.board[threat[0]][threat[1]].piece.color == color):
                                # finish / return true
                                return True
        # else... return false
        return False


class Space:
    def __init__(self, x, y):
        self.position = (x, y)
        self.piece = None
        self.threatened_by_white = None
        self.threatened_by_black = None
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
# some_board = Board()
# print(some_board.grid)
# print("\n\n\n")
#
# print(some_board)
# print("\n\n")
#
# some_board.board_setup()
# print(some_board)

# thing1 = Bishop(color='white')
# thing2 = King(color='white')
# print(thing1.check_direction((3, 3), (1, 1), some_board))
# print("\n\n\n")

# Piece tests
# some_board.board[7][1].piece = Knight()
# some_board.board[7][0].piece = Rook()
# some_board.board[3][4].piece = Queen()
# some_board.board[4][3].piece = Queen(color='black')
# some_board.board[2][3].piece = Queen(color='black')
# some_board.board[4][5].piece = Queen(color='black')
# some_board.board[2][5].piece = Queen(color='black')
# some_board.board[1][4].piece = Pawn(color='black')
# some_board.board[7][4].piece = King()
# some_board.board[7][7].piece = Rook()
# some_board.board[7][0].piece = Rook()
# some_board.board[6][7].piece = Pawn(color='black')
# 
# player1 = Player()
# print(some_board)
# print("\n\n\n")
# while True:
#     player1.make_a_move(some_board)
#     print(some_board)
#     print("\n\n\n")

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

def main():
    players = (Player(), Player(color="Black"))
    turn = 0
    some_board = Board()
    some_board.board_setup()
    while True:
        print(some_board)
        players[(turn + 2) % 2].make_a_move(some_board)
        turn += 1


if __name__ == '__main__':
    main()
