'''
first_name = "Brigham"

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter)
'''

'''
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")
'''

#Step 1
'''
word = "Commitment"
for letter in word:
    if letter.lower() == 'm':
        print(letter.upper())
    else:
        print(letter.lower())
'''

#Step 2
'''
word = "Commitment"
favorite_letter = input("What is your favorite letter? ")
for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
'''

#Step 3
word = "Commitment"
favorite_letter = input("What is your favorite letter? ")
for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")