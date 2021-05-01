import abc
import config
import utility

class Player(metaclass=abc.ABCMeta):
    def __init__(self, colour):
        self.colour = colour

    def game_over(self):
        # Look for checkmate; note that we have switched the turn already
        if config.check:
            if utility.is_checkmate(config.pieces, config.turn):
                config.print_checkmate = True
                if config.turn == "black":
                    config.white_score += 1
                else:
                    config.black_score += 1

        # Look for stalemate
        if not config.check and utility.is_checkmate(config.pieces, config.turn):
            config.print_stalemate = True
        if utility.insufficient("white") and utility.insufficient("black"):
            config.print_stalemate = True

