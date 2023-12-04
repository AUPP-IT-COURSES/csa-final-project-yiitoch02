from tkinter import *

def switch_to_loan_calculator():
    root.destroy()

def switch_to_loan_comparison():
    root.destroy()

# Initialize the Tkinter window
root = Tk()
root.title("Loan Comparison Calculator")
root.geometry("500x300")

# Create labels and headings for the home page
heading_label = Label(root, text="Loan Comparison Calculator", font=("Arial", 24))
heading_label.pack(pady=20)

description_label = Label(root, text="This web application allows you to calculate and compare loan information for different loan options. You can calculate the monthly payment, total interest paid, and amortization schedule for a single loan. You can also compare two loans side-by-side to see which one is the better option for you.", font=("Arial", 12))
description_label.pack()

button_frame = Frame(root)
button_frame.pack()

loan_calculator_button = Button(button_frame, text="Loan Calculator", command=switch_to_loan_calculator)
loan_calculator_button.pack(pady=10)

loan_comparison_button = Button(button_frame, text="Loan Comparison", command=switch_to_loan_comparison)
loan_comparison_button.pack(pady=10)

# Start the main event loop
root.mainloop()
