#Program to calculate the bill for a restaurant
print ("============================================")
print

Bill = float(input("How much is the meal ? "))
Tax = float(input("What is the sales tax (percentage)? "))
Tip = float(input("How much of a tip (percentage)? "))

Tax_amount = (Bill * Tax) / 100
Total = (Bill + Tax_amount)

Tip_amount = (Total * Tip) / 100

Total = Total + Tip_amount

Total = round(Total, 2)
print
print("The total bill is $", Total, sep = '')
