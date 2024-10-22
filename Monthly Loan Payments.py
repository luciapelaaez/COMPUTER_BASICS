# Define the loan details
P = 250000  # Principal loan amount in euros
annual_rate = 5 / 100  # Annual interest rate (5% expressed as a decimal)
years = 30  # Loan term in years

# Convert annual interest rate to monthly and calculate total number of months
r = annual_rate / 12  # Monthly interest rate
n = years * 12  # Total number of months

# Calculate monthly payment using the formula
M = (P * (r * (1 + r)**n)) / ((1 + r)**n - 1)

# Show the result
print(f"The monthly payment for the loan is: {M:.2f}€")