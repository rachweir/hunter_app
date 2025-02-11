board = [['0' for i in range(8)] for j in range(2)]

def __init__():
  for i in range(1,7):
    board[0][i] = '3'
    board[1][i] = '3'
  board[0][7] = "X"
  board[1][0] = "X"
  print(board[0])
  print(board[1])

def move(player, x, y):
  if player == 1:
    if board[x][y] == "X":
      print("Invalid move")
    else:
      currently_in_x = x
      currently_in_y = y
      in_hand = int(board[x][y])
      board[x][y] = '0'
      while in_hand > 0:
        if currently_in_y == 0 and currently_in_x == 0:
          currently_in_x = 1
          currently_in_y = 0
          board[currently_in_x][currently_in_y + 1] = str(int(board[currently_in_x][currently_in_y + 1]) + 1)
          currently_in_y += 1
          in_hand -= 1
        elif currently_in_y == 6 and currently_in_x == 1:
          currently_in_x = 0
          currently_in_y = 7
          board[currently_in_x][currently_in_y - 1] = str(int(board[currently_in_x][currently_in_y - 1]) + 1)
          currently_in_y -= 1
          in_hand -= 1
        else:
          if currently_in_x == 0:
            board[currently_in_x][currently_in_y - 1] = str(int(board[currently_in_x][currently_in_y - 1]) + 1)
            currently_in_y -= 1
            in_hand -= 1
          else:
            board[currently_in_x][currently_in_y + 1] = str(int(board[currently_in_x][currently_in_y + 1]) + 1)
            currently_in_y += 1
            in_hand -= 1
      if currently_in_x == 0 and currently_in_y == 0:
        print(board[0])
        print(board[1])
        print("Which pit would you like to move?")
        pit = int(input())
        move(1, 0, pit)
  elif player == 2:
    if board[x][y] == "X":
      print("Invalid move")
    else:
      currently_in_x = x
      currently_in_y = y
      in_hand = int(board[x][y])
      board[x][y] = '0'
      while in_hand > 0:
        if currently_in_y == 1 and currently_in_x == 0:
          currently_in_x = 1
          currently_in_y = 0
          board[currently_in_x][currently_in_y + 1] = str(int(board[currently_in_x][currently_in_y + 1]) + 1)
          currently_in_y += 1
          in_hand -= 1
        elif currently_in_y == 7 and currently_in_x == 1:
          currently_in_x = 0
          currently_in_y = 7
          board[currently_in_x][currently_in_y - 1] = str(int(board[currently_in_x][currently_in_y - 1]) + 1)
          currently_in_y -= 1
          in_hand -= 1
        else:
          if currently_in_x == 1:
            board[currently_in_x][currently_in_y + 1] = str(int(board[currently_in_x][currently_in_y + 1]) + 1)
            currently_in_y += 1
            in_hand -= 1
          else:
            board[currently_in_x][currently_in_y - 1] = str(int(board[currently_in_x][currently_in_y - 1]) + 1)
            currently_in_y -= 1
            in_hand -= 1
      if currently_in_x == 1 and currently_in_y == 7:
        print(board[0])
        print(board[1])
        print("Go again! Which pit would you like to move?")
        pit = int(input())
        move(2, 1, pit)

def game_over():
  if int(board[0][0]) + int(board[1][7]) == 36:
    return True
  else:
    return False

def main():
  
  print("Welcome to the game of mancala!")
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")
  __init__()
  print(player1_name + " goes first")
  game_over()
  while game_over() == False:
    print("It is " + player1_name + "'s turn")
    print("Which pit would you like to move?")
    pit = int(input())
    move(1, 0, pit)
    print(board[0])
    print(board[1])
    if (game_over() == True):
      break
    print("It is " + player2_name + "'s turn")
    print("Which pit would you like to move?")
    pit = int(input())
    move(2, 1, pit)
    print(board[0])
    print(board[1])
    if (game_over() == True):
      break
    
  if int(board[0][0]) > int(board[1][7]):
    print(player1_name + " wins!")
  else:
    print(player2_name + " wins!")

main()
