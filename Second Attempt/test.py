import chess
from NewPieceTable import *

board = chess.Board()

#pawneval_w = sum([mg_pawn_table[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
#print(pawneval_w)


board.push(move)
print(board)

eval = sum([mg_pawn_table[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
print(eval)


