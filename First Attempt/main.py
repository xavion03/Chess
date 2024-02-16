import chess

#import piece tables from piece_tables file
from piece_tables import tabledict

#create chess board object
board = chess.Board()

#function to evaluate board
#returns evaluation score
def evaluate_board():
    #based on/taken from https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec

    #conditional statement to see if white or black is in checkmate
    #if white checkmates black the function returns 9999, an evaluation of 9999 indicates victory
    if board.is_checkmate():
        if board.turn(chess.WHITE):
            return 9999
        else:
            return -9999
        
    #if there is some form of stalemate, not all stalemate rules are represented here, returns evaluation of 0
    #evaluation of 0 indicates that the positions of white and black is equal
    if board.is_stalemate():
        return 0
    
    if board.is_insufficient_material():
        return 0

    #variables to hold number of pieces currently on board
    wp = len(board.pieces(chess.PAWN, chess.WHITE)) 
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    #calculate material evaluation based on how many pieces are on board
    #based off material values from simplified evaluation function (https://www.chessprogramming.org/Simplified_Evaluation_Function#Piece_Values)
    material_eval = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    
    # for loop to calculate the position evaluation based on the piece tables
    square_eval = 0
    for table_piece in range(1,7):
        #first loop iterates though numbers 1 and 7 that correlate to the piece table and also the chess pieces
        #second loop finds the sum of the piece table evaluation numbers based on the pieces position for white and black 
        #the evaluation numbers are then added 
        square_eval += sum([tabledict[table_piece][i] for i in board.pieces(table_piece, chess.WHITE)])
        square_eval += sum([-tabledict[table_piece][chess.square_mirror(i)] for i in board.pieces(table_piece, chess.BLACK)])
    
    #returns the evaluation of the board in the form of the sum of the material evaluation and square evaluations
    total_evaluation = material_eval + square_eval
    #if it is whites turn return positive, if blacks turn return negative
    #for negmax search 
    if board.turn:
        return total_evaluation
    else:
        return -total_evaluation

# function to implement negamax algorithm with alpha/beta pruning including quiescence search
# https://www.chessprogramming.org/Alpha-Beta
# alpha = lower bound score, beta = upperbound score, depthleft = search depth *depth is exponential
def alpha_beta_nega(alpha, beta, depth_left):
    if depth_left == 0:
        return quiescence(alpha, beta)
    
    for move in board.legal_moves:
        board.push(move)
        score = -alpha_beta_nega( -beta, -alpha, depth_left-1)
        board.pop()

        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    
    return alpha
        
    
# function to implement quiescence search
# https://www.chessprogramming.org/Quiescence_Search 
def quiescence(alpha, beta):
    stand_pat = evaluate_board()
    
    if stand_pat == beta:
        return beta
    
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = quiescence( -beta, -alpha)
            board.pop()
        
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha

def find_best_move(depth):
    best_move = chess.Move.null()

    alpha = float('inf')
    beta = float('-inf')
    best_value = -99999

    for move in board.legal_moves:
        board.push(move)
        board_value = -alpha_beta_nega(-beta, -alpha, depth-1)

        if board_value > best_value:
            best_value = board_value
            best_move = move

        if board_value > alpha:
            alpha = board_value
        
        board.pop()
    
    return best_move

print(find_best_move(3))
