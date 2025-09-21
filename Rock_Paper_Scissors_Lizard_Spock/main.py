import random 

computer = random.randint(1,5)

options = ['✊', '✋', '✌️', '🦎', '🖖']

print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================\n')

for i in range(5):
    print(f'{i + 1}) ' + options[i])

player = int(input('Pick a number: '))

print('\nYou chose :' + options[player - 1])
print('CPU chose :' + options[computer - 1])

if computer == player:
    print("It's a tie!")
elif (computer == 5 and (player == 3 or player == 1)) \
    or (computer == 2 and (player == 5 or player == 1)) \
    or (computer == 4 and (player == 5 or player == 2)) \
    or (computer == 3 and (player == 4 or player == 2)) \
    or (computer == 1 and (player == 4 or player == 3)):
    print('The CPU won!')
else:
    print('The player won!')

# Spock smashes Scissors.
# Spock vaporizes Rock.
# Paper covers Rock.
# Paper disproves Spock.
# Lizard poisons Spock.
# Lizard eats Paper.
# Scissors cut Paper.
# Scissors beat Lizard.
# Rock crushes Lizard.
# Rock breaks Scissors.