#Rock Paper Scissors
command = input('Do you have a partner and both want play a game of Rock Paper Scissors? Y/N ')
while command == 'Y':
    if command == 'N':
        break
    move1 = input('Player 1: rock, paper, or scissors? ')
    move2 = input('Player 2: rock, paper, or scissors? ')
    if move1 == 'rock' and move2 == 'rock':
        print('Tie!')
    elif move1 == 'rock' and move2 == 'paper':
        print('Player 2 wins!')
    elif move1 == 'rock' and move2 == 'scissors':
        print('Player 1 wins!')
    elif move1 == 'paper' and move2 == 'paper':
        print('Tie!')
    elif move1 == 'paper' and move2 == 'scissors':
        print('Player 2 wins!')
    elif move1 == 'scissors' and move2 == 'scissors':
        print('Tie!')
    else:
        print('I didn\'t understand you, try again!')
    newGame = input('Do you want to play another game? Y/N ')
    if newGame == 'Y':
        command == 'Y'
    else:
        break