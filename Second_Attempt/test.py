import chess
import chess.polyglot
from NewPieceTable import *
from Engine import *

while(1):

    print (board.legal_moves)
    print(board)
    print('\n')

    if board.is_checkmate() | board.is_stalemate() | board.is_insufficient_material():
        print ("Game is over!")
        break

    player_move = input('Input move: ')
    if player_move == 'exit':
        break
    
    board.push_san(player_move)

    move = find_best_move(3)
    board.push(move)

 


