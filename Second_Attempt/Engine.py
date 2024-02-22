import chess
import chess.polyglot # for opening book
from NewPieceTable import *

board = chess.Board()

#function that returns phase of game
#middle = 2, end = 3
def check_gamephase():
    phase = 2
    return phase

def evaluate_material(phase):
    #simple piece evaluation
    pawn_eval = 100
    bishop_eval = 330
    knight_eval = 300
    king_eval = 400 # for late game
    rook_eval = 500
    queen_eval = 900

    #count of each white piece vs black piece
    pawn_count = len(board.pieces(chess.PAWN, chess.WHITE)) - len(board.pieces(chess.PAWN, chess.BLACK))
    bishop_count = len(board.pieces(chess.BISHOP, chess.WHITE)) - len(board.pieces(chess.BISHOP, chess.BLACK))
    knight_count = len(board.pieces(chess.KNIGHT, chess.WHITE)) - len(board.pieces(chess.KNIGHT, chess.BLACK))
    rook_count = len(board.pieces(chess.ROOK, chess.WHITE)) - len(board.pieces(chess.ROOK, chess.BLACK))
    queen_count = len(board.pieces(chess.QUEEN, chess.WHITE)) - len(board.pieces(chess.QUEEN, chess.BLACK))

    if phase < 3:
        # if game is in midgame phase multiply piece evaluation by piece count
        # negative total means black has more of that piece
        pawn_total = pawn_eval * pawn_count
        bishop_total = bishop_eval * bishop_count
        knight_total = knight_eval * knight_count
        rook_total = rook_eval * rook_count
        queen_total = queen_eval * queen_count

        # total evaluation calculated by adding all of the piece totals
        # a postive evaluation number means white has a piece advantage
        evaluation = pawn_total + bishop_total + knight_total + rook_total + queen_total
        return evaluation
    else:
        return evaluation

def evaluate_position(phase):
    evaluation = 0

    if phase < 3:
        # finds difference between sums of white and black piece positions (for mid game) 
        # a possitive total means that white's pieces have a better position than black's
        pawn_total = sum([mg_pawn_table[i] for i in board.pieces(chess.PAWN, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.PAWN, chess.BLACK)])
        knight_total = sum([mg_knight_table[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
        bishop_total = sum([mg_bishop_table[i] for i in board.pieces(chess.BISHOP, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.BISHOP, chess.BLACK)])
        rook_total = sum([mg_rook_table[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.ROOK, chess.BLACK)])
        queen_total = sum([mg_queen_table[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.QUEEN, chess.BLACK)])
        king_total = sum([mg_king_table[i] for i in board.pieces(chess.KING, chess.WHITE)]) - sum([mg_pawn_table[i] for i in board.pieces(chess.KING, chess.BLACK)])

        evaluation = pawn_total + bishop_total + knight_total + rook_total + queen_total + king_total
        return evaluation
    else:
        return evaluation

def evaluate():

    if board.is_checkmate():
        if board.turn:
            return 9999
        else: 
            return -9999
    
    if board.is_stalemate():
        return 0
    
    if board.is_insufficient_material():
        return 0

    phase = check_gamephase()
    material_eval = evaluate_material(phase)
    positonal_eval = evaluate_position(phase)

    total_eval = material_eval + positonal_eval

    if board.turn:
       return total_eval
    else:
       return -total_eval
    
#implement negamax search with quiescence
def search(alpha, beta, depth):
    best_score = -9999

    if depth == 0:
        return quiescence(alpha, beta)
    
    for move in board.legal_moves:
        board.push(move)
        score = -search(-beta, -alpha, depth -  1)
        board.pop()

        if score >= beta:
            return score
        if score > best_score:
            best_score = score
        if score > alpha:
            alpha = score

    return best_score
   
   
def quiescence(alpha, beta):
    stand_pat = evaluate()
    if(stand_pat >= beta):
        return beta
    if(alpha < stand_pat):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiescence( -beta, -alpha)
            board.pop()

            if(score >= beta):
                return beta
            if(score > alpha):
                alpha = score

    return alpha
    
def find_best_move(depth):
    try: 
        move = chess.polyglot.MemoryMappedReader("/workspaces/Chess/Second_Attempt/Book.bin").weighted_choice(board).move
        return move
    except:
        print ("Midgame Start")
        alpha = -99999
        beta = 99999
        score = -99999
        best_move = chess.Move.null()

        for move in board.legal_moves:
            board.push(move)
            search_score = -search(-beta, -alpha, depth - 1)

            if search_score > score:
                score = search_score
                best_move = move
            
            if search_score > alpha:
                alpha = search_score

            board.pop()

        return best_move
