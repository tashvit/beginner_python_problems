# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of
# quarters, dimes, nickels, pennies needed for the change.

# penny: 1 cent, nickel: 5 cents, dime: 10 cents, quarter: 25 cents

cost = float(input("Enter cost: $"))
money_given = float(input("Enter amount of money given: $"))
balance = money_given - cost

print(f"The balance is ${balance:1.2f}")

dollars = int(balance)
change = round((balance - dollars) * 100)
quarters = change//25
change -= quarters * 25
dimes = change//10
change -= dimes * 10
nickels = change//5
change -= nickels * 5

print(f"{dollars:1.0f} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {change} cents")
