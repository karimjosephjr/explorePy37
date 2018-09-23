#Define Rook class

from colorama import init
from colorama import Fore, Style
init()


class Rook:

    def __init__(self, color="White"):
        self.color = color

    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' R ' + Style.RESET_ALL

    def move_options(self,position):
        '''
        position - a tuple that represents where the rook is on the board
        based on position, build 2 lists to represent the rook's row and column of movement
        returns a list that can be used for Player.validate_move
        '''
        a = position[0]
        b = position[1]
        
        #row    - [(a,0),(a,1),(a,2),(a,3),(a,4),(a,5),(a,6),(a,7)] 
        #column - [(0,b),(1,b),(2,b),(3,b),(4,b),(5,b),(6,b),(7,b)]
        
        valid_range = list(range(8))
        row = [(a,i) for i in valid_range if i != b] #conditional statement lets us skip returning the rook's current position
        column = [(i,b) for i in valid_range if i != a]
        valid_moves = row + column
        
        #legal_moves = []
        
        #for space in valid_moves:
        #    if occupied_check(space):
        #        legal_moves.append(space)
    
        return valid_moves
    
    
# Help visualize board:
# [
# [0,1,2,3,4,5,6,7], 0
# [0,1,2,3,4,5,6,7], 1
# [0,1,2,3,4,5,6,7], 2
# [0,1,2,3,4,5,6,7], 3 
# [0,1,2,R,4,5,6,7], 4
# [0,1,2,3,4,5,6,7], 5
# [0,1,2,3,4,5,6,7], 6
# [0,1,2,3,4,5,6,7]  7
# ]
# Top left is [0][0], bottom right is [7][7]

#rook(R) is at a,b (a=4,b=3)
#On an empty board, the rook can move anywhere in its current row, or current column
#row - [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7)] 
#column - [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3)]
