# Class imports
import config
import utility
import human
import ai

# Pygame declarations
import pygame
pygame.init()

# Globals
WIDTH = 900
HEIGHT = 600

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load media
circle_image = pygame.image.load("Images/circle.gif")
white_pieces_image = pygame.image.load("Images/white_pieces.gif")
black_pieces_image = pygame.image.load("Images/black_pieces.gif")
restart_image = pygame.image.load("Images/restart.gif")
main_menu_image = pygame.image.load("images/mainmenu.gif")
white_promotion_image = pygame.image.load("Images/white_promotion.gif")
black_promotion_image = pygame.image.load("Images/black_promotion.gif")
menu_image = pygame.image.load("Images/menu.png")
options_image = pygame.image.load("Images/options.png")
black_checkmate_image = pygame.image.load("Images/black_checkmate.gif")
white_checkmate_image = pygame.image.load("Images/white_checkmate.png")
stalemate_image = pygame.image.load("Images/stalemate.gif")
flip_image = pygame.image.load("Images/flip.gif")
empty_box_image = pygame.image.load("Images/empty_box.gif")
checked_box_image = pygame.image.load("Images/checked_box.gif")
resign_draw_image = pygame.image.load("Images/resign_draw.png")
white_resignation_image = pygame.image.load("Images/white_resignation.png")
black_resignation_image = pygame.image.load("Images/black_resignation.png")
draw_image = pygame.image.load("Images/draw.png")

# Refractor images
circle_image.set_alpha(168)
menu_image = pygame.transform.scale(menu_image, (900, 600))
options_image = pygame.transform.scale(options_image, (900, 600))
flip_image = pygame.transform.scale(flip_image, (45, 30))
empty_box_image = pygame.transform.scale(empty_box_image, (22, 22))
checked_box_image = pygame.transform.scale(checked_box_image, (22, 22))
resign_draw_image = pygame.transform.scale(resign_draw_image, (175, 69))
white_resignation_image = pygame.transform.scale(white_resignation_image, (200, 550))
black_resignation_image = pygame.transform.scale(black_resignation_image, (180, 550))
draw_image = pygame.transform.scale(draw_image, (150, 400))


# Initialize colours/fonts
col = (107, 142, 35)
helvetica_30 = pygame.font.SysFont("freesansbold.ttf", 30)
helvetica_40 = pygame.font.SysFont("freesansbold.ttf", 40)
helvetica_55 = pygame.font.SysFont("freesansbold.ttf", 55)
apple_chancery_40 = pygame.font.SysFont("applechanceryttf", 30)
# print(pygame.font.get_fonts())
# (pygame.font.get_default_font())


# Variables
p1 = human.Human("white")
p2 = human.Human("black")
ai1 = ai.AI("white")
ai2 = ai.AI("black")


# Text variables
one_player_text_black = apple_chancery_40.render("1P", 1, (0, 0, 0))
two_player_text_black = apple_chancery_40.render("2P", 1, (0, 0, 0))
white_text_black = apple_chancery_40.render("White", 1, (0, 0, 0))
black_text_black = apple_chancery_40.render("Black", 1, (0, 0, 0))
one_player_text_green = apple_chancery_40.render("1P", 1, col)
two_player_text_green = apple_chancery_40.render("2P", 1, col)
white_text_green = apple_chancery_40.render("White", 1, col)
black_text_green = apple_chancery_40.render("Black", 1, col)


