'''
number = 0

while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")
'''

'''
number = 1
while number <=5:
    print(f"The number is: {number}")
    number += 1
print("Finished with the loop")
'''

'''
positive_number = int(input("Please type a positive number: "))

while positive_number < 0:
    print("Sorry, that is a negative number, please try again.")
    positive_number = int(input("Please type a positive number: "))
    
print(f"The number is: {positive_number}")
'''

candy = "no"

while candy != "yes":
    candy = input("May I have a piece of candy? ")
print("Thank you!")