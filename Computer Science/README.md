# Computer Science
This repository stores some coding exercises, currently all from my school assignments.
## 1. Polynomial Derivative
**Key Techniques:** *OOP, Python*  
Allows the user to enter a polynomial in standard form as a string and derive its derivative.
## 2. Ecosystem Simulator
**Key Techniques:** *OOP, Python*  
Imitate an ecosystem of fish and bear.

In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
## 3. Hanoi Tower Solution
**Key Techniques:** *OOP, Stack, Python*  
Simulates the tower of Hanoi, a mathematical game or puzzle.

There are three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire stack to
another rod, obeying the following simple rules: 

  1. Only one disk can be moved at a time.
  2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
  3. No disk may be placed on top of a smaller disk.
     
Assume that initially all the disks are placed on rod A. This program asked the user for the preferred initial number of disks. It prints out the needed steps to shift all the disks to rod C via rod B.
## 4. Klotski Sliding Puzzle
**Key Techniques:** *Function Definition, Python*   
An interactive game.

This game generates a disordered number table in dimensions up to 10x10. The minimum dimension is 3x3. The gaming board has an empty space where an adjacent number can be slid to. The objective of this game is to rearrange the numbers into a sequential order (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down).
## 5. Greedy Snake
**Key Techniques:** *User Interface, Python*   
A special snake game. 

The user will use 4 arrow keys to control the snake’s movement, in order to consume all the food items generated randomly on the board (represented by numbers from 1 to 9) and avoid head-on collision with the monster (represented by a purple square). When the snake eats all the “food” on the board and is not caught by the monster, the user wins the game. Oppositely, when the monster catches the snake, the user loses the game. Also, as soon as the user clicks anywhere on the screen to start the game, the status area on the board will show the current gaming time and the snake’smotion, including “Up”, “Right”, “Down”, “Left”, and “Paused” (the user can use a space bar to pause or un-pause the snake’s movement). The area also counts the contact time of the monster and the snake’s body.
## 6. Two Sum
**Key Techniques:** *Quick Sort, Binary Search, Java*  
Given an array of n integers and an integer t, find the indices of the two elements such that they
add up to t.
## 7. Inversion Number
**Key Techniques:** *merge sort, Java*  
Count the number of inversions of an array
## 8. Symmetric Binary Tree
**Key Techniques:** *Recursion, BFS*    
Finds the biggest symmetric subtree in a binary tree.
## 9. Wandering
**Key Techniques:** *Dijkstra*
Finds the second shortest path from node 1 to node n in a bidirectional graph.  

The program first uses traditional Dijkstra to find the shortest distance to node 1 for every node and stores them in an array. Then, the algorithm uses basically the same way of Dijkstra to iterate over the graph but when update the second shortest distance based on the first Dijkstra's results
## 10. Pandemic
**Key Techniques:** *Prim Algorithm*  
Build a minimum spinning tree to cover all the nodes in a two-dimensional space.








