import chess

#import piece tables from piece_tables file
from piece_tables import *

#create chess board object
board = chess.Board()

#function to evaluate board
#returns evaluation score
def evaluate_board():
    #taken from https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec

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

    #calculate material based on how many pieces are on board
    #based off material values from simplified evaluation function (https://www.chessprogramming.org/Simplified_Evaluation_Function#Piece_Values)
    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])

num = chess.E2
num

num2 = pawntable[num]
num2




