#Author: MReduzino
'''EXTRA CREDIT:
I asked the user if they would like to add a tip to the total price.
Used a IF statement to add the tip to the total price if the user wants to add a tip.'''

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

total_price = subtotal + sales_tax
print(f"Total: ${total_price:.2f}")

ask_tip = input("\nWould you like to add a tip? (Y/N) :")
if ask_tip == "Y" or "y":
    tip = float(input("\nHow much would you like to tip? "))
    total_price = total_price + tip
    print(f"Total: ${total_price:.2f}")
else:
    tip = 0

payment_amount = float(input("\nWhat is the payment amount? "))

change = payment_amount - total_price
print(f"Change: ${change:.2f}")