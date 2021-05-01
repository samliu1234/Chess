# Imports
import pygame
import utility

from piece import Piece


# Knight subclass
class Knight(Piece):
    white_image = pygame.image.load("Images/whiteknight.gif")
    black_image = pygame.image.load("Images/blackknight.gif")

    def __init__(self, name, colour, x, y):
        super().__init__(name, colour, x, y)

    # All squares around it
    def get_threatened_squares(self, list_to_use):
        temporary_list = []
        directions = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]

        for pair in directions:
            newx = self.x + pair[0]
            newy = self.y + pair[1]
            if 1 <= newx <= 8 and 1 <= newy <= 8:
                temporary_list.append([newx, newy])

        return temporary_list

    # All squares around it, but remove some of those moves
    def show_options(self, list_to_use):
        temporary_list = self.get_threatened_squares(list_to_use)

        # Get threatened squares
        same_list = utility.get_same_colour(list_to_use, self.colour)
        for item in same_list:
            if temporary_list.__contains__(item):
                temporary_list.pop(temporary_list.index(item))

        if utility.get_check():
            to_pop = []
            for pair in temporary_list:
                if self.simulate_move(pair[0], pair[1], list_to_use):
                    to_pop.append(temporary_list.index(pair))

        # Prevent move if it puts the king in check
        to_pop = []
        for pair in temporary_list:
            if self.simulate_move(pair[0], pair[1], list_to_use):
                to_pop.append(temporary_list.index(pair))
        to_pop.sort(reverse=True)
        for ind in to_pop:
            temporary_list.pop(ind)

        return temporary_list
