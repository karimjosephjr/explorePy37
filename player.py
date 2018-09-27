#define Player class

class Player:

    def __init__(self, name="Default", color="White"):
        self.name = name
        self.color = color
    
    def make_a_move(self, board):
        '''
        Prompt the player to select a piece that they wish to move by providing the space that piece occupies
        Then prompt the player to select where they would like to move that piece to
        Update the board after validation 
        '''
        
        #board.get_coords(string) returns either None or a tuple
        #board.update_board(start,end) is expecting two tuples (coord of piece that is going to move)(coord of destination)
        
        valid_piece = None
        while not valid_piece:
            piece_space = input("Select the piece that you wish to move by providing the space it currently occupies: ")
            piece_tup = board.get_coords(piece_space)
            if piece_tup != None and board.board[piece_tup[0]][piece_tup[1]].piece != None:
                valid_piece = board.board[piece_tup[0]][piece_tup[1]].piece
                
        valid_moves = valid_piece.move_options(piece_tup, board)
        move_choice = None
        while move_choice not in valid_moves:
            potential_move = input("Select the space that you would like to move your piece to: ")
            if potential_move == "help":
                print(self.print_move_options(piece_tup, board))
            move_choice = board.get_coords(potential_move)
            
        board.update_board(piece_tup,move_choice)

    @staticmethod
    def print_move_options(position, board):
        piece = board.board[position[0]][position[1]].piece
        tuple_options = piece.move_options(position, board)
        pretty_options = [board.inverted_grid[position] for position in tuple_options]
        return "\n".join(pretty_options)


# Help visualize board:
# [

# [0,1,2,3,4,5,6,7], 8
# [0,1,2,3,4,5,6,7], 7
# [0,1,2,3,4,5,6,7], 6
# [0,1,2,3,4,5,6,7], 5 
# [0,1,2,3,4,5,6,7], 4
# [0,1,2,3,4,5,6,7], 3
# [0,1,2,3,4,5,6,7], 2
# [0,1,2,3,4,5,6,7]  1
#  A B C D E F G H
# ]
# Top left is [0][0] {'A8':(0,0)}, bottom right is [7][7] {'H1':(7,7)}        [Number][Letter]

# Letter    Index
# A            0    
# B            1
# C            2
# D            3
# E            4
# F            5
# G            6
# H            7

# Number    Index
# 1            7    
# 2            6
# 3            5
# 4            4
# 5            3
# 6            2
# 7            1
# 8            0
