#Define Pawn class

from colorama import init
from colorama import Fore, Style
init()


class Pawn:

    def __init__(self, color="White"):
        self.color = color
        self.has_moved = False

    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' P ' + Style.RESET_ALL

    def move_options(self,position):
        '''
        position - a tuple that represents where the pawn is on the board
        possible_moves is a list of positions that the pawn could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        '''
        a = position[0]
        b = position[1]
        if self.color.lower()[0] == "w":
            color_mod = -1
        else:
            color_mod = 1        
        possible_moves = [(a + color_mod, b), (a + (2 * color_mod), b), (a + color_mod, b - 1), (a + color_mod, b + 1)]
        valid_moves = []
        
        #single_move   - (a + color_mod, b)       The default move
        #double_move   - (a + (2 * color_mod), b) Only legal when self.has_moved = False
        #capture_left  - (a + color_mod, b - 1)   Only legal when the destination space is occupied by a non-king piece of the opposite color
        #capture_right - (a + color_mod, b + 1)   Only legal when the destination space is occupied by a non-king piece of the opposite color
        
        #single_move
        if not board.board[possible_moves[0][0]][possible_moves[0][1]].piece:
            valid_moves.append(possible_moves[0])
        #double_move
        if not self.has_moved:
            if not board.board[possible_moves[0][0]][possible_moves[0][1]].piece and not board.board[possible_moves[1][0]][possible_moves[1][1]].piece:
                valid_moves.append(possible_moves[1])
        #captures
        for i in possible_moves[2:]:
            if board.board[possible_moves[i][0]][possible_moves[i][1]].piece and board.board[possible_moves[i][0]][possible_moves[i][1]].piece.color != self.color:
                valid_moves.append(possible_moves[i])
        
        valid_range = list(range(8))
        #legal_moves = []
        
        for (x,y) in possible_moves:
            if x in valid_range and y in valid_range:
                valid_moves.append((x,y))

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