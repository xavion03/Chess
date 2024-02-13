import chess
from NewPieceTable import *

board = chess.Board()

#pawneval_w = sum([mg_pawn_table[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
#print(pawneval_w)

for i in board.pieces(chess.PAWN, chess.WHITE):
    print(i)
print("\n")
for i in board.pieces(chess.PAWN, chess.WHITE):
    print(mg_pawn_table[i])


