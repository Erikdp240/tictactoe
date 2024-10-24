import sys
import random

# Minimax-Search function
def minimax_search(game, board):
  nodes_explored = [0]
  player = game.to_move(board)
  value, move = max_value(game, board, nodes_explored) if player == 'X' else min_value(game, board, nodes_explored)

  return move, nodes_explored[0]

def max_value(game, board, nodes_explored):
  if game.is_terminal(board):
    return game.utility(board, 'X'), None
  
  v = float('-inf')
  best_move = None
  for a in game.actions(board):
    nodes_explored[0] += 1  # Increment node count
    v2, _ = min_value(game, game.result(board, a), nodes_explored)
    if v2 > v:
      v = v2
      best_move = a

  return v, best_move

def min_value(game, board, nodes_explored):
  if game.is_terminal(board):
    return game.utility(board, 'O'), None
  
  v = float('inf')
  best_move = None
  for a in game.actions(board):
    nodes_explored[0] += 1  # Increment node count
    v2, _ = max_value(game, game.result(board, a), nodes_explored)
    if v2 < v:
      v = v2
      best_move = a

  return v, best_move
# End Minimax-Search function


# Alpha-Beta Search function
def alpha_beta_search(game, board):
  nodes_explored = [0]  # Counter passed by reference
  player = game.to_move(board)
  value, move = abmax_value(game, board, float('-inf'), float('inf'), nodes_explored) if player == 'X' else abmin_value(game, board, float('-inf'), float('inf'), nodes_explored)
  return move, nodes_explored[0]

def abmax_value(game, board, alpha, beta, nodes_explored):
  if game.is_terminal(board):
    return game.utility(board, 'X'), None
  
  v = float('-inf')
  best_move = None
  for a in game.actions(board):
    nodes_explored[0] += 1  # Increment node count
    v2, _ = abmin_value(game, game.result(board, a), alpha, beta, nodes_explored)
    if v2 > v:
      v = v2
      best_move = a

    alpha = max(alpha, v)
    
    if alpha >= beta:
      break
      
  return v, best_move

def abmin_value(game, board, alpha, beta, nodes_explored):
  if game.is_terminal(board):
    return game.utility(board, 'O'), None
  
  v = float('inf')
  best_move = None
  for a in game.actions(board):
    nodes_explored[0] += 1  # Increment node count
    v2, _ = abmax_value(game, game.result(board, a), alpha, beta, nodes_explored)
    if v2 < v:
      v = v2
      best_move = a
    beta = min(beta, v)
    if beta <= alpha:
      break
      
  return v, best_move
# End Alpha-Beta Search function

class Game:
  def to_move(self, board):
    # Returns the player whose turn it is
    return 'X' if board.count('X') == board.count('O') else 'O'

  def actions(self, board):
    # Returns available actions (empty spots)
    return available_moves(board)

  def result(self, board, move):
    if board[move - 1] != ' ':
      raise ValueError("Invalid move: Position already taken")
    new_board = board[:]
    new_board[move - 1] = self.to_move(board)
    return new_board

  def is_terminal(self, board):
    # Returns True if the game is over (win or full board)
    return self.check_winner(board) or ' ' not in board

  def utility(self, board, player):
    # Returns the utility value (1 for win, -1 for loss, 0 for draw)
    winner = self.check_winner(board)
    if winner == player:
        return 1
    elif winner:
        return -1
    return 0

  def check_winner(self, board):
    # Checks if there's a winner
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combos:
      if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
        return board[combo[0]]
    return None

def parse_args():
  if len(sys.argv) != 4:
    print("ERROR: Not enough/too many/illegal input arguments.")
    sys.exit(1)

  algo = sys.argv[1]
  first = sys.argv[2]
  mode = sys.argv[3]

  if algo not in ['1', '2']:
    print("ERROR: Not enough/too many/illegal input arguments.")
    sys.exit(1)
  if first not in ['X', 'O']:
    print("ERROR: Not enough/too many/illegal input arguments.")
    sys.exit(1)
  if mode not in ['1', '2']:
    print("ERROR: Not enough/too many/illegal input arguments.")
    sys.exit(1)

  return algo, first, mode

def display_info(a, f, m):
  last_name = "Pacheco"
  first_name = "Erik"
  iit_id = "A20459355"

  if a == '1':
    algorithm = "MiniMax"
  else:
    algorithm = "MiniMax with alpha-beta pruning"

  first_player = f

  if m == "1":
    mode = "human (X) versus computer (O)"
  else:
    mode = "computer (X) versus computer (O)"

  print(f"{last_name}, {first_name}, {iit_id} solution:")
  print(f"Algorithm: {algorithm}")
  print(f"First: {first_player}")
  print(f"Mode: {mode}")

def empty_board():
  board = [' ' for _ in range(9)]
  return board

def display_board(b):
  print(f"{b[0]} | {b[1]} | {b[2]}")
  print("--+---+--")
  print(f"{b[3]} | {b[4]} | {b[5]}")
  print("--+---+--")
  print(f"{b[6]} | {b[7]} | {b[8]}")

def available_moves(board):
  return [i+1 for i, cell in enumerate(board) if cell == ' ']

def human_move(board, player):
  moves = available_moves(board)
  while True:
      print(f"{player}'s move. What is your move (possible moves at the moment are: {moves} | enter 0 to exit the game)?")
      move = input("Enter your move: ")
      if move == '0':
          print("Exiting the game.")
          sys.exit(0)
      try:
          move = int(move)
          if move in moves:
              board[move - 1] = player  # Update the board with the player's move
              break
          else:
              print("Invalid move. Please select a valid move from the list.")
      except ValueError:
          print("Invalid input. Please enter a number.")

def computer_move(game, board, algo, player):
  if algo == '1':
      best_move, nodes_explored = minimax_search(game, board)
  else:
      best_move, nodes_explored = alpha_beta_search(game, board)

  board[best_move - 1] = player

  print(f"{player}'s selected move: {best_move}. Number of search tree nodes generated: {nodes_explored}")

  return best_move


def main():
  algo, first, mode = parse_args()

  display_info(algo, first, mode)

  board = empty_board()

  game = Game()

  display_board(board)

  if mode == '2':
    first = random.choice(['X', 'O'])

  current_player = first

  while not game.is_terminal(board):
    if mode == '1':  # Human vs Computer
      if current_player == 'X':  # Human's turn
        if first == 'X':
          human_move(board, 'X')
        else:
          computer_move(game, board, algo, 'X')
      else:  # Computer's turn
        if first == 'O':
          human_move(board, 'O')
        else:
          computer_move(game, board, algo, 'O')
    else:  # Computer vs Computer

      computer_move(game, board, algo, current_player)

    # Display the updated board after each move
    display_board(board)

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

  # Check the result
  winner = game.check_winner(board)
  if winner:
    print(f"The winner is {winner}!")
  else:
    print("The game is a draw.")


  
if __name__ == "__main__":
  main()