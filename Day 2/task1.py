print("Welcome to the tip Calculator!")

cuenta = float(input("What was the total bill? $"))

propina = int(input("What percentage tip would you like to give 10, 12 or 15? "))

personas = int(input("How many people to split the bill? "))

tip_as_percent = propina / 100
total_tip_amount = cuenta * tip_as_percent
total_bill = cuenta + total_tip_amount
bill_per_person = total_bill / personas
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")