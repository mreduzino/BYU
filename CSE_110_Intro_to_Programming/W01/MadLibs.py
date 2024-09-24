#Author: MReduzino (Marcelo Henrique Reduzino)
'''
EXTRA CREDIT:
I added a part asking for a noun, an adverb and another adjective.
It also has a function that determines if the noun starts with a vowel or a consonant and returns the correct article.
'''

adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")

print("Your story is: ")
print("")
print(f"The other day, I was really in trouble. It all started when I saw a very ")
print(f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all ")
print(f"I could think to do was to {verb2} over and over. Miraculously, ")
print(f"That caused it to stop, but not before it tried to {verb3} ")
print(f"Right in front of my family.")
print("")

part2 = input("Do you want to continue the story? (y/n) ")

if part2 == "y":
    noun = input("Enter a noun: ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    
    def article(noun):
        if noun[0] in "aeiou":
            return "an"
        else:
            return "a"

    print(f"After that, I decided to take {article(noun)} {noun} and {verb1} {adverb}. It was a {adjective2} experience.")
else:
    print("The end.")