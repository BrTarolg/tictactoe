board = list(range(1,10))
turn = "P1"
win_combos = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
game_end = False
turn_count = 0

def print_board():
    for y in range (0,3):
        print "    ",
        for x in range (0,3):
            print (board[x + 3*y]),
        print "\n"

def reset_board():
    for x in range(0,9):
        board[x] = "-"

def get_input():
    goodinput = False
    while not goodinput:
        try:
            print "\nIt's %s's turn!" % (turn)
            print "The current state of the board:\n"
            print_board()
            place = int(raw_input("\n> pick your number "))
        except ValueError:
            print "that's not a number dude"
            continue

        if place > 9 or place < 1:
            print "That's not an option! Try again"
        elif board[place-1] != "-":
            print "That space is already taken! Try again"
        else:
            goodinput = True
            return place

def send_input():
    places = get_input()
    global turn_count
    if turn == "P1":
        board[places-1] = "O"
    else:
        board[places-1] = "X"
    turn_count += 1

def switch_turn():
    global turn
    if turn == "P1":
        turn = "P2"
    else:
        turn = "P1"

def win_condition():
    global game_end
    global turn_count
    for a, b, c in win_combos:
        if board[a-1] == board[b-1] == board[c-1] != "-":
            game_end = True
            print "Congratulations, %s wins!" % (turn)
    if turn_count == 9 and game_end == False:
        game_end = True
        print "The game is a draw!"

def start_game():
    print"""

Welcome to tic tac toe by Vincent Tam!
To select where you want to go, type in the number according to the following key
1 2 3
4 5 6
7 8 9

Player 1 goes first, and he starts with O"""
    reset_board()
    while game_end == False:
        send_input()
        win_condition()
        switch_turn()
    print "The final board state is:"

    print_board()

start_game()
