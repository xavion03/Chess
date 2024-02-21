import chess
import chess.polyglot
from NewPieceTable import *
from Engine import *

## basic program to test opening book

""" while(1):
    print (board.legal_moves)
    print(board)
    print('/n')
    pmove = input('Input move: ')
    if pmove == 'exit':
        break
    board.push_san(pmove)
    print(board)
    print('/n')
    move = chess.polyglot.MemoryMappedReader("/workspaces/Chess/Second_Attempt/Book.bin").weighted_choice(board).move
    board.push(move)
    print(board)
    print('/n')
 """




