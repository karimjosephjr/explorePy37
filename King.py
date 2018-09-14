#Define King class

class King:

	def __init(self, color="White"):
		self.color = color
		
	def move_options(self,position):
		'''
		position - a tuple that represents where the king is on the board
		possible_moves is a list of positions that the king could move to without concern for size of the board
		the for loop retains elements from the possible_moves list that are valid given an 8x8 board
		returns a list that can be used for Player.validate_move
		'''
		a = position[0]
		b = position[1]
		#up 		= (a-1,b)
		#down 		= (a+1,b)
		#left 		= (a,b-1)
		#right 		= (a,b+1)
		#up_left 	= (a-1,b-1)
		#up_right 	= (a-1,b+1)
		#down_left 	= (a+1,b-1)
		#down_right = (a+1, b+1)
		possible_moves = [(a-1,b),(a+1,b),(a,b-1),(a,b+1),(a-1,b-1),(a-1,b+1),(a+1,b-1),(a+1, b+1)] #a list of tuple coordinate pairs corresponding to positions on the board
		valid_range = list(range(8))
		valid_moves = []
		#legal_moves = []
		
		for (x,y) in possible_moves:
			if x in valid_range and y in valid_range:
				valid_moves.append((x,y))

		#for space in valid_moves:
		#	if occupied_check(space):
		#		legal_moves.append(space)
	
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

#king(K) is at a,b (a=6,b=3)
#
#king can move:
#up - 5,3
#down - 7,3
#left - 6,2
#right - 6,4
#up_left - 5,2
#up_right - 5,4
#down_left - 7,2
#down_right - 7,4