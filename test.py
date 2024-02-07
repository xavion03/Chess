import chess

board = chess.Board("8/5K2/8/8/8/5Q2/7p/R5k1 b - - 3 57")

legal_moves = board.legal_moves.count()
print(legal_moves)