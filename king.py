# Imports
import pygame
import utility

from piece import Piece


# King subclass
class King(Piece):
    white_image = pygame.image.load("Images/whiteking.gif")
    black_image = pygame.image.load("Images/blackking.gif")

    def __init__(self, name, colour, x, y):
        super().__init__(name, colour, x, y)

    # Move piece
    def move(self, xsquare, ysquare, index):
        super().move(xsquare, ysquare, index)
        # Move rook as well if castling
        if utility.get_left_castle() and xsquare == 3:
            for piece2 in utility.get_pieces():
                if piece2.name == "rook" and piece2.colour == self.colour and piece2.x == 1:
                    ind = utility.get_pieces().index(piece2)
                    utility.get_pieces()[ind].move(4, piece2.y, ind)
        if utility.get_right_castle() and xsquare == 7:
            for piece2 in utility.get_pieces():
                if piece2.name == "rook" and piece2.colour == self.colour and piece2.x == 8:
                    ind = utility.get_pieces().index(piece2)
                    utility.get_pieces()[ind].move(6, piece2.y, ind)

    # The king merely threatens all squares around him
    def get_threatened_squares(self, list_to_use):
        temporary_list = []
        directions = [[1, 0], [1, 1], [0, 1], [-1, -1], [-1, 0], [-1, 1], [0, -1], [1, -1]]

        for pair in directions:
            newx = self.x + pair[0]
            newy = self.y + pair[1]
            if 1 <= newx <= 8 and 1 <= newy <= 8:
                temporary_list.append([newx, newy])

        return temporary_list

    # Show all the possible moves of the king
    def show_options(self, list_to_use):
        utility.set_left_castle_false()
        utility.set_right_castle_false()
        temporary_list = []
        directions = [[1, 0], [1, 1], [0, 1], [-1, -1], [-1, 0], [-1, 1], [0, -1], [1, -1]]

        for pair in directions:
            newx = self.x + pair[0]
            newy = self.y + pair[1]
            if 1 <= newx <= 8 and 1 <= newy <= 8:
                if not utility.get_same_colour(list_to_use, self.colour).__contains__([newx, newy]):
                    temporary_list.append([newx, newy])

        # Get threatened squares
        threatened_list = utility.get_threatened_squares(list_to_use, utility.get_other_colour(self.colour))

        # If a different coloured piece occupies this spot, the king can still move there as long as it is not defended
        for pair in threatened_list:
            if temporary_list.__contains__(pair):
                temporary_list.pop(temporary_list.index(pair))

        # Look to pop move if it doesn't bring the king out of check
        if utility.get_check():
            to_pop = []
            for pair in temporary_list:
                if self.simulate_move(pair[0], pair[1], list_to_use):
                    to_pop.append(temporary_list.index(pair))

            # Sort in descending order so pop index will be unaffected
            to_pop.sort(reverse=True)
            for ind in to_pop:
                temporary_list.pop(ind)

        # Look to castle only if the king isn't under check
        else:
            # Can castle
            if self.colour == utility.get_turn() and self.move_count == 0 and self.x == 5:
                # print(self.move_count)
                # Get pieces blocking
                threatened_list = threatened_list + utility.get_all_positions(list_to_use)

                # Check for castling
                for piece in list_to_use:
                    if piece.colour == self.colour and piece.name == "rook" and piece.move_count == 0:
                        # King side castle
                        if piece.x == 1:
                            if not threatened_list.__contains__([3, self.y]) and not threatened_list.__contains__([4, self.y]):
                                temporary_list.append([3, self.y])
                                utility.set_left_castle_true()

                        # Queen side castle
                        else:
                            if not threatened_list.__contains__([6, self.y]) and not threatened_list.__contains__([7, self.y]):
                                temporary_list.append([7, self.y])
                                utility.set_right_castle_true()

        return temporary_list
