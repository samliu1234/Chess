# Imports
import pawn
import knight
import bishop
import rook
import queen
import king


# Screen
screen = "menu"
# Indicates which options are selected in the options page
one_player_selected = True
white_selected = True
# Run variable
run = True
# Whether white or black is in check
check = False
# Whose turn it is
turn = "white"
# If a piece has been pressed
pressed_piece = False
# Which piece was pressed
current_piece_number = 0
# Left castle is an option
left_castle = False
# Right castle is an option
right_castle = False
# En passant is an option
en_passant = False
# Checkmate
print_checkmate = False
# Stalemate
print_stalemate = False
# Move number
move = 0
# [xpx, ypx, x, y] of the last move
last_move = [-100, -100, -100, -100]
# [bp, bn, bb, br, bq, wp, wn, wb, wr, wq, btotal, wtotal]
totals = [0 for _ in range(12)]
# Highlights of a clicked piece
to_move = [-100, -100]
# White promotion
white_promotion = False
# Black promotion
black_promotion = False
# Whether the board should flip
flip = False
# Counter for clicking
counter = 0
increment_counter = False
# Which colour pawn moves up
moves_up = "white"
# White and black scores
white_score = 0.0
black_score = 0.0
# Black, white resign, draw
black_resign = False
white_resign = False
draw = False
# Total number of possible moves, used in utility.eval_board()
white_total_moves = 0
black_total_moves = 0
# Show draw declination text
draw_declination = False
draw_counter = 0

# List of circles
circles = []

# List of pieces
pieces = [pawn.Pawn("pawn", "white", 1, 7), pawn.Pawn("pawn", "white", 2, 7), pawn.Pawn("pawn", "white", 3, 7),
          pawn.Pawn("pawn", "white", 4, 7), pawn.Pawn("pawn", "white", 5, 7), pawn.Pawn("pawn", "white", 6, 7),
          pawn.Pawn("pawn", "white", 7, 7), pawn.Pawn("pawn", "white", 8, 7), pawn.Pawn("pawn", "black", 1, 2),
          pawn.Pawn("pawn", "black", 2, 2), pawn.Pawn("pawn", "black", 3, 2), pawn.Pawn("pawn", "black", 4, 2),
          pawn.Pawn("pawn", "black", 5, 2), pawn.Pawn("pawn", "black", 6, 2), pawn.Pawn("pawn", "black", 7, 2),
          pawn.Pawn("pawn", "black", 8, 2), knight.Knight("knight", "white", 2, 8), knight.Knight("knight", "white", 7, 8),
          knight.Knight("knight", "black", 2, 1), knight.Knight("knight", "black", 7, 1), bishop.Bishop("bishop", "white", 3, 8),
          bishop.Bishop("bishop", "white", 6, 8), bishop.Bishop("bishop", "black", 3, 1), bishop.Bishop("bishop", "black", 6, 1),
          rook.Rook("rook", "white", 1, 8), rook.Rook("rook", "white", 8, 8), rook.Rook("rook", "black", 1, 1),
          rook.Rook("rook", "black", 8, 1), queen.Queen("queen", "white", 4, 8), queen.Queen("queen", "black", 4, 1),
          king.King("king", "white", 5, 8), king.King("king", "black", 5, 1)]


def restart():
    global run, check, turn, pressed_piece, current_piece_number, left_castle, right_castle, en_passant, print_checkmate, \
        print_stalemate, last_move, move, totals, to_move, white_promotion, black_promotion, flip, circles, pieces, moves_up, \
        black_resign, white_resign, draw, white_total_moves, black_total_moves, one_player_selected, white_selected

    check = False
    turn = "white"
    pressed_piece = False
    current_piece_number = 0
    left_castle = False
    right_castle = False
    en_passant = False
    print_checkmate = False
    print_stalemate = False
    move = 0
    last_move = [-100, -100, -100, -100]
    totals = [0 for _ in range(12)]
    to_move = [-100, -100]
    white_promotion = False
    black_promotion = False
    flip = False
    moves_up = "white"
    black_resign = False
    white_resign = False
    draw = False
    white_total_moves = 0
    black_total_moves = 0

    circles = []

    pieces = [pawn.Pawn("pawn", "white", 1, 7), pawn.Pawn("pawn", "white", 2, 7), pawn.Pawn("pawn", "white", 3, 7),
              pawn.Pawn("pawn", "white", 4, 7), pawn.Pawn("pawn", "white", 5, 7), pawn.Pawn("pawn", "white", 6, 7),
              pawn.Pawn("pawn", "white", 7, 7), pawn.Pawn("pawn", "white", 8, 7), pawn.Pawn("pawn", "black", 1, 2),
              pawn.Pawn("pawn", "black", 2, 2), pawn.Pawn("pawn", "black", 3, 2), pawn.Pawn("pawn", "black", 4, 2),
              pawn.Pawn("pawn", "black", 5, 2), pawn.Pawn("pawn", "black", 6, 2), pawn.Pawn("pawn", "black", 7, 2),
              pawn.Pawn("pawn", "black", 8, 2), knight.Knight("knight", "white", 2, 8),
              knight.Knight("knight", "white", 7, 8),
              knight.Knight("knight", "black", 2, 1), knight.Knight("knight", "black", 7, 1),
              bishop.Bishop("bishop", "white", 3, 8),
              bishop.Bishop("bishop", "white", 6, 8), bishop.Bishop("bishop", "black", 3, 1),
              bishop.Bishop("bishop", "black", 6, 1),
              rook.Rook("rook", "white", 1, 8), rook.Rook("rook", "white", 8, 8), rook.Rook("rook", "black", 1, 1),
              rook.Rook("rook", "black", 8, 1), queen.Queen("queen", "white", 4, 8),
              queen.Queen("queen", "black", 4, 1),
              king.King("king", "white", 5, 8), king.King("king", "black", 5, 1)]
