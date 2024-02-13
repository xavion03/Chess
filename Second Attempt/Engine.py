import chess

from PieceTable import *

board = chess.Board()

#function that returns phase of game
#opening = 1, middle = 2, end = 3
def gamephase():
    phase = 1
    return phase

def evaluate_material(phase):
    #simple piece evaluation
    pawn_eval = 100
    biship_eval = 330
    knight_eval = 300
    king_eval = 400
    rook_eval = 500
    queen_eval = 900

    #count of each white piece vs black piece
    pawn_count = len(board.pieces(chess.PAWN, chess.WHITE)) - len(board.pieces(chess.PAWN, chess.BLACK))
    biship_count = len(board.pieces(chess.BISHOP, chess.WHITE)) - len(board.pieces(chess.BISHOP, chess.BLACK))
    knight_count = len(board.pieces(chess.KNIGHT, chess.WHITE)) - len(board.pieces(chess.KNIGHT, chess.BLACK))
    rook_count = len(board.pieces(chess.ROOK, chess.WHITE)) - len(board.pieces(chess.ROOK, chess.BLACK))
    queen_count = len(board.pieces(chess.QUEEN, chess.WHITE)) - len(board.pieces(chess.QUEEN, chess.BLACK))

    if phase < 3:
        # if game is in midgame phase multiply piece evaluation by piece count
        # negative total means black has more of that piece
        pawn_total = pawn_eval * pawn_count
        biship_total = biship_eval * biship_count
        knight_total = knight_eval * knight_count
        rook_total = rook_eval * rook_count
        queen_total = queen_eval * queen_count

        # total evaluation calculated by adding all of the piece totals
        # a postive evaluation number means white has a piece advantage
        evaluation = pawn_total + biship_total + knight_total + rook_total + queen_total
        return evaluation
    else:
        return evaluation

def evaluate_position(phase):
    evaluation = 0

    if phase < 3:
        return evaluation
    else:
        return evaluation

def evaluate(phase):

   if board.is_checkmate():
        if board.turn(chess.WHITE):
            return 9999
        else: 
            return -9999
        
   material_eval = evaluate_material(phase)
   positonal_eval = 0

   total_eval = material_eval + positonal_eval

   if board.turn(chess.WHITE):
       return total_eval
   else:
       return -total_eval
    
    
    

    