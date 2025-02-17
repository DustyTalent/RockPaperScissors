import random, time , sys

print('''Rock, Paper, Scissors, Lizard, Spock, Copied by Elijah Lee
      - Scissors cuts Paper
      - Paper covers Rock
      - Rock crushes Lizard
      - Lizard poisons Spock
      - Spock smashes Scissors
      - Scissors decapitates Lizard
      - Lizard eats Paper
      - Paper disproves Spock
      - Spock vaporizes Rock
      - And as it always has ben Rock crushes Scissors
      ''')

#These numbers keep track of the number of wins, loses, and ties.
wins = 0
loses = 0
ties = 0

while True: #Main game loop
    while True: #keep asking until user enters R, P, S
        print('{} Wins, {} Loses, {} Ties'.format(wins, loses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors (L)izard Sp(O)ck or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing')
            sys.exit()
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' or playerMove == 'L' or playerMove == 'O':
            break
        else:
            print('Type one of R, P, S, L, O, or Q.')

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
    elif playerMove == 'L':
        print('LIZARD versus...')
        playerMove = 'LIZARD'
    elif playerMove == 'O':
        print('SPOCK versus...')
        playerMove = 'SPOCK'
    
    #Count to 3 with dramatic pauses
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3... and SHOOT!')

    #Get computers move
    comMove = random.randint(1,5)
    if comMove == 1:
        comMove = 'ROCK'
    elif comMove == 2:
        comMove = 'PAPER'
    elif comMove == 3:
        comMove = 'SCISSORS'
    elif comMove == 4:
        comMove = 'LIZARD'
    elif comMove == 5:
        comMove = 'SPOCK'

    print(comMove)
    time.sleep(0.5)

    #Find the winner
    if playerMove == comMove:
        ties = ties + 1
        print('It\'s a tie')
        #All the win conditions (Chat-GPT version)
    elif (playerMove == 'ROCK' and comMove == 'SCISSORS') or \
         (playerMove == 'ROCK' and comMove == 'LIZARD') or \
         (playerMove == 'PAPER' and comMove == 'ROCK') or \
         (playerMove == 'PAPER' and comMove == 'SPOCK') or \
         (playerMove == 'SCISSORS' and comMove == 'PAPER') or \
         (playerMove == 'SCISSORS' and comMove == 'LIZARD') or \
         (playerMove == 'LIZARD' and comMove == 'SPOCK') or \
         (playerMove == 'LIZARD' and comMove == 'PAPER') or \
         (playerMove == 'SPOCK' and comMove == 'SCISSORS') or \
         (playerMove == 'SPOCK' and comMove == 'ROCK'):
             wins += 1
             print('You won, wouldn\'t be able to keep track in real life')
           
        
      #All the lose conditions
    else:
        lose += 1
        print('Better luck next time nerd!')
