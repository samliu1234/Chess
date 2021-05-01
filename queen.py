# Imports
import pygame
import utility

from piece import Piece


class Queen(Piece):
    white_image = pygame.image.load("Images/whitequeen.gif")
    black_image = pygame.image.load("Images/blackqueen.gif")

    def __init__(self, name, colour, x, y):
        super().__init__(name, colour, x, y)

    # Get threatened squares
    def get_threatened_squares(self, list_to_use):
        temporary_list = []

        for i in range(1, 8):
            if self.x + i > 8 or self.y + i > 8:
                break
            temporary_list.append([self.x + i, self.y + i])
            if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y + i]):
                break

        for i in range(1, 8):
            if self.x - i < 1 or self.y - i < 1:
                break
            temporary_list.append([self.x - i, self.y - i])
            if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y - i]):
                break

        for i in range(1, 8):
            if self.x + i > 8 or self.y - i < 1:
                break
            temporary_list.append([self.x + i, self.y - i])
            if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y - i]):
                break

        for i in range(1, 8):
            if self.x - i < 1 or self.y + i > 8:
                break
            temporary_list.append([self.x - i, self.y + i])
            if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y + i]):
                break

        for i in range(1, 8):
            if 1 <= self.x + i <= 8:
                temporary_list.append([self.x + i, self.y])
                if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y]):
                    break

        for i in range(1, 8):
            if 1 <= self.x - i <= 8:
                temporary_list.append([self.x - i, self.y])
                if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y]):
                    break

        for i in range(1, 8):
            if 1 <= self.y + i <= 8:
                temporary_list.append([self.x, self.y + i])
                if utility.get_all_positions(list_to_use).__contains__([self.x, self.y + i]):
                    break

        for i in range(1, 8):
            if 1 <= self.y - i <= 8:
                temporary_list.append([self.x, self.y - i])
                if utility.get_all_positions(list_to_use).__contains__([self.x, self.y - i]):
                    break

        return temporary_list

    # Show move options
    def show_options(self, list_to_use):
        temporary_list = []
        same_list = utility.get_same_colour(list_to_use, self.colour)

        for i in range(1, 8):
            if self.x + i > 8 or self.y + i > 8:
                break
            # If same coloured piece, stop immediately
            if same_list.__contains__([self.x + i, self.y + i]):
                break
            temporary_list.append([self.x + i, self.y + i])
            # If different coloured piece, add and stop
            if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y + i]):
                break

        for i in range(1, 8):
            if self.x - i < 1 or self.y - i < 1:
                break
            # If same coloured piece, stop immediately
            if same_list.__contains__([self.x - i, self.y - i]):
                break
            temporary_list.append([self.x - i, self.y - i])
            # If different coloured piece, add and stop
            if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y - i]):
                break

        for i in range(1, 8):
            if self.x + i > 8 or self.y - i < 1:
                break
            # If same coloured piece, stop immediately
            if same_list.__contains__([self.x + i, self.y - i]):
                break
            temporary_list.append([self.x + i, self.y - i])
            # If different coloured piece, add and stop
            if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y - i]):
                break

        for i in range(1, 8):
            if self.x - i < 1 or self.y + i > 8:
                break
            # If same coloured piece, stop immediately
            if same_list.__contains__([self.x - i, self.y + i]):
                break
            temporary_list.append([self.x - i, self.y + i])
            # If different coloured piece, add and stop
            if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y + i]):
                break

        for i in range(1, 8):
            if 1 <= self.x + i <= 8:
                # If same coloured piece, break immediately
                if same_list.__contains__([self.x + i, self.y]):
                    break
                temporary_list.append([self.x + i, self.y])
                # If different coloured piece, add then break
                if utility.get_all_positions(list_to_use).__contains__([self.x + i, self.y]):
                    break

        for i in range(1, 8):
            if 1 <= self.x - i <= 8:
                # If same coloured piece, break immediately
                if same_list.__contains__([self.x - i, self.y]):
                    break
                temporary_list.append([self.x - i, self.y])
                # If different coloured piece, add then break
                if utility.get_all_positions(list_to_use).__contains__([self.x - i, self.y]):
                    break

        for i in range(1, 8):
            if 1 <= self.y + i <= 8:
                # If same coloured piece, break immediately
                if same_list.__contains__([self.x, self.y + i]):
                    break
                temporary_list.append([self.x, self.y + i])
                # If different coloured piece, add then break
                if utility.get_all_positions(list_to_use).__contains__([self.x, self.y + i]):
                    break

        for i in range(1, 8):
            if 1 <= self.y - i <= 8:
                # If same coloured piece, break immediately
                if same_list.__contains__([self.x, self.y - i]):
                    break
                temporary_list.append([self.x, self.y - i])
                # If different coloured piece, add then break
                if utility.get_all_positions(list_to_use).__contains__([self.x, self.y - i]):
                    break

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
