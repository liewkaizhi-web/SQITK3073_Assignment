import functions

FILENAME = 'ASSIGNMENT/INDIVIDUAL/user_data.csv'
print("=== Malaysian Tax Input Program ===\n")


has_account = input("Do you have an account? (Y/N): ").upper()
if has_account == 'N':
    ic_number = input("Enter your IC number (12 digits): ")
    while len(ic_number) != 12 or not ic_number.isdigit():
        ic_number = input("IC number must be 12 digits. Please try again: ")
    password = input("Set your password (last 4 digits of IC): ")
    while password != ic_number[-4:]:
        password = input("Password must match the last 4 digits of IC: ")
    print("Registration successful! Please log in to continue.\n")


logged_in = False
while not logged_in:
    ic_number = input("Enter your IC number (12 digits): ")
    password = input("Enter your password (last 4 digits of IC): ")
    if functions.verify_user(ic_number, password):
        print("Login successful!\n")
        logged_in = True
    else:
        print("IC or password is incorrect. Please try again.\n")


while True:
    try:
        income = float(input("Enter your annual income (RM): "))
        if income < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number.")


print("\n--- Tax Relief Information ---")
print("Tax relief helps reduce your taxable income based on your personal situation.")
print("1. RM9000 for self (basic individual relief).")
print("2. RM4000 for spouse (if spouse income < RM4000).")
print("3. RM2000 per child.")
print("4. Up to RM8000 for medical expenses.")
print("5. Up to RM2500 for lifestyle expenses.")
print("6. Up to RM7000 for education fees.")
print("7. Up to RM5000 for parental care.")


print("\n--- Please enter information for tax relief calculation ---")
while True:
    try:
        spouse_income = float(input("Spouse income (RM, enter 0 if no income): "))
        num_children = int(input("Number of children: "))
        medical_expenses = float(input("Medical expenses (RM): "))
        lifestyle_expenses = float(input("Lifestyle expenses (RM): "))
        education_fees = float(input("Education fees (RM): "))
        parental_care = float(input("Parental care expenses (RM): "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.")


relief_details = functions.calculate_tax_relief(
    spouse_income, num_children, medical_expenses,
    lifestyle_expenses, education_fees, parental_care
)
tax_relief = relief_details["total_relief"]


print("\n================ TAX RELIEF BREAKDOWN ================\n")
print(f"Individual Relief (Fixed): RM {relief_details['self_relief']}")
print(f"Spouse Relief: RM {relief_details['spouse_relief']}")
print(f"Children Relief: RM {relief_details['children_relief']}")
print(f"Medical Relief: RM {relief_details['medical_relief']}")
print(f"Lifestyle Relief: RM {relief_details['lifestyle_relief']}")
print(f"Education Fees Relief: RM {relief_details['education_relief']}")
print(f"Parental Care Relief: RM {relief_details['parental_relief']}")
print("------------------------------------------------------")
print(f"Total Tax Relief: RM {relief_details['total_relief']}")
print("======================================================\n")


taxable_income = max(0, income - tax_relief)
tax_payable = functions.calculate_tax(income, tax_relief)

if taxable_income == 0:
    print("Your income is fully covered by tax relief. No tax payable.\n")
else:
    print(f"Your tax payable is: RM {tax_payable}\n")


data = [ic_number, income, tax_relief, tax_payable]
functions.save_to_csv(data, FILENAME)
print(f"Your data has been saved to {FILENAME}\n")


view = input("Do you want to view all tax records? (Y/N): ").upper()
if view == 'Y':
    df = functions.read_from_csv(FILENAME)
    if df is not None:
        print("\n=== All Tax Records ===")
        print(df)
    else:
        print("No records found.")
