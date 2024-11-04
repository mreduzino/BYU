print("Please provide a rating from 1 to 10 for the following item:\n")
loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan >= 5:
    if (credit_history >=7 and income >= 7) or ((credit_history >=7 or income >= 7) and down_payment>= 5):
        print("yes")
    else:
        print("no")
else:
    if credit_history >= 4 and ((income >= 7 or down_payment >= 7) or (income >= 4 and down_payment >= 4)):
        print("yes")
    else:
        print("no")