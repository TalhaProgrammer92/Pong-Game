# Modules
import pygame, sys, random

##########################
# General setup
##########################
pygame.init()                   # Initializing the game
clock = pygame.time.Clock()     # Initializing game clock for FPS
FPS = 60                        # Frames per second - Definition


##########################
# Setting up the window
##########################
win_width = 800                                                 # Defining the window's width
win_height = 600                                                # Defining the window's height
window = pygame.display.set_mode((win_width, win_height))       # Setting up the window's resolution
pygame.display.set_caption('Pong Game')                         # Setting the window's title


##########################
# Game objects
##########################

# Ball - Game object - Rectangle Canvas
# 1st two args are the position (x, y) and last two are the size (width, height) of the ball
ball_size_x = 20                                        # Size - Horizontal
ball_size_y = 20                                        # Size - Vertical
ball_speed_x = 4.5 * random.choice((1, -1))             # Speed - Horizontal
ball_speed_y = 4.5 * random.choice((1, -1))             # Speed - Vertical
ball_position_x = win_width / 2 - ball_size_x / 2       # To put it at centre
ball_position_y = win_height / 2 - ball_size_y / 2      # To put it at centre
ball_object = pygame.Rect(ball_position_x, ball_position_y, ball_size_x, ball_size_y)

# Players - Game Objects - Rectangle Canvas
# Same args as ball but different values
player1_speed = 0           # Speed - Player 1
player1_size_x = 10         # Size - Horizontal
player1_size_y = 100        # Size - Vertical
player1_position_x = win_width - 20                         # To put at left side
player1_position_y = win_height / 2 - player1_size_y / 2    # To put at centre

player2_speed = 0           # Speed - Player 2
player2_position_x = 10                                     # To put at right side

player1_object = pygame.Rect(player1_position_x, player1_position_y, player1_size_x, player1_size_y)
player2_object = pygame.Rect(player2_position_x, player1_position_y, player1_size_x, player1_size_y)

# Background color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


##########################
# Functions
##########################

def ball_reset() -> None:
    """ Function to reset the ball position """
    global  ball_speed_y, ball_speed_x
    ball_object.center = (win_width / 2, win_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def ball_animation() -> None:
    """ Function to move the ball object and detect collisions to create a smooth animation """
    global ball_speed_x, ball_speed_y

    # Motion - Ball
    ball_object.x += ball_speed_x
    ball_object.y += ball_speed_y

    # Collision detection - Ball
    if ball_object.top <= 0 or ball_object.bottom >= win_height:        # Vertical - y axis
        ball_speed_y *= -1
    if ball_object.left <= 0 or ball_object.right >= win_width:         # Horizontal - x axis
        ball_reset()
    if ball_object.colliderect(player1_object) or ball_object.colliderect(player2_object):      # Collision with players
        ball_speed_x *= -1

def player_animation() -> None:
    """ Function to move player object """
    player1_object.y += player1_speed
    player2_object.y += player2_speed

    # Border restriction
    if player1_object.top <= 0:
        player1_object.top = 0
    if player2_object.top <= 0:
        player2_object.top = 0

    if player1_object.bottom >= win_height:
        player1_object.bottom = win_height
    if player2_object.bottom >= win_height:
        player2_object.bottom = win_height

def draw_objects() -> None:
    """ Function to draw all the game objects / visuals """
    pygame.draw.rect(window, light_grey, player1_object)  # Player 1
    pygame.draw.rect(window, light_grey, player2_object)  # Player 2
    pygame.draw.ellipse(window, light_grey, ball_object)  # Ball
    # Seperator - at the middle of the window
    pygame.draw.aaline(window, light_grey, (win_width / 2, 0), (win_width / 2, win_height))


##########################
# Game-loop
##########################
while True:
    # Input - Event Handling
    for event in pygame.event.get():
        # Closing the window
        # pygame.QUIT checks if user click on the close button of the window
        if event.type == pygame.QUIT:
            pygame.quit()           # Close game
            sys.exit()              # Close program

        # Key pressed
        if event.type == pygame.KEYDOWN:
            # Player 1 - Control
            if event.key == pygame.K_DOWN:
                player1_speed += 5
            if event.key == pygame.K_UP:
                player1_speed -= 5
            # Player 2 - Control
            if event.key == pygame.K_w:
                player2_speed -= 5
            if event.key == pygame.K_s:
                player2_speed += 5

        # Key released
        if event.type == pygame.KEYUP:
            # Player 1 - Control
            if event.key == pygame.K_DOWN:
                player1_speed -= 5
            if event.key == pygame.K_UP:
                player1_speed += 5
            # Player 2 - Control
            if event.key == pygame.K_w:
                player2_speed += 5
            if event.key == pygame.K_s:
                player2_speed -= 5

    # Motion
    ball_animation()
    player_animation()

    # Background color of the window
    window.fill(bg_color)

    # Draw game objects and visuals
    draw_objects()

    # Updating the window screen
    pygame.display.flip()           # Window screen - Loads all images/sprites and other game objects
    clock.tick(FPS)                 # FPS - Very important
