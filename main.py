from random import randint

def generate_answer():
    return str(randint(1000,9999))

def check_input(guess):
    """
    With a given input, will first check if the input is the correct length.
    If the correct length is provided, the input will be checked for the correct typing by checking each digit compared to the acceptable input choices.
    """
    if len(guess) != 4:
        return True
    acceptable_input = ['0','1','2','3','4','5','6','7','8','9']
    for digit in guess:
        if digit not in acceptable_input:
            return True
    return False

def did_you_win(guess, answer, guesses):
    reds, whites = 0, 0
    whites_list = []
    remaining_answer = []
    if guesses == 0:
        print "Sorry, you lost. The answer was: " + answer
        return True
    if guess == answer:
        print "You figured it out!"
        return True
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            whites_list.append(digit)
            remaining_answer.append(answer[key])
    for digit in whites_list:
        if digit in remaining_answer:
            whites += 1        
    display_gameboard(reds,whites,guesses)
    return False

def guess_answer():
    guess = raw_input("please give a 4-digit number between: ")
    while check_input(guess):
        guess = raw_input("Really, give me a 4-digit number: ")
    return guess

def display_gameboard(reds,whites,guesses):
    print ""
    if guesses == 1:
        print "You only have 1 more guess!"
    else: 
        print "You have " + str(guesses) + " guesses remaining."
    print "Reds: " + str(reds) + " | Whites: " + str(whites)
    print ""

answer = generate_answer()
guesses = 11
guess = guess_answer()
while did_you_win(guess,answer,guesses) == False:
    guesses -= 1
    guess = guess_answer()




    

