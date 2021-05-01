import config
import utility
import random
from player import Player
import queen


class AI(Player):
    def __init__(self, colour):
        super().__init__(colour)

    def after_each_move(self):
        if (config.white_promotion and self.colour == "white") or (config.black_promotion and self.colour == "black"):
            ind = 0
            if config.white_promotion:
                # Get index of pawn that will be promoted
                for piece in config.pieces:
                    if piece.name == "pawn" and piece.colour == "white":
                        ind = config.pieces.index(piece)
                tmp = queen.Queen("queen", "white", config.pieces[ind].x, config.pieces[ind].y)
                config.pieces.append(queen.Queen("queen", "white", config.pieces[ind].x, config.pieces[ind].y))
                config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                config.white_promotion = False
            elif config.black_promotion:
                # Get index of pawn that will be promoted
                for piece in config.pieces:
                    if piece.name == "pawn" and piece.colour == "black":
                        ind = config.pieces.index(piece)
                tmp = queen.Queen("queen", "black", config.pieces[ind].x, config.pieces[ind].y)
                config.pieces.append(queen.Queen("queen", "black", config.pieces[ind].x, config.pieces[ind].y))
                config.pieces[len(config.pieces) - 1].move(tmp.x, tmp.y, len(config.pieces) - 1)
                config.black_promotion = False
            config.pieces.pop(ind)
            config.move -= 1

    def perform_move(self, x, y, i):
        config.check = False

        if not config.flip:
            config.last_move = [config.pieces[i].xpx, config.pieces[i].ypx, x * 75 - 75, y * 75 - 75]
        else:
            config.last_move = [config.pieces[i].xpx, utility.flip_coordinate(config.pieces[i].ypx), x * 75 - 75,
                                utility.flip_coordinate(y * 75 - 75)]
        # print(config.moves_up)
        config.pieces[i].move(x, y, i)

        # Flip, add move, switch turn, check for checkmate/stalemate
        if config.flip:
            config.moves_up = utility.get_other_colour(config.moves_up)
            if config.pieces[i].name != "pawn":
                utility.switch_board()
        config.move += 1
        utility.switch_turn()
        self.after_each_move()

        super().game_over()

    # Make a random move. Iterate through all the pieces, then use a random number generator to pick a move
    def random_move(self):
        if config.turn is not self.colour:
            return
        possible_moves = []
        # For each piece of the AI's colour
        for i in range(len(config.pieces)):
            piece = config.pieces[i]
            if piece.colour == config.turn:
                options = piece.show_options(config.pieces)
                for pair in options:
                    possible_moves.append([i, pair[0], pair[1]])

        ind = random.randint(0, len(possible_moves) - 1)

        # Make the move, set highlight
        i, x, y = possible_moves[ind]
        self.perform_move(x, y, i)

    def best_move(self):
        if config.turn is not self.colour:
            return
        # There's a 50% chance that a random move is played
        num = random.randint(1, 10)
        if num <= 5:
            self.random_move()
            return
        config.white_total_moves, config.black_total_moves = [0, 0]
        # [xsquare, ysquare, ind]
        to_move = []
        if self.colour == "white":
            cur_max = -9999
        else:
            cur_max = 9999
        for i in range(len(config.pieces)):
            piece = config.pieces[i]
            # Get the total number of moves for mobility
            tmp = piece.show_options(config.pieces)
            if self.colour == "white":
                config.black_total_moves += len(tmp)
            else:
                config.white_total_moves += len(tmp)
            # Simulate all possible moves
            if piece.colour == self.colour:
                for pair in tmp:
                    cur = piece.ai_simulate(pair[0], pair[1], config.pieces)
                    if (self.colour == "white" and cur > cur_max) or (self.colour == "black" and cur < cur_max):
                        cur_max = cur
                        to_move = [pair[0], pair[1], i]
        x, y, i = to_move
        self.perform_move(x, y, i)
        return
