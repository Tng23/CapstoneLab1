import random

hangman_board = ['''

 /----\\
     |
     |
     |
     |
     |
-------------''', '''
 /----\\
 o   |
     |
     |
     |
     |
-------------''', '''
 /----\\
 o   |
 |   |
     |
     |
     |
-------------''', '''
 /----\\
 o   |
\|   |
     |
     |
     |
-------------''', '''
 /----\\
 o   |
\|/  |
 |   |
     |
     |
-------------''', '''
 /----\\
 o
\|/  |
 |   |
/    |
     |
-------------''', '''
 /----\\
 o   |
\|/  |
 |   |
/ \  |
     |
-------------''']


#word list for subjects
wordlist = 'timberwolves football basketball soccer vikings twins packers hockey'.upper().split()
random.shuffle(wordlist)
wordlist2 = 'minnesota california illinois wisconsin texas florida mississippi oklahoma'.upper().split()
random.shuffle(wordlist2)
wordlist3 = 'china canada germany japan thailand mexico taiwan madagascar indonesia mayalsia'.upper().split()
random.shuffle(wordlist3)

#prompting user for subject
print("\n LET'S PLAY HANGMAN! \n")
subject_choice = int(input("Select a subject:\n 1. Sports \n 2. States \n 3. Countries\n ---------------------------"))

if subject_choice == 1:
    secret_word = wordlist.pop()
elif subject_choice == 2:
    secret_word = wordlist2.pop()
elif subject_choice == 3:
    secret_word = wordlist3.pop()

correct = []
incorrect = []
#function for drawing the hangman board
def draw_board():
    #draws the lines and displays the words
    print(hangman_board[len(incorrect)])
    for i in secret_word:
        if i in correct:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print("\n\n")
    print("*** Missed Letters ***")
    for i in incorrect:
        print(i, end=" ")
    print("\n*************************")

#function for the user's guesses and error checking
def user_guess():
        #Allow user to take a guess. Appends the letter to correct or incorrect word
    while True:
        guess = input("Guess a letter:\n").upper()
        if guess in correct or guess in incorrect:
            print("You have already guessed that letter. Guess again.")
        elif guess.isnumeric():
            print("Please enter letters only, not numbers. Guess again.")
        elif len(guess) > 1:
            print("Please enter only 1 letter at a time. Guess again.")
        elif len(guess) == 0:
            print("please guess a letter.")
        else:
            break
    if guess in secret_word:
        correct.append(guess)
    else:
        incorrect.append(guess)

#check to see if user won or loss
def check_win():
    if len(incorrect) > 5:
        return 'loss'
    for i in secret_word:
        if i not in correct:
            return 'no win'
    return 'win'

#combining functions for the game to run
gameIsDone = False
while True:
    draw_board()
    user_guess()
    win_condition = check_win()
    if win_condition == 'loss':
        print("GAME OVER. The word was *** %s ***" % secret_word)
        print(hangman_board[6])
        break
    elif win_condition == 'win':
        print("YOU WIN! The word was *** %s ***" % secret_word)
        break
