import random, time , sys

print('''Rock Paper, Scissors, Copied by Elijah Lee
      - Rock beats Scissors.
      - Paper beats Rock.
      - Scissors beats Paper.
      ''')

#These numbers keep track of the number of wins, loses, and ties.
wins = 0
loses = 0
ties = 0

while True: #Main game loop
    while True: #keep asking until user enters R, P, S
        print('{} Wins, {} Loses, {} Ties'.format(wins, loses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing')
            sys.exit()
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R P S or Q.')

      #Display what the player chose
    if playerMove == 'R':
        print('ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'
    
    #Count to 3 with dramatic pauses
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3... and SHOOT!')

    #Get computers move
    comMove = random.randint(1,3)
    if comMove == 1:
        comMove = 'ROCK'
    elif comMove == 2:
        comMove = 'PAPER'
    elif comMove == 3:
        comMove = 'SCISSORS'

    print(comMove)
    time.sleep(0.5)

    #Find the winner
    if playerMove == comMove:
        ties = ties + 1
        print('It\'s a tie')
        #All the win conditions
    elif playerMove == 'ROCK' and comMove == 'SCISSORS':
        wins = wins + 1
        print('You WIN!!!')
    elif playerMove == 'PAPER' and comMove == 'ROCK':
        wins = wins + 1
        print('You WIN!!!')
    elif playerMove == 'SCISSORS' and comMove == 'PAPER':
        wins = wins + 1
        print('You WIN!!!')
      #All the lose conditions
    elif playerMove == 'ROCK' and comMove == 'PAPER':
        loses = loses + 1
        print('You lost better luck next time.')
    elif playerMove == 'PAPER' and comMove == 'ROCK':
        loses = loses + 1
        print('You lost better luck next time.')
    elif playerMove == 'SCISSORS' and comMove == 'ROCK':
        loses = loses + 1
        print('You lost better luck next time.')    