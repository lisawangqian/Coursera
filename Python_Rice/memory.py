# implementation of card game - Memory

import simplegui
import random
list = []
exposed = []
state = 0
select_one = 0
select_two = 0
turns = 0



# helper function to initialize globals
def new_game():
    global state, list, exposed, turns, select_one, select_two
    
    
    frame.set_canvas_background("Green")
    list = []
    state = 0
    turns = 0
    select_one = 0
    select_two = 0
    for i in range (0,8):
        list.append(i)
    list.extend(list)
    random.shuffle(list)
    
    exposed = [False for i in range (0,16)]
    
    label.set_text("Turns = " + str(turns))
    
   
         

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, select_one, select_two, turns
    click = int(pos[0]/50)
    if state == 0:
        exposed[click] = True
        select_one = click
        state = 1
        
    elif state == 1:
       if not exposed[click]:
          exposed[click] = True
          select_two = click
          state = 2
          turns +=1
    else :
       if not exposed[click]:
            if list[select_one]==list[select_two]:
              exposed[select_one]=True
              exposed[select_two]=True
            else:
              exposed[select_one]=False
              exposed[select_two]=False
            exposed[click]=True
            select_one = click
            state = 1
            
    label.set_text("Turns = " + str(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    canvas.draw_line([0, 100], [800, 100], 4, "Black")
    canvas.draw_line([800, 0], [800, 100], 4, "Black")
    canvas.draw_line([0, 0], [800, 0], 4 , "Black")
    canvas.draw_line([0, 0], [0, 100], 4, "Black")
    
    for i in range(0,16):
      canvas.draw_line([50 * (i + 1), 0],  [50 * (i + 1), 100], 4, "Black")
      if exposed[i]:
         canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*(i+1), 100], [50*(i+1), 0]], 2, 'Black', 'Black')
         canvas.draw_text(str(list[i]), [15+ 50 * i, 60], 35, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
