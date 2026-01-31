import math

board = [' ']*9

def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])

def check_winner(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Main Program
while True:
    print_board()
    pos = int(input("Player X move (0-8): "))
    board[pos] = 'X'

    if check_winner('X'):
        print_board()
        print("Player X wins")
        break

    if ' ' not in board:
        print("Game Draw")
        break

    ai = best_move()
    board[ai] = 'O'

    if check_winner('O'):
        print_board()
        print("Computer wins")
        break
