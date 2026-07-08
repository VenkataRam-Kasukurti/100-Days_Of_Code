
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10,12, or 15? ")
bill_split = input("how many people to split the bill? ")

total_tip = int(tip) / 100

amount = (float(total_bill) * (1+float(total_tip))) / float(bill_split)

final_amount = round(amount, 2)

print(f"Each person should pay: {final_amount}")
