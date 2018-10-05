#Define Pawn class

from colorama import init
from colorama import Fore, Style
init()


class Pawn:

    def __init__(self, color="White"):
        self.color = self.set_color(color)
        self.has_moved = False
        self.double_move_flag = False
        self.passant_left = False
        self.passant_right = False
        self.color_mod = self.set_color_mod()
        
    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' P ' + Style.RESET_ALL
        
    @staticmethod
    def set_color(color):
        result = "White"
        if color.lower()[0] != "w":
            result = "Black"
        return result

    @staticmethod
    def set_color_mod(self):
        if self.color.lower()[0] == "w":
            color_mod = -1
        else:
            color_mod = 1        
        return color_mod         
    
    def en_passant(self, board, a, b, possible_moves):
        #reset passant attributes to False
        self.passant_left = False
        self.passant_right = False
        #Now check to see if passant attributes should be updated to True, based on ALL of the following criteria
        if capture_left in possible_moves and board.board[a][b-1].piece and board.board[a][b-1].piece.color != self.color and isinstance(board.board[a][b-1].piece, Pawn) and board.board[a][b-1].piece.double_move_flag:
            self.passant_left = True
        if capture_right in possible_moves and board.board[a][b+1].piece and board.board[a][b+1].piece.color != self.color and isinstance(board.board[a][b+1].piece, Pawn) and board.board[a][b+1].piece.double_move_flag:
            self.passant_right = True            
            
    def move_options(self,position,board):
        '''
        position - a tuple that represents where the pawn is on the board
        possible_moves is a list of positions that the pawn could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        '''
        a = position[0]
        b = position[1]
        single_move = (a + self.color_mod, b)
        double_move = (a + (2 * self.color_mod), b)
        capture_left = (a + self.color_mod, b - 1)
        capture_right = (a + self.color_mod, b + 1)
        move_list = [single_move, double_move, capture_left, capture_right]
        valid_range = list(range(8))
        possible_moves = [] #This list will be the moves that fit on the board, used mostly to trim the diaganol captures from the sides of the board
        valid_moves = []

        #single_move   - (a + color_mod, b)       The default move
        #double_move   - (a + (2 * color_mod), b) Only legal when self.has_moved = False
        #capture_left  - (a + color_mod, b - 1)   Only legal when the destination space is occupied by a non-king piece of the opposite color
        #capture_right - (a + color_mod, b + 1)   Only legal when the destination space is occupied by a non-king piece of the opposite color
        
        #limit move_list to only check for moves that fit on the board
        for move in move_list:
            if move[0] in valid_range and move[1] in valid_range:
                possible_moves.append(move)        
        #update passant attributes
        en_passant(board, a, b, possible_moves)
        #single_move
        if single_move in possible_moves:
            if not board.board[single_move[0]][single_move[1]].piece:
                valid_moves.append(single_move)
        #double_move
        if double_move in possible_moves and single_move in valid_moves:
            if not self.has_moved:
                if not board.board[double_move[0]][double_move[1]].piece:
                    valid_moves.append(double_move)
        #capture_left
        if capture_left in possible_moves:
            if (board.board[capture_left[0]][capture_left[1]].piece and board.board[capture_left[0]][capture_left[1]].piece.color != self.color) or self.passant_left:
                valid_moves.append(capture_left)
        #capture_right
        if capture_right in possible_moves:
            if board.board[capture_right[0]][capture_right[1]].piece and board.board[capture_right[0]][capture_right[1]].piece.color != self.color or self.passant_right:
                valid_moves.append(capture_right)        
        
        #legal_moves = []

        #for space in valid_moves:
        #    if occupied_check(space):
        #        legal_moves.append(space)
    
        return valid_moves
    
    
# Help visualize board:
# [
# [0,1,2,3,4,5,6,7], 0
# [0,1,2,3,A,5,6,7], 1
# [0,1,2,3,4,5,6,7], 2
# [0,1,2,3,4,5,6,7], 3 
# [0,1,2,3,4,5,6,7], 4
# [0,1,2,3,4,5,6,7], 5
# [0,1,2,3,P,5,6,7], 6
# [0,1,2,3,4,5,6,7]  7
# ]
# Top left is [0][0], bottom right is [7][7]

#white pawn(P) is at a,b (a=6,b=4)

#single_move   - 5,4 
#double_move   - 4,4
#capture_left  - 5,3
#capture_right - 5,5

#black pawn(A) is at c,d (c=1,d=4)

#single_move   - 2,4 
#double_move   - 3,4
#capture_left  - 2,3
#capture_right - 2,5