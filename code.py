def game_board(board):
	print('\n'*100)
	print('    |     |')
	print('  '+board[7]+' ' + '|' + '  '+board[8]  + '  |' +' '+ board[9])
	print('---------------')
	print('    |     |')
	print('  '+board[4]+' ' + '|' + '  '+board[5]  + '  |'+' ' + board[6])
	print('    |     |')
	print('---------------')
	print('  '+board[1]+' ' + '|' + '  '+board[2]  + '  |'+' ' + board[3])
	print('    |     |')

'test_board=['#','X','O','X','O','X','O','X','O','X']'
#game_board(test_board)

def player_input():
	marker=''
	while not(marker=='X' or marker=='O'):
		marker=input('Player 1, choose X or O: ').upper()

	if marker=='X':
		return('X','O')
	else:
		return('O','X')
	
#player_input()
def place_marker(board,marker,position):
	board[position]=marker

#place_marker(test_board,'$',8)
#game_board(test_board)

def check_win(board,mark):
	return ((board[1]==mark and board[2]==mark and board[3]==mark)or
			(board[4]==mark and board[5]==mark and board[6]==mark)or
			(board[7]==mark and board[8]==mark and board[9]==mark)or
			(board[1]==mark and board[5]==mark and board[9]==mark)or
			(board[3]==mark and board[5]==mark and board[7]==mark)or
			(board[1]==mark and board[4]==mark and board[7]==mark)or
			(board[2]==mark and board[5]==mark and board[8]==mark)or
			(board[3]==mark and board[6]==mark and board[9]==mark))

#check_win(test_board,'X')

import random
def toss():
	if random.randint(0,1)==0:
		return 'Player 2'
	else:
		return 'Player 1'


def space_check(board,position):
	return board[position]==' '


def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	position=0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position=int(input('Choose next position (1-9): '))

	return position

def replay():
	option=''
	while not option=='yes' or not option=='no':
	    option=input('Replay? Yes or No: ').lower()
	    if option=='yes':
	        return option
	    elif option=='no':
	        print('Thanks for playing')
	        break
	    else:
	        print('Invalid option')
	        continue
	    
	


print("**********Let's Play Tic Toc**********")
while True:
	the_Board=[' ']*10
	player1_marker,player2_marker=player_input()
	turn=toss()
	print(turn+' will go first.')
	play_game=''
	while not play_game=='yes' or not play_game=='no':
		play_game=input('Ready to play? Yes or No: ').lower()
		if play_game.lower()=='yes':
			game_start=True
			break
		elif play_game.lower()=='no':
			game_start=False
			break
		else:
			print('Incorrect option')
			continue
		  
	while game_start:
		if turn=='Player 1':
			game_board(the_Board)
			position=player_choice(the_Board)
			place_marker(the_Board,player1_marker,position)

			if check_win(the_Board,player1_marker):
				game_board(the_Board)
				print('Player 1 wins')
				game_start=False
			else:
				if full_board_check(the_Board):
					game_board(the_Board)
					print('Draw Match')
					break
				else:
					turn='Player 2'

		else:
			game_board(the_Board)
			position=player_choice(the_Board)
			place_marker(the_Board,player2_marker,position)

			if check_win(the_Board,player2_marker):
				game_board(the_Board)
				print('Player 2 wins')
				game_start=False
			else:
				if full_board_check(the_Board):
					game_board(the_Board)
					print('Draw Match')
					break
				else:
					turn='Player 1'
	
	if not replay():
		break
