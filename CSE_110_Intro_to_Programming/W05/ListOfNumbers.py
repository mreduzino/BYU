numbers_list = []
new_number = -1

print("Enter a list of numbers, type 0 when finished.")
while True:
    new_number = int(input("Enter a number: "))
    if new_number == 0:
        break
    else:
        numbers_list.append(new_number)
        
sum = 0

for number in numbers_list:
    sum += number
print(f"\nThe sum is: {sum}")

count = (len(numbers_list))
average = sum / count
print(f"The average is: {average}")

largest = float('-inf')
for number in numbers_list:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

#Stretch Challenge

smallest_number = largest

for number in numbers_list:
    if number > 0:
        if number < smallest_number:
            smallest_number = number
            
print(f"The smallest positive number is: {smallest_number}")

sorted_list = sorted(numbers_list)

print("The sorted list is: ")
for number in sorted_list:
    print(number)