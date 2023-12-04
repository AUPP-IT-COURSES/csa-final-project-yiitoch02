from tkinter import *

def calculate_loan():
    # Get user input
    loan_amount = float(loan_amount_entry.get())
    interest_rate = float(interest_rate_entry.get())
    repayment_term = int(repayment_term_entry.get())

    # Calculate monthly payment
    monthly_interest_rate = interest_rate / 12 / 100
    number_of_payments = repayment_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate * pow(1 + monthly_interest_rate, number_of_payments)) / (pow(1 + monthly_interest_rate, number_of_payments) - 1)

    # Display results
    result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

# Create the main window
root = Tk()
root.title("Loan Calculator")

# Create labels and entry fields for user input
loan_amount_label = Label(root, text="Loan Amount:")
loan_amount_label.grid(row=0, column=0)
loan_amount_entry = Entry(root)
loan_amount_entry.grid(row=0, column=1)

interest_rate_label = Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0)
interest_rate_entry = Entry(root)
interest_rate_entry.grid(row=1, column=1)

repayment_term_label = Label(root, text="Repayment Term (Years):")
repayment_term_label.grid(row=2, column=0)
repayment_term_entry = Entry(root)
repayment_term_entry.grid(row=2, column=1)

# Create a button to trigger the calculation
calculate_button = Button(root, text="Calculate", command=calculate_loan)
calculate_button.grid(row=3, column=0, columnspan=2)

# Create a label to display the results
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
