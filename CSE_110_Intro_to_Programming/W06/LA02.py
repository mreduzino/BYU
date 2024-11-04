people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 999
youngest_name = ""

for person in people:
    person = person.split()
    person_name = person[0]
    person_age = int(person[1])
    
    if person_age < youngest_age:
        youngest_name = person_name
        youngest_age = person_age
print(f"The yougenst person is: {youngest_name}, which is {youngest_age} years old")