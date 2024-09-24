#Author: MReduzino

age = int(input("How old are you? "))
print("On your next birthday, you will be " + str(age+1))

eggs_cartoons = int(input("\nHow many egg cartons do you have? "))
print("You have " + str(eggs_cartoons*12) + " eggs")

cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))
cookiesPPerson= cookies/people
print("Each person may have " + str(cookiesPPerson) + " cookies")

age = int(input("How old are you? "))

print(f"On your next birthday, you will be {age+1}." )

eggs_cartoons = int(input("\nHow many egg cartons do you have? "))
print(f"You have {eggs_cartoons*12} eggs")

cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))
cookiesPPerson = cookies/people
print(f"Each person may have {cookiesPPerson} cookies")