# Helper method that draws the background
def draw_background():
    # Fill the screen to white
    win.fill((255, 255, 255))

    # Draw board
    for x in range(0, 8):
        for y in range(0, 8):
            if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
                pygame.draw.rect(win, col, (x * 75, y * 75, 75, 75))

    # Displays promotion options
    if config.white_promotion:
        win.blit(white_promotion_image, (750 - white_promotion_image.get_size()[0] / 2, 300 - white_promotion_image.get_size()[1] / 2))
        return
    elif config.black_promotion:
        win.blit(black_promotion_image, (750 - black_promotion_image.get_size()[0] / 2, 300 - black_promotion_image.get_size()[1] / 2))
        return

    # Checked or unchecked box
    if config.flip:
        box_image = checked_box_image
    else:
        box_image = empty_box_image

    # Draw highlights for previous move
    pygame.draw.rect(win, (187, 203, 61), (config.last_move[0], config.last_move[1], 75, 75))
    pygame.draw.rect(win, (246, 246, 127), (config.last_move[2], config.last_move[3], 75, 75))

    # Draw highlights of clicked piece
    pygame.draw.rect(win, (246, 246, 127), (config.to_move[0], config.to_move[1], 75, 75))

    # Draw red box if check
    if config.check:
        for piece in config.pieces:
            if piece.colour == config.turn and piece.name == "king":
                pygame.draw.rect(win, (255, 0, 0), (piece.xpx, piece.ypx, 75, 75))

    # Checkmate
    if config.print_checkmate:
        if config.turn == "white":
            image = black_checkmate_image
        else:
            image = white_checkmate_image
        win.blit(image, (750 - image.get_size()[0] / 2, 25))
        utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)
        return

    # Stalemate
    elif config.print_stalemate:
        win.blit(stalemate_image, (750 - stalemate_image.get_size()[0] / 2, 25))
        utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)
        return

    # White resign
    elif config.white_resign:
        win.blit(white_resignation_image, (750 - white_resignation_image.get_size()[0] / 2, 300 - white_resignation_image.get_size()[1] / 2))
        utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)
        return

    # Draw
    elif config.draw:
        win.blit(draw_image, (750 - draw_image.get_size()[0] / 2, 300 - draw_image.get_size()[1] / 2))
        utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)
        return

    # Black resign
    elif config.black_resign:
        win.blit(black_resignation_image,
                 (750 - black_resignation_image.get_size()[0] / 2, 300 - black_resignation_image.get_size()[1] / 2))
        utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)
        return

    # Show restart and main menu options
    utility.default_images(win, restart_image, main_menu_image, flip_image, box_image)

    # Show resign and draw options
    win.blit(resign_draw_image,
             (750 - resign_draw_image.get_size()[0] / 2, 300 - resign_draw_image.get_size()[1] / 2))

    # Draw sidebar
    win.blit(black_pieces_image, (630, 30))
    win.blit(white_pieces_image, (630, 330))

    # List numbers/totals for black
    list_of_numbers = utility.get_numbers()
    for i in range(0, 5):
        txt = helvetica_40.render(str(list_of_numbers[i]), 1, (0, 0, 0))
        win.blit(txt, (695, 46 + 42 * i))
    txt2 = helvetica_55.render("Total: " + str(list_of_numbers[10]), 1, col)
    win.blit(txt2, (740, 130))
    txt3 = helvetica_30.render("Score: " + str(config.black_score), 1, col)
    win.blit(txt3, (765, 190))

    # List numbers/totals for white
    for i in range(0, 5):
        txt = helvetica_40.render(str(list_of_numbers[i + 5]), 1, (0, 0, 0))
        win.blit(txt, (695, 346 + 42 * i))
    txt2 = helvetica_55.render("Total: " + str(list_of_numbers[11]), 1, col)
    win.blit(txt2, (740, 430))
    txt3 = helvetica_30.render("Score: " + str(config.white_score), 1, col)
    win.blit(txt3, (765, 385))


# Helper method that draws the circles (to indicate where certain pieces can move)
def draw_circles():
    for pair in config.circles:
        win.blit(circle_image, (pair[0] * 75 - 75 + 27.5, pair[1] * 75 - 75 + 27.5))


