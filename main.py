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


while True:
    try:
        tax_relief = float(input("Enter your total tax relief (RM): "))
        if tax_relief < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number.")


tax_payable = functions.calculate_tax(income, tax_relief)
print(f"\nYour tax payable is: RM {tax_payable}")


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