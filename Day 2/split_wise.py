#Write your code below this line 👇

print("Welcome to the tip calculator!!")

bill = float(input("What was the total bill? $" ))
tip = int(input("how much tip would you like to give 10, 12, 15, 20? "))
people = int(input("How many people would like to split the bill? "))

#calcualator


tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
final_amount = round(total_bill / people, 2)

print(f"Each one should pay: $ {final_amount}" )