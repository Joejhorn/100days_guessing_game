import random   

def choose_difficulty():
    guess_number = 0
    while True:
        difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print('Invalid input')


def get_soultion():
    return random.randint(1,100)

def get_guess(soultion, guess_number):
    while guess_number > 0:
        try:
            print(f'You have {guess_number} attempts remaining to guess the number')
            guess = int(input('Guess: '))
            if guess == soultion:
                return('won')
            elif guess < soultion:
                print('Too low')
                guess_number -= 1
            else:
                print('Too high')
                guess_number -= 1
        except ValueError:
            print('Please enter an integer between 1 - 100')
    return 'lost'
  


def main():
    print('Welcome ot the number guessing game!')
    print('I am thinking of a number between 1 and 100')
    print('Im thinking of a number between 1 and 100')
    guesses_allowed = choose_difficulty()
    soultion = get_soultion()
    result = get_guess(soultion, guesses_allowed)
    if result == 'won':
        print(f'You got it! The answer was {soultion}')
    elif result == 'lost':
        print(f'You ran out of guesses. The answer was {soultion}')


if __name__ == '__main__':
    main()


