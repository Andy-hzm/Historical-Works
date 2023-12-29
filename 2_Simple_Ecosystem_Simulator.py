import random # used when initializing, moving animals, and generating new animals 
class river:
    def __init__(self, river_len, fish_num, bear_num): #all parameters are int
        river = ["N" for x in range(river_len)]
        location = [x for x in range(river_len)]
        for i in range(fish_num):
            fish = random.choice(location)
            river[fish] = "F"
            location.remove(fish)
        for i in range(bear_num):
            bear = random.choice(location)
            river[bear] = "B"
            location.remove(bear)
        self.river = river
        self.river_len = river_len
        self.new_number = [0, 0] # the first: new bear; the second: new fish
        
    def move_animal(self, animal_loc): #animal_loc is int
        direction = [-1, +1]
        none_list = self.get_none()
        if animal_loc == 0:
            self.move_after_check(0,1)
        elif animal_loc == self.river_len - 1:
            self.move_after_check(animal_loc, animal_loc-1)                                    
        else:
            movement = random.choice(direction)
            self.move_after_check(animal_loc, animal_loc + movement)


    def move_after_check(self, moved, encountered): #reuse the code of judging all situations
        #pay attention to the sequence of the parameter 
        result = self.check(moved, encountered)
        if result == "go":
            self.river[moved], self.river[encountered] = self.river[encountered], self.river[moved]
            self.river[encountered] += "_new"
        elif result == "bear":
            self.new_number[0] += 1
        elif result == "fish":
            self.new_number[1] += 1
        elif result == "mbf":
            self.river[moved] = "N"
            self.river[encountered] = "B_new"
        elif result == "mfb":
            self.river[moved] = "N"


    def check(self, moved, encountered): #Two animals' locations are int
        # return go/bear/fish/the position of fish if eaten
        move_animal = self.river[moved]
        encountered_animal = self.river[encountered]
        if move_animal[0] == encountered_animal[0]:
            if move_animal[0] == "F":
                return "fish"
            else:
                return "bear"
        elif encountered_animal[0] == "N":
            return "go"
        elif encountered_animal[0] == "F":
            return "mbf" #move bear to eat fish
        elif encountered_animal[0] == "B":
            return "mfb" #move fish to be eaten by fish

    def get_none(self): #get all empty positions
        none_list = []
        for i in range(self.river_len):
            if self.river[i] == "N":
                none_list.append(i)
        return none_list

    def simulation(self, time):
        self.show_river()
        print("")
        if self.river_len > 1:
            for i in range(time):
                self.new_number = [0, 0]
                for p in range(self.river_len):
                    if self.river[p] != "N" and len(self.river[p]) == 1:
                        self.move_animal(p)
                for p in range(self.river_len):
                    if len(self.river[p]) != 1:
                        self.river[p] = self.river[p][:1]
                try:
                    for b in range(self.new_number[0]):
                        none_list = self.get_none()
                        pos = random.choice(none_list)
                        self.river[pos] = "B"

                    for f in range(self.new_number[1]):
                        none_list = self.get_none()
                        pos = random.choice(none_list)
                        self.river[pos] = "F"
                except:
                    if not ("F" in self.river and "B" in self.river):
                        print(f"The river has alreadey been filled with only one species at the {i+1}th simulation.")
                        print("Thus, the simulation stops early.")
                        break
        else:
            print("Since the river's length is 1, nothing will change.")
        self.show_river()

    def show_river(self):
        print("<", end="")
        for i in self.river:
            print(i, end="")
        print(">", end="")

def main():
    while True: # prompt the user to enter the river's length
        try:
            l = int(input("The river's length: "))
            if l > 0:
                break
            else:
                print("The river's length is a positive integer.")
                continue
        except:
            print("The river's lenth is an integer.")
            continue
    
    while True: # prompt the user to enter the number of the bear
        try:
            b = int(input("The bear's number: "))
            if b >= 0:
                if b <= l:
                    break
                else:
                    print("Too mamy bears!!")
                    continue
            else:
                print("The bear's number is a nonnegative integer.")
                continue
        except:
            print("The bear's number is an integer.")
            continue
    
    while True: # prompt the user to enter the number of the fish
        try:
            f = int(input("The fish's number: "))
            if f >= 0:
                if f <= l-b:
                    break
                else:
                    print("Too many fish!!")
                    continue
            else:
                print("The fish's number is a nonnegative integer.")
                continue
        except:
            print("The fish's number is an integer.")
            continue
    
    while True: # prompt the user to enter the simulation time
        try:
            n = int(input("Time of simulations: "))
            if n>=0:
                break
            else:
                print("The simulation time is a nonnegative integer.")
                continue
        except:
            print("The simulation time is an integer.")
            continue
    r = river(l, f, b)
    r.simulation(n)

main()
