from colorama import init
from colorama import Fore, Style
init()


class Knight:

    def __init__(self, color="White"):
        self.color = self.set_color(color)
        self.options = []

    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' N ' + Style.RESET_ALL

    @staticmethod
    def set_color(color):
        result = "White"
        if color.lower()[0] != "w":
            result = "Black"
        return result

    def move_options(self, position, board):
        """
        position - a tuple that represents where the knight is on the board
        possible_moves is a list of positions that the knight could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        """
        a = position[0]
        b = position[1]
        
        # up_left    - (a-2,b-1)
        # up_right   - (a-2,b+1)
        # down_left  - (a+2,b-1)
        # down_right - (a+2,b+1)
        # right_up   - (a-1,b+2)
        # right_down - (a+1,b+2)
        # left_up    - (a-1,b-2)
        # left_down  - (a+1,b-2)
        
        possible_moves = [(a-2, b-1), (a-2, b+1), (a+2, b-1), (a+2, b+1), (a-1, b+2), (a+1, b+2), (a-1, b-2), (a+1, b-2)]  # a list of tuple coordinate pairs corresponding to positions on the board
        valid_range = list(range(8))
        valid_moves = []
        # legal_moves = []
        
        for (x, y) in possible_moves:
            if x in valid_range and y in valid_range:
                if not (board.board[x][y].piece and board.board[x][y].piece.color == self.color):
                    valid_moves.append((x, y))

        # for space in valid_moves:
        #    if occupied_check(space):
        #        legal_moves.append(space)
    
        return valid_moves
    
    
# Help visualize board:
# [
# [0,1,2,3,4,5,6,7], 0
# [0,1,2,3,4,5,6,7], 1
# [0,1,2,3,4,5,6,7], 2
# [0,1,2,3,4,5,6,7], 3 
# [0,1,2,3,N,5,6,7], 4
# [0,1,2,3,4,5,6,7], 5
# [0,1,2,3,4,5,6,7], 6
# [0,1,2,3,4,5,6,7]  7
# ]
# Top left is [0][0], bottom right is [7][7]

# knight(N) is at a,b (a=4,b=4)

# up_left - 2,3
# up_right - 2,5
# down_left - 6,3
# down_right - 6,5
# right_up - 3,6
# right_down - 5,6
# left_up - 3,2
# left_down - 5,2
