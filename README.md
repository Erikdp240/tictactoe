# Documentation
## Programming Assignment 01

The main objective of this assignment: Implement MiniMax adversarial search algorithm in Python

## Problem input and command-line interface
The program accepts 3 command line argument: *python proj1.py ALGORITHM FIRST MODE*

ALGORITHM - specifies which algorithm the computer player will use
  * 1 - MiniMax
  * 2 - MiniMax with alpha-beta pruning

FIRST - specifies who begins the game
  * X
  * O

MODE - specifies the mode in which your program should operate
  * 1 - Human (X) vs. Computer (O)
  * 2 - Computer (X) vs. Computer (O)

If the number of arguments provided is NOT three or arguments are invalid the program displays an error message and exits.

## Program details
The Tic-Tac-Toe game board is represented by 3x3 grid with cells numbered [1, 2, 3, 4, 5, 6, 7, 8, 9]

When it is the computer's turn (regardless of the game mode), the program displays the move selected by computer and the number of search tree nodes generated.

When the game is complete, the following is displayed:
 * X won or O won
 * TIE
 * X LOST or O LOST
