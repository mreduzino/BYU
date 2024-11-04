numbers = []
while True:
    new_number = int(input("Enter a list of numbers, type 0 when finished. "))
    if new_number == 0:
        break
    else:
        numbers.append(new_number)

total = 0
average = 0
largest = float('-inf')

#sum
for number in numbers:
    total += number
print(f"The sum is: {total}")

#average
average = total / len(numbers)
print(f"The average is: {average}")

#largest
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")


###################################################################################################
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

# Exibe os resultados
print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
'''