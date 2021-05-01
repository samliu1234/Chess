# Imports
import abc
import copy
import utility


# Piece abstract class
class Piece(metaclass=abc.ABCMeta):
    white_image = None
    black_image = None
    @abc.abstractmethod
    def __init__(self, name, colour, x, y):
        self.name = name
        self.colour = colour
        self.x = x
        self.y = y
        self.xpx = (self.x - 1) * 75
        self.ypx = (self.y - 1) * 75
        self.alive = True
        self.move_count = 0

    # Draws the piece
    def draw(self, win):
        if self.colour == "white":
            win.blit(self.white_image, (self.xpx, self.ypx))
        else:
            win.blit(self.black_image, (self.xpx, self.ypx))

    # Describes the piece
    def description(self):
        if self.colour == "white":
            print("White " + self.name)
        else:
            print("Black " + self.name)

    # Moves the piece
    def move(self, xsquare, ysquare, index):
        # Pops self from list of pieces for now
        temp = utility.get_pieces()
        temp.pop(index)

        # Updates details
        self.x = xsquare
        self.y = ysquare
        self.xpx = (self.x - 1) * 75
        self.ypx = (self.y - 1) * 75
        utility.clear_circles()
        self.move_count += 1

        # Delete any piece that is on the square
        for piece in temp:
            if piece.x == self.x and piece.y == self.y and piece.colour != self.colour:
                temp.remove(piece)
                utility.set_numbers(piece.colour, piece.name)

        # Add back self
        temp.append(self)
        utility.set_pieces(temp)

        # Look for check
        threatened_list = utility.get_threatened_squares(utility.get_pieces(), self.colour)
        for piece in utility.get_pieces():
            if piece.name == "king" and piece.colour != self.colour:
                if threatened_list.__contains__([piece.x, piece.y]):
                    utility.set_check()
                    break

    # Returns a boolean indicating whether the king is still in check
    def simulate_move(self, xsquare, ysquare, list_to_use):
        # We need to check two things: (1) if the piece blocked the check or if the king moved away from the check,
        # (2) if the threatening piece was taken

        temp = copy.deepcopy(list_to_use)

        # Since a copy was made, "self" is no longer contained, change the coordinates of this piece
        for piece in temp:
            if piece.x == self.x and piece.y == self.y:
                piece.x = xsquare
                piece.y = ysquare
                break

        # Pop the piece that may have been captured in this move
        for piece in temp:
            if piece.x == xsquare and piece.y == ysquare and piece.colour != self.colour:
                temp.pop(temp.index(piece))
                break

        # Get all the threatened squares
        threatened_list = utility.get_threatened_squares(temp, utility.get_other_colour(self.colour))

        # Get king's coordinates
        kingx = 0
        kingy = 0
        for piece in temp:
            if piece.colour == self.colour and piece.name == "king":
                kingx = piece.x
                kingy = piece.y
                break

        # Check if the king is still threatened
        if threatened_list.__contains__([kingx, kingy]):
            return True

        return False

    # Method that simulates a move for the AI
    def ai_simulate(self, xsquare, ysquare, piece_list):
        temp = copy.deepcopy(piece_list)
        # Since a copy was made, "self" is no longer contained, change the coordinates of this piece
        for piece in temp:
            if piece.x == self.x and piece.y == self.y:
                piece.x = xsquare
                piece.y = ysquare
                break

        # Pop the piece that may have been captured in this move
        for piece in temp:
            if piece.x == xsquare and piece.y == ysquare and piece.colour != self.colour:
                temp.pop(temp.index(piece))
                break
        return utility.eval_board(temp)

    # Abstract method that gets the squares that the piece threatens
    def get_threatened_squares(self, list_to_use):
        pass

    # Abstract method that displays options
    def show_options(self, list_to_use):
        pass
