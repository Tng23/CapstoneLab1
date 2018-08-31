import random

number = random.randint(1,10);
print('can you guess the number between 1-10?')

for numberOfGuesses in range(1,6):
    print('Guess the number.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('You are correct!')
        break
