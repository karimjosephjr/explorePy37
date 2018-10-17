def assess_threat(future_board, color, row, col):
    threats = []
    if future_board.board[row][col].piece and future_board.board[row][col].piece.color != color:
        # get their move options
        threats = future_board.board[row][col].piece.move_options((row, col), future_board)
    return threats