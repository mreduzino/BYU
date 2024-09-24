# Author: MReduzino

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
emailAddress = input("Enter your email address: ")
phoneNumber = input("Enter your phone number: ")
jobTitle = input("Enter your job title: ")
idNumber = input("Enter your ID number: ")

hairColor = input("Enter your hair color: ")
eyeColor = input("Enter your eye color: ")
startMonth = input("Enter the month you started: ")
advancedTraining = input("Have you completed advanced training? (yes/no): ")

print("----------------------------------------")
print(f"{lastName.upper()}, {firstName.capitalize()}")
print(f"{jobTitle.title()}")
print(f"ID: {idNumber}")
print()
print(f"{emailAddress.lower()}")
print(f"{phoneNumber}")
print(f"Hair: {hairColor:15} Eyes: {eyeColor}")
print(f"Month: {startMonth:14} Training: {advancedTraining}")
print("----------------------------------------")