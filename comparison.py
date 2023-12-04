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
    result_label = Label(calculation_frame, text=f"Monthly Payment: ${monthly_payment:.2f}")
    result_label.grid(row=4, column=0, columnspan=2)

def switch_to_loan_calculator():
    calculation_frame.pack()

def switch_back_to_home():
    calculation_frame.pack_forget()

# Initialize the Tkinter window
root = Tk()
root.title("Loan Comparison Calculator")
root.geometry("500x400")

# Create labels and headings for the home page
heading_label = Label(root, text="Loan Comparison Calculator", font=("Arial", 24))
heading_label.pack(pady=20)

description_label = Label(root, text="This web application allows you to calculate and compare loan information for different loan options. You can calculate the monthly payment, total interest paid, and amortization schedule for a single loan.", font=("Arial", 12))
description_label.pack()

button_frame = Frame(root)
button_frame.pack()

loan_calculator_button = Button(button_frame, text="Loan Calculator", command=switch_to_loan_calculator)
loan_calculator_button.pack(pady=10)

# Create a frame for loan calculation input and results
calculation_frame = Frame(root)
calculation_frame.pack_forget()

loan_amount_label = Label(calculation_frame, text="Loan Amount:")
loan_amount_label.grid(row=0, column=0)
loan_amount_entry = Entry(calculation_frame)
loan_amount_entry.grid(row=0, column=1)

interest_rate_label = Label(calculation_frame, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0)
interest_rate_entry = Entry(calculation_frame)
interest_rate_entry.grid(row=1, column=1)

repayment_term_label = Label(calculation_frame, text="Repayment Term (Years):")
repayment_term_label.grid(row=2, column=0)
repayment_term_entry = Entry(calculation_frame)
repayment_term_entry.grid(row=2, column=1)

calculate_button = Button(calculation_frame, text="Calculate", command=calculate_loan)
calculate_button.grid(row=3, column=0, columnspan=2)
