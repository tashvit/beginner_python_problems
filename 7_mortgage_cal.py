# Calculate the monthly payments of a fixed term mortgage over given Nth terms
# at a given interest rate.

P0 = float(input("Enter property value: $ "))
years = float(input("Enter full mortgage repayment period (years): "))
rate = float(input("Enter initial interest rate (%): "))

# Monthly mortgage payment
# Equation from https://en.wikipedia.org/wiki/Fixed-rate_mortgage
payment = ((rate/100/12) / (1 - (1 + (rate/100/12)) ** (-years*12))) * P0

print("\n")
print(f"Your monthly mortgage payment is: $ {payment:1.2f}")
print(f"Total mortgage cost including interest: $ {payment*12*30:1.2f}")
print(f"Assuming your interest rate stays at {rate}% for {years} years")