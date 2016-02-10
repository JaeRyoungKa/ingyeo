"""Template file for KAIST CS101 Spring 2015 HW2"""

from cs1graphics import *
import cs101supplement
import random

#--------------------------------------------------------------------------------------

# predefined game constants - your program will be tested with various settings here
CELL_SIZE = 24              # the size of each square cell block            (positive integer, greater than 5)
GAME_SPEED = 8              # the speed of the game in steps per second     (positive value)
BOARD_SIZE_X = 15           # the number of cells in x-axis                 (positive integer, greater than 10)
BOARD_SIZE_Y = 15           # the number of cells in y-axis                 (positive integer, greater than 10)
LENGTH_PER_FOOD = 4         # length to be increased on each food eaten     (positive integer)
highrecord = 0
#--------------------------------------------------------------------------------------

# the game states - you should define it in various tasks below
snake_head_position_x = 0       # a x-axis index of cell where the snake's head is placed
snake_head_position_y = 0       # a y-axis index of cell where the snake's head is placed
snake_direction = 'N'           # a string representing the direction of the snake;
                                # it should be one of 'N', 'S', 'W', 'E', representing north, south, west or east, respectively.
snake_length = 1                # the length of the snake
snake_trail = [(0, 0)]          # a list holding the history of recent locations for snake's head
                                # (you don't need to modify this variable)
food_position_x = 0             # a x-axis index of cell where the food object is placed
food_position_y = 0             # a y-axis index of cell where the food object is placed
game_over = False               # True if the game is over, False otherwise

#--------------------------------------------------------------------------------------

def create_canvas(nx, ny):
    # This function is used to create a Canvas object which is the game board.
    # The width and height of the canvas should be nx * CELL_SIZE and ny * CELL_SIZE, respectively.
    #
    # used in: main()
    # 
    # nx: the number of cells in width
    # ny: the number of cells in height
    #
    # return value: a Canvas object created

    # *************************
    # *************************
    # MODIFY THE FOLLOWING CODE FOR TASK 1
    # *************************
    # *************************
    
    canvas = Canvas() # Modify this object so that it satisfies the requirements!
    canvas.setWidth(nx*CELL_SIZE)
    canvas.setHeight(ny*CELL_SIZE)
    canvas.setTitle('뱀탕 한 뚝배기 하실래예?')
    canvas.setBackgroundColor((0,190,240))
    return canvas

def initialize_game():
    # This function is used to initialize the game state variables. It is called when the game is started or reset.
    # The following global variables must be set accordingly:
    #
    #   snake_head_position_x:  a random x-axis cell index in the game board, where 0 <= x < BOARD_SIZE_X
    #   snake_head_position_y:  a random y-axis cell index in the game board, where 0 <= y < BOARD_SIZE_Y
    #   snake_direction:        set to the closer direction from its head position toward the center of the game board,
    #                           so that we can prevent accidental game over at the beginning.
    #                           *Note: You may choose any direction when a conflict occurs while determining "the direction toward the center".
    #   snake_length:           set to 1, as the game starts with length 1
    #   snake_trail:            You don't need to manually initialize this variable in this function.
    #                           Instead, call initialize_snake_trail() with newly set snake_head_position_x and snake_head_position_y as parameters.
    #                           *Note: initialize_snake_trail() is given in the template source code below. You don't need to implement it.
    #   food_position_x, food_position_y:
    #                           You don't need to manually initialize this variable in this function.
    #                           Call generate_food() right after initialize_snake_trail() is called.
    #                           *Note: You must implement generate_food() as well.
    #   game_over:              set to False as we're (re)setting the game
    #
    # used in: main(), process_keyboard_input()
    
    # *************************
    # *************************
    #   IMPLEMENT TASK 2 HERE
    # *************************
    # *************************    
    global snake_head_position_x, snake_head_position_y, snake_direction,snake_length,game_over
    snake_length = 1
    snake_head_position_x = random.randint(0,BOARD_SIZE_X-1)
    snake_head_position_y = random.randint(0,BOARD_SIZE_Y-1)    
    initialize_snake_trail(snake_head_position_x,snake_head_position_y)
    generate_food()    
    if snake_head_position_y >= snake_head_position_x and snake_head_position_x >= BOARD_SIZE_Y-snake_head_position_y:
        snake_direction = "N"
    elif snake_head_position_y >= snake_head_position_x  and snake_head_position_x < BOARD_SIZE_Y-snake_head_position_y:
        snake_direction = "E"
    elif snake_head_position_y < snake_head_position_x  and snake_head_position_x < BOARD_SIZE_Y-snake_head_position_y:
        snake_direction = "S"
    else:
        snake_direction = "W"
    game_over = False

def initialize_snake_trail(initial_head_position_x, initial_head_position_y):
    # Initialize snake_trail during the starting or resetting the game.
    # Must be used after snake_head_position_x and snake_head_position_y are properly set.
    # DO NOT EDIT THIS FUNCTION
    #
    # initial_head_position_x: initial position of the snake's head in x-axis cell index
    # initial_head_position_y: initial position of the snake's head in y-axis cell index
    #
    # used in: initialize_game()
    
    global snake_trail
    snake_trail = [(initial_head_position_x, initial_head_position_y)]

