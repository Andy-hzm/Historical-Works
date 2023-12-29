### Preparations ###
from random import choice as ran 
import os
block = [] # a nested list to store the puzzle
answer = [] # the answer block 
address = [] # location of the empty space
command = {} # memorize the keyboard settings
count = 0 # the number of the user's moves


### Defining functions ###
def keyboard(): # memorizing the user's keyboard settings
    global command
    print("Please enter the four letters used for left, right, up and down directions.")
    while True:
        l = input("The letter for left direction: ")
        command[l] = "left"
        break
    while True:    
        r = input("The letter for right direction: ")
        if l != r:
            command[r] = "right"
            break
        else:
            print("This key is already occupied, please try another key.")
            continue
    while True:
        u = input("The letter for up direction: ")
        if l != u and r != u:
            command[u] = "up"
            break
        else:
            print("This key is already occupied, please try another key.")
            continue 
    while True:    
        d = input("The letter for down direction: ")
        if l != d and r != d and u != d:
            command[d] = "down"
            break
        else:
            print("This key is already occupied, please try another key.")
            continue


def movement(d): # switch the position of the empty space and one adjacent number
    global block,address
    x = address[0]
    y = address[1]
    if d == "left":
        block[y][x+1], block[y][x] = block[y][x], block[y][x+1]
        address[0] += 1
    elif d == "right":
        block[y][x-1], block[y][x] = block[y][x], block[y][x-1]
        address[0] -= 1
    elif d == "up":
        block[y+1][x], block[y][x] = block[y][x], block[y+1][x]
        address[1] += 1
    elif d == "down":
        block[y-1][x], block[y][x] = block[y][x], block[y-1][x]
        address[1] -= 1


def block_generator(d): # generate the answer block
    global block, address, answer
    address.append(d-1)
    address.append(d-1)
    for i in range(1,d+1):
        block.append([])
        for m in range(d*i-d+1,d*i+1):
            block[i-1].append(m)
    block[d-1][d-1] = " "
    for i in range(0,len(block)):
        answer.append(block[i][:])


# return available directions according to the empty space's position
def availability_check(): 
    global block, address
    clist = ["right","left","up","down"] 
    if address[0] == 0:
        clist.remove("right")
        if address[1] == 0:
            clist.remove("down")
        elif address[1] == len(block)-1:
            clist.remove("up")
    elif address[0] == len(block)-1:
        clist.remove("left")
        if address[1] == 0:
            clist.remove("down")
        if address[1] == len(block)-1:
            clist.remove("up")
    else:
        if address[1] == 0:
            clist.remove("down")
        if address[1] == len(block)-1:
            clist.remove("up")
    return clist


def puzzle_generator(): # move the standard block randomly to create a puzzle
    global block, address,dimension
    for i in range(1,dimension**4):
        instruct = ran(availability_check())
        movement(instruct)


def block_show(): # print the block
    global block
    for i in range(0,len(block)):
        for m in block[i]:
            if m is int:
                print("%-3d"%m, end =" ")
            else:
                print("%-3s"%m, end =" ")
        print("")


# return a string indicating the available direction and its relevant key
def show_available_dir(): 
    check = availability_check()
    string = ""
    key = list(command.keys())
    value = list(command.values())
    for i in check:
        index = value.index(i)
        string += value[index] + "---" + key[index] + " "
    return(string)


# the whole process for single movement
def single_step(): 
    global block,address
    while True:
        try:
           print(">> Available directions(with their set keys): ",show_available_dir(),"<<")
           step = input("Enter your move >>> ")
           if availability_check().count(command[step]) == 1:
               movement(command[step])
               break
           else:
               print("Please note that again, only these directions are available: ")
               print(show_available_dir()) 
               continue         
        except:
            print("Please make sure that you enter the correct key.")
            continue



### Main process ###

print("""Welcome!!!! My freind!!!

Welcome to my sliding puzzle!!!

In this puzzle, you will get a disorded number tables.

You can choose any dimensions up to 10x10, minimum dimension is 3x3.

The board has an empty space where an adjacent tile can be slide to. 

You are going to help me rearrange the tiles into a sequential order 
by their numbers(left to right, top to bottom) by repeatedly making 
sliding moves(left, right, up or down).

Your steps taken will be counted and shown when you finish the game.""") # welcoming
while True:
    block,answer,address,command,count =[],[],[],{},0 #initialize the game
    print("Now let's get started! ")
    print("""What dimension of puzzle do you want?
    Please choose from the following dimension.
    >>> 3,4,5,6,7,8,9,10 <<<
    (e.g "3" means "3x3")""")
    
    while True: # Choosing dimension
        try:
            dimension = int(input("Dimension: ")) 
            if dimension in [3,4,5,6,7,8,9,10]:
                break
            else:
                print("Please note that you could only choose form 3x3 to 10x10.")
                print("Please enter your choice again.")
                continue
        except:
            print("Please check your input again. I can't understand you.")
            continue

    # settings
    block_generator(dimension)
    puzzle_generator()
    keyboard() 

    while block != answer: # user solving puzzle
        i = os.system("cls") # make the interface cleaner
        block_show()
        single_step()
        count += 1
    
    block_show()
    print("Congratulations! You solved the puzzle!!")
    print(f"You took {count} steps to solve the puzzle!")

    while True: # ask the user if he wants to play again
        try:
            check = input("""Do you want to play again?
(Press "y" for yes, "n" to quit.)""")
            if check != "y" and check != "n":
                print("Please check whether your command is correct and enter it again.")
                continue
            break
        except:
            print("Please check that whether your command is correct.")
            continue
    if check == "y":
        continue
    else:
        print("Farewell, my friend! See you next time!!")
        break
