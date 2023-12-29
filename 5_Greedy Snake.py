###### Preparation ######
import random
import turtle
 
direction = "none" # later may be: up, down, left, or right
game_status = "on" # later may be lost or won
food_list = {} # food numbers(value) and their locations(key)
num_turtle = [] # turtles that write food numbers
body = [] # the stamps' positions
count_five_move = 0 # count extension while not eating (only at the beginning)
body_length = 5 # the newest snake's length
is_extending = False # whether the snake is extending
on_body = False # whether the monster on the snake's body
contact = 0
time = 0
motion = True # whether the snake is moving

# prepare a function to make it convenient to create turtles 
def add_turtle(visibility, cor, size, main_color, margin_color): 
    # visibility is a bool value/cor and size is a tuple/colors are string
    tur = turtle.Pen("square", visible=visibility)
    tur._tracer(0)
    tur.up()
    tur.color(margin_color, main_color)
    tur.shapesize(size[0]/20, size[1]/20)
    tur.goto(cor[0], cor[1])
    tur._update()
    turtle.tracer(1)
    return tur

turtle.screensize(740,660,"white")
snake = add_turtle(True, (0,-40), (20,20), "red", "red") # prepare the snake
snake.speed(1)
monster = add_turtle(True, (-170,-210), (20,20), "purple", "purple") # prepare the monster
monster.speed(1)

contact_str = add_turtle(False, (-200,240),(20,20),"black","black") # prepare the initial status area
contact_str.write("Contact: 0",font=("Arial",15))
time_str = add_turtle(False, (-70,240),(20,20),"black","black")
time_str.write("Time: 0",font=("Arial",15))
motion_str = add_turtle(False,(70,240),(20,20),"black","black")
motion_str.write("Motion: Paused",font=("Arial",15))
 
 
###### Defining functions ######
# < preparing functions > #
def plot_margin(): # plot the margin by a turtle
    turtle.tracer(0) 
    plot_turtle = turtle.Pen(visible=False)
    plot_turtle.up()
    plot_turtle.goto(-250, 210)
    plot_turtle.down()
    plot_turtle.goto(250, 210)
    plot_turtle.goto(250, -290)
    plot_turtle.goto(-250, -290)
    plot_turtle.goto(-250, 290)
    plot_turtle.goto(250, 290)
    plot_turtle.goto(250,210)
    turtle.update()

def generate_food(): # randomly generate food within the gaming area
    global food_list, num_turtle
    turtle.tracer(0)
    w1 = turtle.Pen(visible=False) # turtles used to write each food number
    w2 = turtle.Pen(visible=False)
    w3 = turtle.Pen(visible=False)
    w4 = turtle.Pen(visible=False)
    w5 = turtle.Pen(visible=False)
    w6 = turtle.Pen(visible=False)
    w7 = turtle.Pen(visible=False)
    w8 = turtle.Pen(visible=False)
    w9 = turtle.Pen(visible=False)
    num_turtle = [None,w1,w2,w3,w4,w5,w6,w7,w8,w9]
    for i in range(1,10):
        while True:    
            x = random.randint(-12,12) # divide the gaming board into 25x25 unit blocks
            y = random.randint(-12,12) # one unit block equals the size of snake and monster 
            x = 20 * x
            y = 20 * y - 40
            if (x,y) == (0,-40):
            # make sure the number won't generate on the snake
                continue
            elif (x,y) == (-180,-200) or (x,y) == (-160,-200) or (x,y) == (-160,-220) or (x,y) == (-160,-220):
            # make sure the number won't generate on monster
                continue 
            elif (x,y) in food_list:
            # make sure the numbers don't generate on the same position
                continue
            else:
                break
        food_list[(x,y)] = i
        num_turtle[i] = add_turtle(False, (x-3,y-10), (20,20), "black", "black")
        num_turtle[i].write(i,font=(0.7))
    turtle.tracer(1)

def instruction(): # welcoming message and brief introduction
    instruct = add_turtle(False, (-230, 70),(20,20),"black", "black")
    instruct.write("""   Welcome to Andy's version of snake game....
     
    You are going to use the 4 arrow keys to move the snake around 
    the screen, trying to consume all the food items before the 
    monster catches you...You can stop the snake by the "Space Bar". 
     
    Click anywhere on the screen to start the game, have fun!!""", font=("Arial",12,"normal"))
    return instruct


# < key board functions > # 
def collect_direction(): # connect to keyboard
    turtle.onkey(store_up,"Up")    
    turtle.onkey(store_down,"Down")
    turtle.onkey(store_left,"Left")
    turtle.onkey(store_right,"Right")
    turtle.onkey(reverse_motion,"space")
 
def store_up(): # integrate the "collect_direction()" function, below the same
    global direction, motion
    if not motion:
        motion = not motion
    direction = "up"
def store_down():
    global direction, motion
    if not motion:
        motion = not motion
    direction = "down"
def store_left():
    global direction, motion
    if not motion:
        motion = not motion
    direction = "left"
def store_right():
    global direction, motion
    if not motion:
        motion = not motion
    direction = "right"
def reverse_motion(): # pause or un-pause the snake
    global motion
    motion = not motion


