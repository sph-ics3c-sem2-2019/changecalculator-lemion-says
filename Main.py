#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("How much does the item cost?"))
amount=float(input("How much did you pay?"))
change=amount-cost
print("Your change is", change)
#how many 100s
num100=change//100
print(num100,"x $100")
change=change%100
#how many 50s
num50=change//50
print(num50,"x $50")
change=change%50
#how many 20s
