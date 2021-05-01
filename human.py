# Import statements
import config
import utility
import knight
import bishop
import rook
import queen
from player import Player


# Pygame declarations
import pygame
pygame.init()


class Human(Player):
    def __init__(self, colour):
        super().__init__(colour)

    def after_each_move(self, event):
        # Deal with promotion
        if (config.white_promotion and self.colour == "white") or (config.black_promotion and self.colour == "black"):
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                ind = 0
                if config.white_promotion:
                    # Get index of pawn that will be promoted
                    for piece in config.pieces:
                        if piece.name == "pawn" and piece.colour == "white":
                            ind = config.pieces.index(piece)
                    # If user selects knight
                    if 700 <= pos[0] <= 800 and 50 <= pos[1] <= 150:
                        tmp = knight.Knight("knight", "white", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(
                            knight.Knight("knight", "white", config.pieces[ind].x, config.pieces[ind].y))
                        # Move the piece to its current spot to display check
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.white_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    # Bishop
                    elif 700 <= pos[0] <= 800 and 175 <= pos[1] <= 275:
                        tmp = bishop.Bishop("bishop", "white", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(
                            bishop.Bishop("bishop", "white", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.white_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    # Rook
                    elif 700 <= pos[0] <= 800 and 300 <= pos[1] <= 400:
                        tmp = rook.Rook("rook", "white", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(rook.Rook("rook", "white", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.white_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    # Queen
                    elif 700 <= pos[0] <= 800 and 430 <= pos[1] <= 530:
                        tmp = queen.Queen("queen", "white", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(queen.Queen("queen", "white", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.white_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1

                # Same as above, except black
                elif config.black_promotion:
                    for piece in config.pieces:
                        if piece.name == "pawn" and piece.colour == "black":
                            ind = config.pieces.index(piece)
                    if 700 <= pos[0] <= 800 and 50 <= pos[1] <= 150:
                        tmp = knight.Knight("knight", "black", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(
                            knight.Knight("knight", "black", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.black_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    elif 700 <= pos[0] <= 800 and 175 <= pos[1] <= 275:
                        tmp = bishop.Bishop("bishop", "black", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(
                            bishop.Bishop("bishop", "black", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.black_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    elif 700 <= pos[0] <= 800 and 300 <= pos[1] <= 400:
                        tmp = rook.Rook("rook", "black", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(rook.Rook("rook", "black", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.black_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1
                    elif 700 <= pos[0] <= 800 and 430 <= pos[1] <= 530:
                        tmp = queen.Queen("queen", "black", config.pieces[ind].x, config.pieces[ind].y)
                        config.pieces.append(queen.Queen("queen", "black", config.pieces[ind].x, config.pieces[ind].y))
                        config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                        config.black_promotion = False
                        config.pieces.pop(ind)
                        config.move -= 1

    def get_move(self, event):
        if config.turn is not self.colour:
            return
        # Check for user click
        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if not config.pressed_piece:
                # Look for the piece that was pressed
                for piece in config.pieces:
                    if piece.colour == config.turn and piece.xpx < pos[0] < piece.xpx + 75 and piece.ypx < pos[
                        1] < piece.ypx + 75:
                        # Get possible moves of that piece
                        config.circles = piece.show_options(config.pieces)

                        # If no possible moves, user can click another piece without having to click out
                        if len(config.circles) == 0:
                            break

                        # Get coordinates of the piece to display yellow highlight
                        config.to_move = [piece.xpx, piece.ypx]

                        config.current_piece_number = config.pieces.index(piece)
                        config.pressed_piece = True
                        break

            else:
                # Get pressed square
                xsquare = pos[0] // 75 + 1
                ysquare = pos[1] // 75 + 1

                # If this is a possible move
                if config.circles.__contains__([xsquare, ysquare]):
                    # Remove current check
                    config.check = False

                    # Move piece
                    if not config.flip:
                        config.last_move = [config.pieces[config.current_piece_number].xpx,
                                            config.pieces[config.current_piece_number].ypx, xsquare * 75 - 75,
                                            ysquare * 75 - 75]
                    else:
                        config.last_move = [config.pieces[config.current_piece_number].xpx,
                                            utility.flip_coordinate(config.pieces[config.current_piece_number].ypx),
                                            xsquare * 75 - 75, utility.flip_coordinate(ysquare * 75 - 75)]
                    # Since the piece at position config.current_piece_number may change after a move
                    tmp_name = config.pieces[config.current_piece_number].name
                    config.pieces[config.current_piece_number].move(xsquare, ysquare, config.current_piece_number)

                    if config.flip:
                        config.moves_up = utility.get_other_colour(config.moves_up)
                        if tmp_name != "pawn":
                            utility.switch_board()
                            print(tmp_name + " Switching")
                    config.move += 1

                    # TURN IS SWITCHED HERE
                    utility.switch_turn()
                    self.after_each_move(event)

                else:
                    config.circles.clear()
                config.pressed_piece = False

                # Remove highlight
                config.to_move = [-100, -100]

        super().game_over()
