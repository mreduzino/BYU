shopping_list = []
item = ""

new_item = input("Please enter the items of the shopping list (type: quit to finish): ")

while new_item.lower() != "quit":
    shopping_list.append(new_item)
    new_item = input("Please enter the items of the shopping list (type: quit to finish): ")
    
print("\nYour shopping list is:")

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(item)
    
print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")
    
index = int(input("\nWhich item you would like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")