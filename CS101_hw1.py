##################################################################
# Title : Defuse Bombs
# Author : jae ryoung ka
# The number of hours taken for finishing the homework :
##################################################################

from cs1robots2 import * # import the upgraded module

def turn_right():
    for i in range(3):
        hubo.turn_left()
def turn_back():
    for i in range(2):
        hubo.turn_left()

load_world('worlds/terror6.wld')

hubo = Robot(beepers=10000) # Modify the number of beepers if your implementation needs more beepers.

hubo.drop_beeper() # Indicate the start as well as the end point
hubo.move()

def defuse_and_move():
    if not hubo.on_beeper():
        if hubo.left_is_clear() or hubo.right_is_clear(): # if hubo is on junction, drop TWO beepers. My code is somewhat different from the guideline;
            hubo.drop_beeper()
            hubo.drop_beeper()
    if hubo.on_beeper(): # if hubo is on beeper, pick ONE beeper even when hubo already dropped beeper right before the action.
        hubo.pick_beeper()
        hubo.turn_left()   # then, turn left.
        
    if hubo.front_is_clear(): # if front is clear, just move on.
        hubo.move()
    else: # if not, turn back. If there is bomb then pick it up
        if hubo.on_bomb(): # bomb only exists in the end of roads. So if front is clear, we don't have to try defusing a bomb.
            hubo.defuse_bomb()         
        turn_back()

    
    
while not hubo.on_beeper() or hubo.front_is_clear() or hubo.left_is_clear() or hubo.right_is_clear(): # An example termination condition.
    defuse_and_move()    # repeat that move til hubo arrives home.
    
hubo.pick_beeper()