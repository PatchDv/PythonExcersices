principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal amount cannot be negative. Please try again.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    if rate < 0:
        print("Interest rate cannot be negative. Please try again.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be negative. Please try again.")
    else:
        break

compoundInterest = principal * pow((1 + rate), time)

print(f"The result is: {compoundInterest:.2f}")