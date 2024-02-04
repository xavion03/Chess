import chess

board = chess.Board()

print(board)
print(board.legal_moves)



move = chess.Move(chess.E2, chess.E4)
if move in board.legal_moves: 
    board.push(move)
    print(board)
else:
    print ("That move is not legal")


