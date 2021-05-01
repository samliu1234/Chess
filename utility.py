# Imports
import config
import pygame
pygame.init()


# Globals
dict = {
    "queen": 9,
    "rook": 5,
    "bishop": 3,
    "knight": 2.9,
    "pawn": 1,
    "king": 0
}


# Get list of pieces
def get_pieces():
    return config.pieces


# Set list of pieces
def set_pieces(pieces_list):
    config.pieces = pieces_list


# Set list of circles
def set_circles(circles_list):
    config.circles = circles_list


# Clear list of circles
def clear_circles():
    config.circles.clear()


# Returns a boolean indicating whether or not the king is under check
def get_check():
    return config.check


# Set check to be true
def set_check():
    config.check = True


# Returns whose turn it is
def get_turn():
    return config.turn


# Get left castle
def get_left_castle():
    return config.left_castle


# Get right castle
def get_right_castle():
    return config.right_castle


# Set left castle variable to be True
def set_left_castle_true():
    config.left_castle = True


# Set right castle variable to be True
def set_right_castle_true():
    config.right_castle = True


# Set left castle variable to be False
def set_left_castle_false():
    config.left_castle = False


# Set right castle variable to be False
def set_right_castle_false():
    config.right_castle = False


# Get en passant
def get_en_passant():
    return config.en_passant


# Set en passant to be True
def set_en_passant_true():
    config.en_passant = True


# Set en passant to be False
def set_en_passant_false():
    config.en_passant = False


# Return move
def get_move():
    return config.move


# Switches turn from white to black and vice versa
def switch_turn():
    if config.turn == "white":
        config.turn = "black"
    else:
        config.turn = "white"


# Gets other colour
def get_other_colour(colour):
    if colour == "white":
        return "black"
    else:
        return "white"


# Gets white promotion
def get_white_promotion():
    return config.white_promotion


# Gets black promotion
def get_black_promotion():
    return config.black_promotion


# Sets white promotion to be true
def set_white_promotion():
    config.white_promotion = True


# Sets black promotion to be true
def set_black_promotion():
    config.black_promotion = True


# Returns a boolean indicating whether the game should continue
def should_continue():
    return not config.print_checkmate and not config.print_stalemate and not config.white_promotion and not \
        config.black_promotion and not config.draw and not config.black_resign and not config.white_resign


# Returns a list of all threatened squares for pieces of a given colour from a given list
def get_threatened_squares(the_list, colour):
    threatened_list = []
    for piece in the_list:
        if piece.colour == colour:
            threatened_list = threatened_list + piece.get_threatened_squares(the_list)
    return threatened_list


# Returns a list of the current position of all pieces
def get_all_positions(the_list):
    return_list = []
    for piece in the_list:
        return_list.append([piece.x, piece.y])

    return return_list


# Returns a list of the current position of all pieces of a given colour
def get_same_colour(the_list, colour):
    return_list = []
    for piece in the_list:
        if piece.colour == colour:
            return_list.append([piece.x, piece.y])

    return return_list


# Returns whether or not the current colour is in checkmate
def is_checkmate(pieces_list, colour):
    # All possible moves
    for piece in pieces_list:
        if piece.colour == colour:
            for pair in piece.show_options(config.pieces):
                if not piece.simulate_move(pair[0], pair[1], config.pieces):
                    return False
    return True


# Changes numbers/totals
def set_numbers(colour, name):
    if name == "pawn" and colour == "black":
        config.totals[0] += 1
        config.totals[10] += 1
    elif name == "knight" and colour == "black":
        config.totals[1] += 1
        config.totals[10] += 3
    elif name == "bishop" and colour == "black":
        config.totals[2] += 1
        config.totals[10] += 3
    elif name == "rook" and colour == "black":
        config.totals[3] += 1
        config.totals[10] += 5
    elif name == "queen" and colour == "black":
        config.totals[4] += 1
        config.totals[10] += 9
    elif name == "pawn" and colour == "white":
        config.totals[5] += 1
        config.totals[11] += 1
    elif name == "knight" and colour == "white":
        config.totals[6] += 1
        config.totals[11] += 3
    elif name == "bishop" and colour == "white":
        config.totals[7] += 1
        config.totals[11] += 3
    elif name == "rook" and colour == "white":
        config.totals[8] += 1
        config.totals[11] += 5
    elif name == "queen" and colour == "white":
        config.totals[9] += 1
        config.totals[11] += 9


# Returns number of each piece that has been taken, as well as total
def get_numbers():
    return config.totals


# Switch board
def switch_board():
    for piece in config.pieces:
        piece.y = 9 - piece.y
        piece.ypx = 75 * (piece.y - 1)


