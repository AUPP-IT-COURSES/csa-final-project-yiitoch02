# This program calculates the loan interest based on the principal amount, interest rate, and loan term.
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
loan_term = int(input("Enter the loan term (in years): "))

# Calculate the monthly payment
monthly_payment = principal_amount * (interest_rate * (1 + interest_rate)**loan_term) / (((1 + interest_rate)**loan_term) - 1)

# Calculate the total interest paid
total_interest_paid = monthly_payment * loan_term - principal_amount

print("Monthly Payment:", monthly_payment)
print("Total Interest Paid:", total_interest_paid)
