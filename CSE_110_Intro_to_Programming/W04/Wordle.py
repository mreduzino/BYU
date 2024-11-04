#Author: MReduzino
#Project: Wordle Game

# Strech: Added a list of words (people from The Book of Mormon) to the game and randomly select one of them as the secret word.

import random

word_list = ["mosiah", "nephi", "moroni", "alma", "helaman", "ether", "lehi", "jacob", "enos", "mormon"]

secret = random.choice(word_list)

initial_hint = len(secret) * "_"
guesses = 0

print("Welcome to the word guessing game!\n")
print(f"Your hint is: {initial_hint}\nA person in the Book of Mormon\n")

while True:
   guess = (input("What is your guess? ").lower())
   guesses += 1
   
   if len(guess) != len(secret):
      print(f"Sorry, the guess must have the same number of letters as the secret word.")
      continue
   
   if guess == secret:
      print("Congratulations! You guessed it!")
      print(f"It took you {guesses} guesses.")
      break
   
   hint = ""
   for i in range(len(secret)):
         if guess[i] == secret[i]:
            hint += guess[i].upper()
         elif guess[i] in secret:
            hint += guess[i].lower()
         else:
            hint += "_"

   print(f"Your hint is: {hint}")