# Helper method that writes numbers and letters that line the left and bottom of the board
def draw_letters_numbers():
    font = pygame.font.SysFont("Helvetica", 22)

    # Blue, column
    for i in range(0, 8, 2):
        tmp = font.render(str(8 - i), 1, col)
        win.blit(tmp, (6, 8 + 75 * i))

    # White, column
    for i in range(1, 8, 2):
        tmp = font.render(str(8 - i), 1, (255, 255, 255))
        win.blit(tmp, (6, 8 + 75 * i))

    # Blue, row
    for i in range(1, 8, 2):
        tmp = font.render(chr(i + 97), 1, col)
        win.blit(tmp, (62 + 75 * i, HEIGHT - 20))

    # White, row
    for i in range(0, 8, 2):
        tmp = font.render(chr(i + 97), 1, (255, 255, 255))
        win.blit(tmp, (62 + 75 * i, HEIGHT - 20))


# Method that updates the window
def draw_window():
    if config.screen == "menu":
        win.blit(menu_image, (0, 0))
    elif config.screen == "options":
        win.blit(options_image, (0, 0))
        if config.one_player_selected:
            win.blit(one_player_text_green, (625, 150))
            win.blit(two_player_text_black, (715, 150))
        else:
            win.blit(one_player_text_black, (625, 150))
            win.blit(two_player_text_green, (715, 150))
        if config.white_selected:
            win.blit(white_text_green, (555, 340))
            win.blit(black_text_black, (685, 340))
        else:
            win.blit(white_text_black, (555, 340))
            win.blit(black_text_green, (685, 340))
    else:
        draw_background()

        for piece in config.pieces:
            piece.draw(win)

        if utility.should_continue():
            draw_circles()

        draw_letters_numbers()

        # Draw declined text
        if config.draw_declination and config.draw_counter <= 20:
            config.draw_counter += 1
            obj = helvetica_55.render("Draw declined", 1, (204, 204, 0))
            win.blit(obj, (300 - obj.get_size()[0] / 2, HEIGHT / 2 - obj.get_size()[1] / 2))
            # print("Draw declined")

    pygame.display.update()


# Main loop
while config.run:
    # Delay
    pygame.time.Clock().tick(50)
    if config.increment_counter:
        config.counter += 1

    # Draw window
    draw_window()

    # print(str(config.left_castle) + ' ' + str(config.right_castle))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.run = False

        # If the user clicks play
        if config.screen == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                # Pressed options
                if 630 <= x <= 730 and 395 <= y <= 445:
                    config.screen = "options"
                    config.one_player_selected = True
                    config.white_selected = True
                    continue

        elif config.screen == "options":
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                # These are automatically true (if the user presses nothing, it should default to this)
                if 625 <= x <= 665 and 150 <= y <= 190:
                    config.one_player_selected = True
                elif 715 <= x <= 745 and 150 <= y <= 190:
                    config.one_player_selected = False
                elif 555 <= x <= 625 and 340 <= y <= 380:
                    config.white_selected = True
                elif 685 <= x <= 755 and 340 <= y <= 380:
                    config.white_selected = False
                elif 675 <= x <= 755 and 490 <= y <= 530:
                    if not config.white_selected and config.one_player_selected:
                        config.moves_up = "black"
                        utility.switch_board()
                    config.screen = "game"
                    continue

        # If we're playing the game
        else:
            # Consider game options like restart, main menu, etc.
            # Continue is necessary so move isn't performed after game is restarted
            if utility.game_options(event):
                continue

            # Deal with promotion
            if not config.one_player_selected or (config.one_player_selected and config.white_selected):
                p1.after_each_move(event)
            else:
                ai1.after_each_move()
            if not config.one_player_selected or (config.one_player_selected and not config.white_selected):
                p2.after_each_move(event)
            else:
                ai2.after_each_move()

            # THIS SHOULD ALWAYS BE LAST. Adding anything afterwards makes the computer move very slowly
            # Only run if the game is not over
            if utility.should_continue():
                # Both of these are called regardless because the turn is checked within the method
                if (not config.one_player_selected) or (config.one_player_selected and config.white_selected):
                    p1.get_move(event)
                else:
                    # ai1.random_move()
                    ai1.best_move()
                if utility.should_continue():
                    if (not config.one_player_selected) or (config.one_player_selected and not config.white_selected):
                        p2.get_move(event)
                        continue
                    else:
                        ai2.best_move()
                        # ai2.random_move()
                        continue


pygame.quit()
