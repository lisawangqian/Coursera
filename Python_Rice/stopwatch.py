# template for "Stopwatch: The Game"
import simplegui
# define global variables
canvas_width = 400
canvas_height = 300
interval = 100
count = 0
succ = 0
total = 0
score = "0/0"
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = int(t / 10/ 60) 
    sec= int(t / 10/ 10) % 6
    sec2 = int(t / 10) % 10
    tsec = int(t) % 10
    disp = str(m) + ":" + str(sec) + str(sec2) + "." + str(tsec)
    return disp
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global count, succ, total, score, running
    if timer.is_running() == running:
        timer.stop()
        if count % 10 == 0:
            succ += 1
            total += 1
        else:
            total += 1
            
    score = str(succ) + "/" + str(total)

def reset():
    global count, succ, total, score
    timer.stop()
    format(0)
    count = 0
    succ = 0
    total = 0
    score = str(succ) + "/" + str(total)

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(count)), [120, 160], 70, "White")
    canvas.draw_text(score, [350, 40], 22, "Yellow")
    
    
# create frame
f = simplegui.create_frame("Stopwatch", canvas_width, canvas_height)


# register event handlers

timer = simplegui.create_timer(interval, tick)
f.add_button("Start", start, 120)
f.add_button("Stop", stop, 120)
f.add_button("Reset", reset, 120)
f.set_draw_handler(draw)

# start frame
f.start()

# Please remember to review the grading rubric