def generate_food():
    # This function is called to create a food object that the snake can eat.
    # We want to avoid the cell where the snake resides, so you should be careful on placing it.
    # Set the global variables food_position_x and food_position_y to the x and y index of the cell you have determined to place it.
    #
    # used in: initialize_game(), game_step()
    
    # *************************
    # *************************
    #   IMPLEMENT TASK 3 HERE
    # *************************
    # *************************     
    global food_position_x, food_position_y
    food_position_x = random.randint(0,BOARD_SIZE_X-1)
    food_position_y = random.randint(0,BOARD_SIZE_Y-1)
    while (food_position_x, food_position_y) in snake_trail:
        food_position_x = random.randint(0,BOARD_SIZE_X-1)
        food_position_y = random.randint(0,BOARD_SIZE_Y-1)        
    
def update_snake_position():
    # This function is called for each time step if the game is not over.
    # Proceed snake_head_position_x and snake_head_position_y by one step ahead in the direction where snake_direction indicates.
    # For example, if snake_direction is 'N', reduce snake_head_position_y by 1.
    #
    # used in: game_step()
    
    # *************************
    # *************************
    #   IMPLEMENT TASK 4 HERE
    # *************************
    # *************************
    global snake_direction, snake_head_position_y, snake_head_position_x
    if snake_direction == "N":
        snake_head_position_y -= 1
    elif snake_direction == "S":
        snake_head_position_y += 1
    elif snake_direction == "W":
        snake_head_position_x -= 1
    elif snake_direction == "E":
        snake_head_position_x += 1

def update_snake_trail():
    # Proceed snake_trail for each game step.
    # DO NOT EDIT THIS FUNCTION
    #
    # used in: game_step()
    
    global snake_trail
    if len(snake_trail) < snake_length:
        snake_trail = snake_trail + [(snake_head_position_x, snake_head_position_y)]
    else:
        snake_trail = snake_trail[1:] + [(snake_head_position_x, snake_head_position_y)]
    
def is_game_over():
    # This function is called to check if the game is over. There are two possible conditions that the game is over:
    #  1) The snake collided to the wall, i.e. One of the variables snake_head_position_x and snake_head_position_y is out of bound.
    #  2) The snake collided itself.
    #
    # used in: game_step()
    #
    # return value: True if the game over condition is met, False otherwise

    # *************************
    # *************************
    # MODIFY THE FOLLOWING CODE FOR TASK 5
    # *************************
    # *************************
    
    global snake_head_position_x, snake_head_position_y, snake_trail
    
    if (snake_head_position_x, snake_head_position_y) in snake_trail[:-1]:
        return True
    elif snake_head_position_x < 0 or snake_head_position_x >= BOARD_SIZE_X:
        return True
    elif snake_head_position_y < 0 or snake_head_position_y >= BOARD_SIZE_Y:
        return True
    else:
        return False

# Drawing functions
def create_circle(x, y, color, head = False):
    # Create a circle representing an object on the board with the given color.
    # You should fill the entire cell. Calculate the center and the radius of Circle object accordingly.
    # If head is specified as True, adjust its depth to smaller value in order that it is still shown, even if it is overlapped with any other circles.
    #
    # used in: draw_board()
    # 
    # x: x-axis cell index of the circle
    # y: y-axis cell index of the circle
    # color: color of the circle
    # head: Indicate if this circle represents the snake's head.
    #       If it is True, you must adjust the circle's depth to higher layer (in terms of depth number, smaller)
    #       so that it correctly highlights the snake's head even if it collides the body.
    #
    # return value: a Circle object created 
    
    # *************************
    # *************************
    # MODIFY THE FOLLOWING CODE FOR TASK 6
    # *************************
    # *************************
    
    circle = Circle(CELL_SIZE/2) # Modify this object so that it satisfies the requirements!
    circle.moveTo(CELL_SIZE * (1/2.0 + x), CELL_SIZE * (1/2.0 + y))
    circle.setFillColor(color)
    if head == False:
        circle.setDepth(3)
    elif head == True:
        circle.setDepth(2)
    return circle

def create_gameover_text():
    # Create a text message "GAME OVER" which is printed out at the middle of the canvas.
    # The text should have the smallest depth compared to the other objects in the canvas (i.e. the circles)
    #
    # used in: draw_board()
    #
    # return value: a Text object created
    
    # *************************
    # *************************
    # MODIFY THE FOLLOWING CODE FOR TASK 7
    # *************************
    # *************************
    global highrecord
    if len(snake_trail) >= highrecord:
        highrecord = len(snake_trail)
        text = Text('GAME OVER \n\nNEW RECORD!\n\nCurrent Record : '+str(len(snake_trail))+'\nHighest Record : '+str(highrecord)+' \n\nPress R key to try again! \n이 게임물은 전체 이용가입니다.', 15)
    else:
        text = Text('GAME OVER \n\nCurrent Record : '+str(len(snake_trail))+'\nHighest Record : '+str(highrecord)+'\n\nPress R key to try again! \n지나친 일상생활은 \n게임 이용에 방해를 줄 수 있습니다.', 15)
    text.moveTo(CELL_SIZE*BOARD_SIZE_X/2,CELL_SIZE*BOARD_SIZE_Y/2)
    text.setDepth(1) 
    return text
    

