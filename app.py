from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='templates')

# Index page
@app.route("/")
def index():
    return render_template("index.html")

# Loan calculator page
@app.route("/loan-calculator")
def loan_calculator():
    return render_template("loan-calculator.html")

# Loan comparison page
@app.route("/loan-comparison")
def loan_comparison():
    return render_template("loan-comparison.html")

# Process loan calculation request
@app.route("/calculate-loan", methods=["POST"])
def calculate_loan():
    # Extract loan parameters from the form
    loan_amount = float(request.form["loanAmount"])
    interest_rate = float(request.form["interestRate"])
    repayment_term = float(request.form["repaymentTerm"])
    loan_type = request.form["loanType"]

    # Calculate monthly payments
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, repayment_term, loan_type)

    # Calculate total interest paid
    total_interest_paid = calculate_total_interest_paid(loan_amount, monthly_payment, repayment_term)

    # Calculate amortization schedule
    amortization_schedule = calculate_amortization_schedule(loan_amount, monthly_payment, repayment_term)

    # Prepare results for display
    loan_summary = {
        "loanAmount": loan_amount,
        "interestRate": interest_rate,
        "repaymentTerm": repayment_term,
        "loanType": loan_type,
        "monthlyPayment": monthly_payment,
        "totalInterestPaid": total_interest_paid
    }

    # Serialize amortization schedule data
    amortization_data = []
    for month, principal_paid, interest_paid, remaining_balance in amortization_schedule:
        amortization_data.append({
            "month": month,
            "principalPaid": principal_paid,
            "interestPaid": interest_paid,
            "remainingBalance": remaining_balance
        })

    # Render results template with calculated values and amortization data
    return render_template("loan-calculator-results.html", loan_summary=loan_summary, amortization_data=amortization_data)

# Calculate monthly payment based on loan parameters
def calculate_monthly_payment(loan_amount, interest_rate, repayment_term, loan_type):
    # Convert interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12 / 100

    # Calculate number of payments
    number_of_payments = repayment_term * 12

    # Calculate monthly payment using loan formula
    monthly_payment = (loan_amount * monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)) / (math.pow(1 + monthly_interest_rate, number_of_payments) - 1)

    return monthly_payment

# Calculate total interest paid over the loan term
def calculate_total_interest_paid(loan_amount, monthly_payment, repayment_term):
    # Calculate total payments
    total_payments = monthly_payment * repayment_term * 12

    # Calculate total interest paid
    total_interest_paid = total_payments - loan_amount

    return total_interest_paid

# Generate amortization schedule for the loan
def calculate_amortization_schedule(loan_amount, monthly_payment, repayment_term):
    def calculate_amortization_schedule(loan_amount, monthly_payment, repayment_term, interest_rate):
        remaining_balance = loan_amount
        amortization_schedule = []

        for month in range(1, int(repayment_term * 12) + 1):
            # Calculate interest paid for the month
            interest_paid = remaining_balance * (interest_rate / 12 / 100)

            # Calculate principal paid for the month
            principal_paid = monthly_payment - interest_paid

            # Update remaining balance
            remaining_balance -= principal_paid

            # Append the month's data to the amortization schedule
            amortization_schedule.append((month, principal_paid, interest_paid, remaining_balance))

        return amortization_schedule

    def calculate_amortization_schedule(loan_amount, monthly_payment, repayment_term, interest_rate):
        remaining_balance = loan_amount
        amortization_schedule = []

        for month in range(1, int(repayment_term * 12) + 1):
            # Calculate interest paid for the month
            interest_paid = remaining_balance * (interest_rate / 12 / 100)

            # Calculate principal paid for the month
            principal_paid = monthly_payment - interest_paid

            # Update remaining balance
            remaining_balance -= principal_paid

            # Append the month's data to the amortization schedule
            amortization_schedule.append((month, principal_paid, interest_paid, remaining_balance))

        return amortization_schedule

    if __name__ == "__main__":
        app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
