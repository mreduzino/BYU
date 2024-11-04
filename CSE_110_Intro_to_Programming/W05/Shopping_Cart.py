# Author: MReduzino
# Extra Points: Implemented a "Finalize purchase" option that calculates change,
#               clears the cart after successful payment, and ends the program.

shopping_cart = []
item_prices = []

while True:
    print("\nWelcome to the Shopping Cart Program!")
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    print("6. Finalize purchase\n")
    
    choice = input("\nPlease enter an action: ")
    
    if choice == '1':
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        item_price = float(input(f"What is the price of '{item}'? "))
        item_prices.append(item_price)
        print(f"'{item}' has been added to the cart.")
    
    elif choice == '2':
        if shopping_cart:
            print("The contents of the shopping cart are:")
            for i in range(len(shopping_cart)):
                print(f"{i + 1}. {shopping_cart[i]} - ${item_prices[i]:.2f}")
        else:
            print("The shopping cart is empty.")
    elif choice == '3':
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            print(f"{i + 1}. {shopping_cart[i]} - ${item_prices[i]:.2f}")
            
        item_index = int(input("Which item would you like to remove? ")) - 1
            
        if 0 <= item_index < len(shopping_cart):
            removed_item = shopping_cart.pop(item_index)
            removed_price = item_prices.pop(item_index)
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("Sorry, that is not a valid item number.")
    elif choice == '4':
        total = 0
        for item_price in item_prices:
            total += item_price
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    elif choice == '5':
        print("Thank you. Goodbye.")
        break
    elif choice == '6':
        if len(shopping_cart) == 0:
            print("The shopping cart is empty. Cannot finalize purchase.")
        else:
            total = sum(item_prices)
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
            
            while True:
                payment = float(input("Enter the amount received: $"))
                if payment >= total:
                    change = payment - total
                    print(f"Change: ${change:.2f}")
                    print("Thank you. Goodbye.")
                    shopping_cart.clear()
                    item_prices.clear()
                    break
                else:
                    print(f"Insufficient payment. The total is ${total:.2f}")
        break
    else:
        print("Invalid choice. Please try again")