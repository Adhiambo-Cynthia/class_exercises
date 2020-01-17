unit_cost = 100
units_bought = int(input("How many units would you like to buy? "))
total_cost= unit_cost * units_bought
if total_cost > 1000:
    money_paid = 0.9 *total_cost
    print("You have been awarded a 10% discount,your items cost:", money_paid)
else:
    print("Your items cost:", total_cost)