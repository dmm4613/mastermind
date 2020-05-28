from random import randint

def intro():
    print "Welcome to my game of Mastermind. Do you think you contain the genius to defeat me?"
    print "I've selected a random 4 digit number. I will provide you clues for your guess. You have 12 guesses."
    print "Red means you guessed a digit and location correctly. White means you guessed a digit correctly, but in the wrong location."
    print "Good luck"

def game_board(reds, whites, mystery_number, guesses):
    print ""
    print ""
    print "The Mystery Number is " +str(mystery_number)
    print "Red: " + str(reds)
    print "White: " + str(whites)
    print "Guesses remaining: " + str(guesses)

def play_round():    
    val = input("Guess a 4-digit number: ")
    while len(str(val)) != 4:
        val = input("No, really. 4 digits: ")
    return val

def check_guess(guess, mystery_number, reds, whites, guesses):
    if guess == mystery_number:
        reds = 4
        guesses -= 1
    else:
        reds, whites = check_positions(guess, mystery_number)
        guesses -= 1
    return reds, whites, guesses

def check_positions(guess, mystery_number):
    red = 0
    white = 0
    for key, digit in enumerate(guess):
        if digit == mystery_number[key]:
            red += 1
        else:
            for answer_digit in mystery_number:
                if answer_digit == digit:
                    white += 1
    return red, white

def mastermind():
    reds = 0
    whites = 0
    guesses = 12
    mystery_number = str(randint(1000,9999))
    intro()
    while reds != 4:
        game_board(reds, whites, mystery_number, guesses)
        guess = str(play_round())
        print guess
        reds, whites, guesses = check_guess(guess, mystery_number, reds, whites, guesses)
        if guesses == 0 & reds != 4:
            print "Sorry, you're out of guesses."
            break
    print "You won the game!"
mastermind()