# Imports
import pygame
import utility

from piece import Piece


class Pawn(Piece):
    white_image = pygame.image.load("Images/whitepawn.gif")
    black_image = pygame.image.load("Images/blackpawn.gif")

    def __init__(self, name, colour, x, y):
        super().__init__(name, colour, x, y)
        self.first_move = 0

    # Moves the piece
    def move(self, xsquare, ysquare, index):
        super().move(xsquare, ysquare, index)
        if self.first_move == 0:
            self.first_move = utility.get_move()
        if utility.get_en_passant():
            if self.colour != utility.get_move_up():
                for piece in utility.get_pieces():
                    if piece.x == xsquare and piece.y == ysquare - 1:
                        utility.get_pieces().pop(utility.get_pieces().index(piece))
                        break
            else:
                for piece in utility.get_pieces():
                    if piece.x == xsquare and piece.y == ysquare + 1:
                        utility.get_pieces().pop(utility.get_pieces().index(piece))
                        break
            utility.set_en_passant_false()

        if ysquare == 1 or ysquare == 8:
            if self.colour == "white":
                utility.set_white_promotion()
            else:
                utility.set_black_promotion()

        if utility.get_flip() and not utility.get_white_promotion() and not utility.get_black_promotion():
            utility.switch_board()

    # Diagonals
    def get_threatened_squares(self, list_to_use):
        if self.colour == utility.get_move_up():
            return [[self.x + 1, self.y - 1], [self.x - 1, self.y - 1]]
        else:
            return [[self.x + 1, self.y + 1], [self.x - 1, self.y + 1]]

    # Check single move, double move, capture, en passant
    def show_options(self, list_to_use):
        temporary_list = []

        enemy_list = utility.get_same_colour(list_to_use, utility.get_other_colour(self.colour))

        if self.colour != utility.get_move_up():
            if enemy_list.__contains__([self.x - 1, self.y + 1]):
                temporary_list.append([self.x - 1, self.y + 1])
            if enemy_list.__contains__([self.x + 1, self.y + 1]):
                temporary_list.append([self.x + 1, self.y + 1])
            if not utility.get_all_positions(list_to_use).__contains__([self.x, self.y + 1]):
                temporary_list.append([self.x, self.y + 1])
            if not utility.get_all_positions(list_to_use).__contains__(
                    [self.x, self.y + 1]) and not utility.get_all_positions(list_to_use).__contains__(
                    [self.x, self.y + 2]) and self.move_count == 0:
                temporary_list.append([self.x, self.y + 2])
            # En passant
            if self.y == 5:
                for piece in list_to_use:
                    if piece.name == "pawn" and piece.colour != self.colour and piece.y == self.y:
                        if piece.first_move == utility.get_move() - 1:
                            if piece.x == self.x - 1:
                                temporary_list.append([piece.x, piece.y + 1])
                                utility.set_en_passant_true()
                            if piece.x == self.x + 1:
                                temporary_list.append([piece.x, piece.y + 1])
                                utility.set_en_passant_true()

        else:
            if enemy_list.__contains__([self.x - 1, self.y - 1]):
                temporary_list.append([self.x - 1, self.y - 1])
            if enemy_list.__contains__([self.x + 1, self.y - 1]):
                temporary_list.append([self.x + 1, self.y - 1])
            if not utility.get_all_positions(list_to_use).__contains__([self.x, self.y - 1]):
                temporary_list.append([self.x, self.y - 1])
            if not utility.get_all_positions(list_to_use).__contains__(
                    [self.x, self.y - 1]) and not utility.get_all_positions(list_to_use).__contains__(
                    [self.x, self.y - 2]) and self.move_count == 0:
                temporary_list.append([self.x, self.y - 2])
            # En passant
            if self.y == 4:
                for piece in list_to_use:
                    if piece.name == "pawn" and piece.colour != self.colour and piece.y == self.y:
                        if piece.first_move == utility.get_move() - 1:
                            if piece.x == self.x - 1:
                                temporary_list.append([piece.x, piece.y - 1])
                                utility.set_en_passant_true()
                            elif piece.x == self.x + 1:
                                temporary_list.append([piece.x, piece.y - 1])
                                utility.set_en_passant_true()

        if utility.get_check():
            to_pop = []
            for pair in temporary_list:
                if self.simulate_move(pair[0], pair[1], list_to_use):
                    to_pop.append(temporary_list.index(pair))

            # Sort in descending order so pop index will be unaffected
            to_pop.sort(reverse=True)
            for ind in to_pop:
                temporary_list.pop(ind)

        # Prevent move if it puts the king in check
        to_pop = []
        for pair in temporary_list:
            if self.simulate_move(pair[0], pair[1], list_to_use):
                to_pop.append(temporary_list.index(pair))
        to_pop.sort(reverse=True)
        for ind in to_pop:
            temporary_list.pop(ind)
                
        return temporary_list
