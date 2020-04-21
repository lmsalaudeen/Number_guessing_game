import random

game_instructions = ('There are three levels in this game: Easy(E), Medium (M) and Hard(H)')
print(game_instructions)

set_level = input('Which level would you like to play? (Enter E for easy, M for medium and H for hard) ').lower()

start = True
# Easy
while start:
    if set_level == "e":
        print('The number is between 1-10. You have six(6) guesses')
        secret_number = random.randint(1, 10)
        # print(secret_number)   # for program test
        guess_limit = 6
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break


    # Medium
    elif set_level == "m".lower():
        print('The number is between 1-20. You have four (4) guesses')
        secret_number = random.randint(1, 20)
        # print(secret_number)  # For program test
        guess_limit = 4
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break


    # Hard
    elif set_level == "h".lower():
        print('The number is between 1-50. You have three (3) guesses')
        secret_number = random.randint(1, 50)
        # print(secret_number)  # for program test
        guess_limit = 3
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break

    else:
        print('Invalid input! (Enter E for easy, M for medium and H for hard)')
        set_level = input(
            'Which level would you like to play? (Enter E for easy, M for medium and H for hard) ').lower()
        start = True