# Flips a coordinate vertically
def flip_coordinate(ypx):
    # 75 <-> 450
    return 600 - ypx - 75


# Returns whether the flip option is on or off
def get_flip():
    return config.flip


# Resets variables in preparation for new game
def reset_game():
    config.restart()


# Shows default images that are always there
def default_images(win, restart_image, main_menu_image, flip_image, empty_box_image):
    win.blit(restart_image, (870 - restart_image.get_size()[0], 20))
    win.blit(main_menu_image, (870 - main_menu_image.get_size()[0], 580 - main_menu_image.get_size()[1]))
    win.blit(flip_image, (870 - flip_image.get_size()[0], 515))
    win.blit(empty_box_image, (805, 515))


# Gets which piece is allowed to move up
def get_move_up():
    return config.moves_up


# Returns whether the given colour has insufficient pieces to checkmate (for stalemate by insufficient material)
def insufficient(colour):
    # [P, N, B, R, Q, K]
    piece_list = [0, 0, 0, 0, 0, 0]
    for piece in config.pieces:
        if piece.colour == colour:
            if piece.name == "pawn":
                piece_list[0] += 1
            elif piece.name == "knight":
                piece_list[1] += 1
            elif piece.name == "bishop":
                piece_list[2] += 1
            elif piece.name == "rook":
                piece_list[3] += 1
            elif piece.name == "queen":
                piece_list[4] += 1
            else:
                piece_list[5] += 1
    return piece_list[0] == 0 and piece_list[3] == 0 and piece_list[4] == 0 and piece_list[1] <= 1 and piece_list[2] <= 1 and not (piece_list[1] == 1 and piece_list[2] == 1)


# A board is evaluated based on material and mobility
def eval_board(piece_list):
    white_mobility, black_mobility = [0, 0]
    # White is in checkmate
    if is_checkmate(piece_list, "white"):
        return -1000
    elif is_checkmate(piece_list, "black"):
        return 1000

    # Note that a pawn capture yields a single point advantage
    # The intended weight of mobility is such that double mobility should be equivalent to a pawn
    score = 0
    for piece in piece_list:
        if piece.colour == "white":
            score += dict[piece.name]
            white_mobility = config.white_total_moves
        else:
            score -= dict[piece.name]
            black_mobility += config.black_total_moves
    white_mobility = white_mobility / max(1, max(white_mobility, black_mobility))
    black_mobility = black_mobility / max(1, max(white_mobility, black_mobility))
    return score + white_mobility - black_mobility


# Check if the user has clicked one of the game options
def game_options(event):
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
        if config.counter > 5:
            config.counter = 0
            config.increment_counter = False
        elif not config.increment_counter:
            x, y = pygame.mouse.get_pos()
            # Restart
            if 795 <= x <= 870 and 20 <= y <= 56:
                reset_game()
                config.counter = 0
                config.increment_counter = True
                if not config.white_selected and config.one_player_selected:
                    config.moves_up = "black"
                    switch_board()
                return True
            # Main menu
            elif 760 <= x <= 870 and 544 <= y <= 580:
                config.screen = "menu"
                config.counter = 0
                config.increment_counter = True
                config.white_score = 0
                config.black_score = 0
                reset_game()
                return True
            # Flip
            elif 805 <= x <= 827 and 515 <= y <= 537:
                if config.one_player_selected:
                    return False
                config.flip = not config.flip
                if config.flip:
                    if config.turn != config.moves_up:
                        switch_board()
                        config.moves_up = get_other_colour(config.moves_up)
                        for i in range(1, 4, 2):
                            config.last_move[i] = flip_coordinate(config.last_move[i])
                config.counter = 0
                config.increment_counter = True
            # Black resign
            elif 680 <= x <= 725 and 280 <= y <= 320:
                # Do not allow user to resign for the computer
                if config.one_player_selected and config.white_selected:
                    return False
                config.black_resign = True
                config.counter = 0
                config.increment_counter = True
                config.white_score += 1
            # Draw
            elif 735 <= x <= 775 and 280 <= y <= 320:
                score = eval_board(config.pieces)
                bl = False
                if (config.white_selected and score > 1.1) or (not config.white_selected and score < -1.1):
                    bl = True
                if not config.one_player_selected or bl:
                    config.draw = True
                    config.counter = 0
                    config.increment_counter = True
                    config.white_score += 0.5
                    config.black_score += 0.5
                else:
                    config.draw_declination = True
                    config.draw_counter = 0
            # White resign
            elif 790 <= x <= 830 and 280 <= y <= 320:
                if config.one_player_selected and not config.white_selected:
                    return False
                config.white_resign = True
                config.counter = 0
                config.increment_counter = True
                config.black_score += 1
    return False
