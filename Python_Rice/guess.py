# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui


# initialize global variables used in your code
low = 0
high = 0
secret_number = 0
limit = 0


# helper function to start and restart the game
def new_game(new_low,new_high):
    global low, high, limit, secret_number
    low = new_low
    high = new_high
    limit = int (math.ceil(math.log((high - low), 2)))
    secret_number = random.randrange(low, high)
    print "New Game. Range is from", low, "to", high
    print "Number of remaining guesses is",limit
    print ""


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    new_game(0,100)    
      
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    new_game(0,1000)   
      
    
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, limit
    limit = limit-1
    print "Guess was", guess
    
    if int(guess) < secret_number:
        print "Higher!"
    elif int(guess) > secret_number:
        print "Lower!"
    else:
        print "Correct! The number was", secret_number
        
    if limit >=1 and int(guess) != secret_number:
        print "Number of remaining guesses is", limit
        print ""
    elif limit == 0 and int(guess) != secret_number:
        print "You ran out of guesses. The number was", secret_number 
        print ""
        new_game(low, high)
    else:
        print ""
        new_game(low, high)
    

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game(0,100)

f.start()



# always remember to check your completed program against the grading rubric
