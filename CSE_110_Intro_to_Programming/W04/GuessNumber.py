import random

'''
magic_number = int(input("What is the magic number? "))

guess = int(input("What is your guess? "))

while guess != magic_number:
    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    guess = int(input("What is your guess? "))
else:
    print("You guessed it!")
'''

keep_playing = "yes"

while keep_playing == "yes":
    magic_number = random.randint(1, 100)
    guess = 0
    guess_count = 0

    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count += 1
        
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")
            break
        
    print(f"You guessed the number in {guess_count} tries.")

    keep_playing = input("Do you want to play again? (yes/no) ")
    
print("Thanks for playing!")