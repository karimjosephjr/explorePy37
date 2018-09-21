class Bishop:

    def __init(self, color="White"):
        self.color = color

    def __str__(self):
        return ' B '

    @staticmethod
    def check_direction(position, direction):
        options = []
        valid_range = list(range(8))
        row = position[0] + direction[0]
        col = position[1] + direction[1]

        while (row in valid_range) and (col in valid_range):
            options.append((row, col))
            row += direction[0]
            col += direction[1]
        return options

    def move_options(self, position):
        '''
        position - a tuple that represents where the king is on the board
        possible_moves is a list of positions that the king could move to without concern for size of the board
        the for loop retains elements from the possible_moves list that are valid given an 8x8 board
        returns a list that can be used for Player.validate_move
        '''

        valid_moves = list()
        valid_moves += self.check_direction(position, (1, 1))
        valid_moves += self.check_direction(position, (1, -1))
        valid_moves += self.check_direction(position, (-1, 1))
        valid_moves += self.check_direction(position, (-1, -1))

        return valid_moves
