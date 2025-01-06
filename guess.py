import random

print('Welcome ot the number guessing game!')
print('I am thinking of a number between 1 and 100')
print('Im thinking of a number between 1 and 100')


while True:
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if difficulty == 'easy':
        guess_number = 10
        break
    elif difficulty == 'hard':
        guess_number = 5
        break
    else:
        print('Invalid input')
soultion = random.randint(1,100)

while guess_number > 0:
    try:
        print(f'You have {guess_number} attempts remaining to guess the number')
        guess = int(input('Guess: '))
        if guess == soultion:
            print(f'You got it! The answer was {soultion}')
            break
        elif guess < soultion:
            print('Too low')
            guess_number -= 1
        else:
            print('Too high')
            guess_number -= 1
    except ValueError:
        print('Please enter an integer between 1 - 100')
