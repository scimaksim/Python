# -----------------------------------------------------------------------------
# Name:        Tip
# Purpose:     Tip calculator
#
# Author:      Maksim Nikiforov
# Date:        09/129/2016
# -----------------------------------------------------------------------------
"""
Tip calculator assuming an 8.75% tip rate

Prompt the user for the cost of their meal.
Print the tip amount and the total cost.
"""

TAX_RATE = 0.0875   # regional tax rate at the time of calculation

Meal_Price_String = input("Enter the price in $: ")
Meal_Price = float(Meal_Price_String)   # convert string input to a float

Sales_Tax = Meal_Price * TAX_RATE       # calculate sales tax
Sales_Tax = round(Sales_Tax, 2)         # round the tax to 2 decimals

print("Sales Tax: $", Sales_Tax, sep='')    # suppress space separator

Total_Cost = Meal_Price + Sales_Tax     # calculate total price of meal
Total_Cost = round(Total_Cost, 2)

print("Total Cost: $", Total_Cost, sep='')






