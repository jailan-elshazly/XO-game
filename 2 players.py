#DISPLAY BOARD
def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#TAKE PLAYER INPUT
def player_marker(name):
    value = 'dummy'
    acceptable_value = ['X','O']

    while value not in acceptable_value:
        value = input('{} do you want to be X or O? : '.format(name)).upper()

        if value not in acceptable_value:
            print('Please select either X or O')
        else:
            return value


def get_position():
    index = 'dummy'
    acceptable_value = [x for x in range(1,10)]

    while index not in acceptable_value:
        index = input('Enter the position at which you want to put your marker : ')

        if index.isalpha():
            print('It must be a number between 1 to 9')
        elif int(index) not in acceptable_value:
            print('Please enter valid position i.e. 1 to 9')
        else:
            return int(index)


def player_turn(board, position, player):
    board[position-1] = player
    return board

#my_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def winner(board):
    winner_player = 'dummy'
    acceptable_value = ['X','O']

    if board[0] == board[1] ==board[2]:
        winner_player = board[0]
    elif board[3] == board[4] ==board[5]:
        winner_player = board[3]
    elif board[6] == board[7] ==board[8]:
        winner_player = board[6]
    elif board[0] == board[3] ==board[6]:
        winner_player = board[0]
    elif board[1] == board[4] ==board[7]:
        winner_player = board[1]
    elif board[2] == board[5] ==board[8]:
        winner_player = board[2]
    elif board[0] == board[4] ==board[8]:
        winner_player = board[0]
    elif board[2] == board[4] ==board[6]:
        winner_player = board[2]

    if winner_player in acceptable_value:
        return winner_player
    else:
        return 'dummy'

my_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

player1 = input('Enter player 1 name : ')
player2 = input('Enter player 2 name : ')

player1_marker = player_marker(player1)

if(player1_marker == 'X'):
    print('{} your marker is \'O\''.format(player2))
    player2_marker = 'O'
else:
    print('{} your marker is \'X\''.format(player2))
    player2_marker = 'X'

start = input('Let\'s get started\n press any key and then enter to start')
if start:
    print('\n'*100)

display_board(my_list)
accepted_winners = [player1_marker,player2_marker]
win = 'dummy'
count = 1

while win not in accepted_winners:
    index = get_position()
    if count%2 == 0:
        my_list = player_turn(my_list,index,player2_marker)
    else:
        my_list = player_turn(my_list,index,player1_marker)

    print('\n' * 100)
    display_board(my_list)
    win = winner(my_list)
    print(win)
    if count < 9 and win in accepted_winners:
        if win == player1_marker:
            print('Congratulations {} you won!!'.format(player1.upper()))
            exit(0)
        else:
            print('Congratulations {} you won!!'.format(player2.upper()))
            exit(0)
    elif count == 9 and win not in accepted_winners:
        print('It\'s a draw!!')
        exit(0)
    else:
        count+=1
