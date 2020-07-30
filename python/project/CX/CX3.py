import random,easygui
secret = random.randint(1,100)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret! 
It is a number from 1 to 100. I'll give you 7 tries.""")
while guess != secret and tries < 7:
    guess = easygui.integerbox("What's your guess,matey?")
    if not guess: break
    if guess < secret: 
        easygui.msgbox(str(guess) + "Too low!")
    elif guess > secret:
        easygui.msgbox(str(guess) + "Too high!") 
    tries = tries + 1
if guess == secret:
    easygui.msgbox("You are very clever!") 
else:
    easygui.msgbox("No more guesses! You are a stupid pig! The secret number was" + str(secret))