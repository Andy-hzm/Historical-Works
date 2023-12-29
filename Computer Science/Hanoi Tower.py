class node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

class Stack:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def push(self, element): 
        self.head = node(element, self.head)
        self.size += 1


def switch(blist, pole1, pole2):
    copy = []
    for i in blist:
        step = i[:]
        copy.append(step)
    for i in copy:
        if i[0] == pole1:
            i[0] = pole2
        elif i[0] == pole2:
            i[0] = pole1
        
        if i[1] == pole1:
            i[1] = pole2
        elif i[1] == pole2:
            i[1] = pole1
    return copy

def HanoiTower(n):
    storage = Stack()
    for n in range(0,n):
        if n == 0:
            storage.push([["A","C"]])
        else:
            recorded_moves = storage.head.element
            process1 = switch(recorded_moves, "B", "C")
            process1.append(["A","C"])
            process2 = switch(recorded_moves, "B", "A")
            storage.push(process1 + process2)
    for step in storage.head.element:
        print(step[0], "-->", step[1])
    

def main():
    while True:
        try:
            n = int(input("The number of disks of the Hanoi tower: "))
            if n > 0:
                break
            else:
                print("The number should be greater than 0.")
                continue
        except:
            print("Please make sure that you entered an positive integer.")
            continue
    HanoiTower(n)

main()
