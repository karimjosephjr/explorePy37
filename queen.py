from colorama import init
from colorama import Fore, Style
init()


class Queen:

    def __init__(self, color="White"):
        self.color = self.set_color(color)

    def __str__(self):
        if self.color.lower()[0] == "w":
            piece_color = Fore.WHITE + Style.BRIGHT
        else:
            piece_color = Fore.BLUE + Style.BRIGHT
        return piece_color + ' Q ' + Style.RESET_ALL

    @staticmethod
    def set_color(color):
        result = "White"
        if color.lower()[0] != "w":
            result = "Black"
        return result

    def check_direction(self, position, direction, board):
        options = []
        valid_range = list(range(8))
        row = position[0] + direction[0]
        col = position[1] + direction[1]

        while (row in valid_range) and (col in valid_range):
            if board.board[row][col].piece and board.board[row][col].piece.color == self.color:
                break
            options.append((row, col))
            if board.board[row][col].piece and board.board[row][col].piece.color != self.color:
                break
            row += direction[0]
            col += direction[1]
        return options

    def move_options(self, position, board):
        """"
        position - a tuple that represents where the king is on the board
        possible_moves is a list of positions that the king could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        """

        valid_moves = list()
        valid_moves += self.check_direction(position, (1, 1), board)
        valid_moves += self.check_direction(position, (1, -1), board)
        valid_moves += self.check_direction(position, (-1, 1), board)
        valid_moves += self.check_direction(position, (-1, -1), board)
        valid_moves += self.check_direction(position, (0, 1), board)
        valid_moves += self.check_direction(position, (0, -1), board)
        valid_moves += self.check_direction(position, (1, 0), board)
        valid_moves += self.check_direction(position, (-1, 0), board)

        return valid_moves