def draw_board():
    # Draw the board using the game states
    # DO NOT EDIT THIS FUNCTION
    #
    # used in: game_step()
    
    global snake_head_position_x, snake_head_position_y, snake_trail, game_over, food_position_x, food_position_y
    canvas.clear()
    canvas.add(create_circle(snake_head_position_x, snake_head_position_y, 'green', True))
    for x, y in snake_trail:
        canvas.add(create_circle(x, y, 'blue'))
    canvas.add(create_circle(food_position_x, food_position_y, 'red'))
    
    if game_over:
        canvas.add(create_gameover_text())

def is_this_cell_snakes_neck(x, y):
    # Return whether the given cell location is the former position of the snake's head (i.e. the snake's "neck")
    # DO NOT EDIT THIS FUNCTION
    #
    # used in: change_direction()
    # 
    # x: x-axis cell index to query
    # y: y-axis cell index to query
    #
    # return value: True if it is the "neck", False otherwise
    global snake_trail
    return len(snake_trail) > 1 and (x, y) == snake_trail[-2]

def change_direction(new_direction):
    # This function is called if the player intends to change the direction.
    # Set new_direction to snake_direction, if it is a valid turn.
    # It is invalid to change the direction toward the cell which was the snake's last head position (i.e. the snake's "neck").
    #    
    # used in: process_keyboard_input()
    #
    # new_direction: the direction user intended to change to
    
    # *************************
    # *************************
    #   IMPLEMENT TASK 8 HERE
    # *************************
    # *************************
    global snake_direction,snake_head_position_x,snake_head_position_y
    if new_direction == "N":
        if not is_this_cell_snakes_neck(snake_head_position_x,snake_head_position_y-1):
            snake_direction = new_direction
    elif new_direction == "S":
        if not is_this_cell_snakes_neck(snake_head_position_x,snake_head_position_y+1):
            snake_direction = new_direction 
    elif new_direction == "W":
        if not is_this_cell_snakes_neck(snake_head_position_x-1,snake_head_position_y):
            snake_direction = new_direction    
    elif new_direction == "E":
        if not is_this_cell_snakes_neck(snake_head_position_x+1,snake_head_position_y):
            snake_direction = new_direction
            
def process_keyboard_input(key):
    # Given the key, do following things:
    # DO NOT EDIT THIS FUNCTION
    #
    # R key - reset the game (using initialize_game())
    # W key - change direction to upward (using change_direction())
    # A key - change direction to left (using change_direction())
    # S key - change direction to downward (using change_direction())
    # D key - change direction to right (using change_direction())
    #
    # used in: main()
    #
    # key: the key user have pressed
    
    if key == 'r':
        initialize_game()
    elif key == 'w':
        change_direction('N')
    elif key == 'a':
        change_direction('W')
    elif key == 's':
        change_direction('S')
    elif key == 'd':
        change_direction('E')

def game_step(e):
    # Proceed the game by one step.
    # DO NOT EDIT THIS FUNCTION
    #
    # used in: main()
    #
    # e: timer event (ignored)
    
    global snake_head_position_x, snake_head_position_y, snake_length, game_over, food_position_x, food_position_y
    
    if not game_over:
        update_snake_position()
        update_snake_trail()
        if snake_head_position_x == food_position_x and snake_head_position_y == food_position_y:
            generate_food()
            snake_length += LENGTH_PER_FOOD
        
        if is_game_over():
            game_over = True
    draw_board()
    canvas.refresh()

def main():
    # Main program definition
    # DO NOT EDIT THIS FUNCTION
    
    global canvas
    
    random.seed()                                               # initialize random seed
    canvas = create_canvas(BOARD_SIZE_X, BOARD_SIZE_Y)          # create the canvas based on the number of cells in each axis
    canvas.setAutoRefresh(False)                                # update will be done manually
    initialize_game()                                           # initialize game states
    #start timer
    cs101supplement.begin_timer(1.0 / GAME_SPEED, game_step)    # start game timer so that we call game_step function periodically, GAME_SPEED per second
    while True:
        event = canvas.wait()                                   # get event
        if event.getDescription() == 'keyboard':
            key = event.getKey()                                # get key input
            process_keyboard_input(key)                         # process key inputs
        elif event.getDescription() == 'canvas close':
            cs101supplement.end_timer()                         # stop calling game_step function
            break                                               # break out of loop, effectively closing the program
            
if __name__ == '__main__': #ignore this line. main() will be executed.
    main()