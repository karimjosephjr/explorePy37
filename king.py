from colorama import init
from colorama import Fore, Style
init()


class King:

    def __init__(self, color="White"):
        self.color = self.set_color(color)
        self.has_moved = False
        self.castle_left = False
        self.castle_right = False
        self.options = []

    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' K ' + Style.RESET_ALL

    @staticmethod
    def set_color(color):
        result = "White"
        if color.lower()[0] != "w":
            result = "Black"
        return result
        
    def castle(self, board, a, b):
        #reset castle flags to false
        self.castle_left = False
        self.castle_right = False
        
        if not self.has_moved:
            if not board.board[a][b-1].piece and not board.board[a][b-2].piece and not board.board[a][b-3].piece:
                if board.board[a][b-4].piece and isinstance(board.board[a][b-4].piece, Rook) and not board.board[a][b-4].piece.has_moved: 
                    #if king doesn't move through threat:
                    self.castle_left = True
        if not self.has_moved:
            if not board.board[a][b+1].piece and not board.board[a][b+2].piece:
                if board.board[a][b+3].piece and isinstance(board.board[a][b+3].piece, Rook) and not board.board[a][b+3].piece.has_moved:
                    #if king doesn't move through threat:
                    self.castle_right = True

    def move_options(self, position, board):
        """"
        position - a tuple that represents where the king is on the board
        possible_moves is a list of positions that the king could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        """
        a = position[0]
        b = position[1]
        # up            = (a-1,b)
        # down          = (a+1,b)
        # left          = (a,b-1)
        # right         = (a,b+1)
        # up_left       = (a-1,b-1)
        # up_right      = (a-1,b+1)
        # down_left     = (a+1,b-1)
        # down_right    = (a+1, b+1)
        #Castling logic - IF (king has not moved AND rook has not moved) AND (no pieces between king and rook) AND (king does not move through check)
        possible_moves = [(a-1, b), (a+1, b), (a, b-1), (a, b+1), (a-1, b-1), (a-1, b+1), (a+1, b-1), (a+1, b+1)]  # a list of tuple coordinate pairs corresponding to positions on the board
        valid_range = list(range(8))
        valid_moves = []
        
        for (x, y) in possible_moves:
            if x in valid_range and y in valid_range:
                if not (board.board[x][y].piece and board.board[x][y].piece.color == self.color):
                    valid_moves.append((x, y))
        #call self.castle to update castle flags            
        self.castle(board, a, b)
        #append castling spaces to valid_moves based on castle flags
        if self.castle_left:
            valid_moves.append((a, b-2))
        if self.castle_right:
            valid_moves.append((a, b+2))
    
        return valid_moves
    
    
# Help visualize board:
# [
# [0,1,2,3,4,5,6,7], 0
# [0,1,2,3,4,5,6,7], 1
# [0,1,2,3,4,5,6,7], 2
# [0,1,2,3,4,5,6,7], 3 
# [0,1,2,3,4,5,6,7], 4
# [0,1,2,3,4,5,6,7], 5
# [0,1,2,K,4,5,6,7], 6
# [0,1,2,3,4,5,6,7]  7
# ]
# Top left is [0][0], bottom right is [7][7]

# king(K) is at a,b (a=6,b=3)
#
# king can move:
# up - 5,3
# down - 7,3
# left - 6,2
# right - 6,4
# up_left - 5,2
# up_right - 5,4
# down_left - 7,2
# down_right - 7,4
