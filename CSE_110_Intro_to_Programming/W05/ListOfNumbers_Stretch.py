numbers = []

print("Enter a list of numbers, type 0 when finished.\n")

while True:
    new_number = int(input("Enter number: "))
    if new_number == 0:
        break
    else:
        numbers.append(new_number)
        
total = 0
average = 0
largest = float('-inf')

#total
for number in numbers:
    total += number
print(f"The sum is: {total}")

#average
average = total / (len(numbers))
print(f"The average is: {average}")

#largest
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

'''Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).'''

#SmallestPositive
smallest_positive = float('inf')
for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number
print(f"The smallest positive number is: {smallest_positive}")

#SortedList
sorted_list = sorted(numbers)

print(f"The sorted list is: ")
for number in sorted_list:
    print(number)

#######################################################################################################################
'''
# Inicializa uma lista vazia para armazenar os números
numbers = []

# Solicita números ao usuário até que 0 seja inserido
print("Enter a list of numbers, type 0 when finished.")
while True:
    num = float(input("Enter number: "))
    if num == 0:
        break
    numbers.append(num)

# Calcula a soma dos números
total = 0
for num in numbers:
    total += num

# Calcula a média dos números
if len(numbers) > 0:
    average = total / len(numbers)
else:
    average = 0

# Encontra o maior número
largest = float('-inf')  # Inicializa com o menor valor possível
for num in numbers:
    if num > largest:
        largest = num

# Encontra o menor número positivo
smallest_positive = float('inf')  # Inicializa com o maior valor possível
for num in numbers:
    if num > 0 and num < smallest_positive:
        smallest_positive = num

# Ordena a lista (usando o algoritmo de ordenação por bolha)
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Exibe os resultados
print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
if smallest_positive != float('inf'):
    print(f"The smallest positive number is: {smallest_positive}")
else:
    print("There are no positive numbers in the list.")
print("The sorted list is:")
for num in numbers:
    print(num)
'''