# < moving functions > # 
def move_snake(): # move the snake and make it correspondingly react to all status changes
    global direction, game_status, count_five_move, is_extending, motion
    x, y = snake.xcor(), snake.ycor()
    collect_direction()
    check_lost() # check whether the monster catches up
    check_in_food_list(x, y) # check whether encounters a food item
    if game_status == "on":
        if motion:
            if direction == "up":
                move_snake_once(x,y,x,y+20,"Up")
            elif direction == "down":
                move_snake_once(x,y,x,y-20,"Down")
            elif direction == "right":
                move_snake_once(x,y,x+20,y,"Right")
            elif direction == "left":
                move_snake_once(x,y,x-20,y,"Left")
            check_lost() # check again (avoid possible error)
        
        if is_extending: # slower the snake's speed while extending
            turtle.ontimer(move_snake,250) 
        else:
            turtle.ontimer(move_snake,220)
    
    elif game_status == "lost": # stops if loses
        game_over = add_turtle(False, (monster.xcor()-100,monster.ycor()),(20,20),"red", "red")
        game_over.write("Game over!",font=("Arial",12,"normal"))
    else: # stops if wins
        you_won = add_turtle(False, (snake.xcor()-100,snake.ycor()),(20,20),"red", "red")
        you_won.write("Winner!",font=("Arial",12,"normal"))

def move_snake_once(x_0, y_0, x_new, y_new, direc): # conduct single move of snake and update the status area
    get_stamp(x_0, y_0)
    change_motion_str(direc)
    if check_in_board(x_new, y_new):
        snake.goto(x_new, y_new)
        clear_stamp()
        
# "get_stamp(x,y)" and "clear_stamp()" integrate the snake's body movement
def get_stamp(x, y): # take stamps for the snake's head
    global body
    snake._tracer(0)
    snake.color("blue", "black")
    snake.stamp()
    snake.color("red")
    snake._update()
    snake._tracer(1)
    body.append((x, y))

def clear_stamp(): # clear the last stamps while moving and not extending
    global body, body_length, is_extending
    if len(body) <= body_length:
        is_extending = True
    else:
        is_extending = False
        snake.clearstamps(1)
        body.remove(body[0])    

def monster_direction(): # make sure the monster is moving towards snake taking the fastest path
    # return values can be "evaled" conveniently
    x_snake, y_snake = snake.xcor(), snake.ycor()
    x_monster, y_monster = monster.xcor(), monster.ycor()
    x_dif = x_snake - x_monster
    y_dif = y_snake - y_monster
    if abs(x_dif) <= abs(y_dif):
        if y_dif > 0:
            return "monster.seth(90)"
        else:
            return "monster.seth(270)"
    else:
        if x_dif > 0:
            return "monster.seth(0)"
        else:
            return "monster.seth(180)"

def move_monster(): # move the monster and make it correspondingly react to all status changes
    global game_status,contact
    monster._tracer(0) # set moving directions
    path = monster_direction()
    eval(path)
    monster._tracer(1)

    check_on_body() # update status area
    check_lost() # check whether catches up the snake 
    monster.forward(20)
    check_lost() # check again
    if game_status == "on":
        time_gap = random.randint(200,800)
        turtle.ontimer(move_monster, time_gap)    


# < status area functions > # 
def change_motion_str(motion): # update the "Motion" in the status area 
    motion_str._tracer(0)
    motion_str.clear()
    motion_str.write("Motion: " + motion,font=("Arial",14,"normal"))
    motion_str._tracer(1)

def change_contact_str(count): # update the "Contact" in the status area
    contact_str._tracer(0)
    contact_str.clear()
    contact_str.write("Contact: " + str(count),font=("Arial",14,"normal"))
    contact_str._tracer(1)
 
def change_time_str(): # update the "Time" in the status area
    global time, game_status
    if game_status == "on":    
        time_str._tracer(0)
        time_str.clear()
        time += 1
        time_str.write("Time: " + str(time),font=("Arial",14,"normal"))
        time_str._tracer(1)
        turtle.ontimer(change_time_str,1000)


# < checking functions > # 
def check_on_body(): # check whether the monster is on the body of the snake and count the contact time
    global body, on_body, contact
    if on_body: # stay on the body or leave the body
        for body_x, body_y in body:
            if abs(body_x - monster.xcor()) < 20 and abs(body_y - monster.ycor()) < 20:
                on_body = True
                break
            else:
                on_body = False
    else: # away from the body or enter the body
        for body_x, body_y in body:
            if abs(body_x - monster.xcor()) < 20 and abs(body_y - monster.ycor()) < 20:
                contact += 1
                change_contact_str(contact)
                on_body = True
                break

def check_in_food_list(x,y): # check whether the place where the snake enters has a food item
    # if all the food eaten, end the game
    global food_list, num_turtle, body_length, game_status
    if (x,y) in food_list:
        num = food_list[(x,y)]
        num_turtle[num].clear()
        food_list.pop((x,y))
        body_length += num
    if len(food_list) == 0:
        game_status = "win" 

def check_in_board(x, y): # make sure that the snake won't go out of the board
    if -240 <= x <= 240 and -280 <= y <= 200:
        return True
    else:
        return False

def check_lost(): # check whether the monster catches up the snake
    global game_status
    x_snake, y_snake = snake.xcor(), snake.ycor()
    x_monster, y_monster = monster.xcor(), monster.ycor()
    if abs(x_monster - x_snake) < 20 and abs(y_monster - y_snake) < 20:
        game_status = "lost"


# < the function to start the game in "onscreenclick" > #
def main_game(x,y):
    turtle.onscreenclick(None) # make sure only one click is effective 
    instruct.clear() # remove the welcoming message
    generate_food()
    turtle.ontimer(move_snake,200)
    turtle.ontimer(move_monster,200)
    turtle.ontimer(change_time_str(),1000)


###### main process ######
plot_margin()
instruct = instruction()

turtle.onscreenclick(main_game)

turtle.listen() # make sure the board is active
turtle.mainloop()
