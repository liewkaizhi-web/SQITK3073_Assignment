
import pandas as pd
import os

def verify_user(ic_number, password):
    return len(ic_number) == 12 and password == ic_number[-4:]

def calculate_tax_relief(spouse_income, num_children, medical_expenses,
                         lifestyle_expenses, education_fees, parental_care):
    self_relief = 9000
    spouse_relief = 4000 if spouse_income < 4000 else 0
    children_relief = num_children * 2000
    medical_relief = min(medical_expenses, 8000)
    lifestyle_relief = min(lifestyle_expenses, 2500)
    education_relief = min(education_fees, 7000)
    parental_relief = min(parental_care, 5000)

    total_relief = (self_relief + spouse_relief + children_relief +
                    medical_relief + lifestyle_relief + education_relief + parental_relief)

    return {
        "self_relief": self_relief,
        "spouse_relief": spouse_relief,
        "children_relief": children_relief,
        "medical_relief": medical_relief,
        "lifestyle_relief": lifestyle_relief,
        "education_relief": education_relief,
        "parental_relief": parental_relief,
        "total_relief": total_relief
    }

def calculate_tax(income, relief):
    taxable_income = max(0, income - relief)
    if taxable_income == 0:
        return 0
    if taxable_income <= 5000:
        return taxable_income * 0.01
    elif taxable_income <= 20000:
        return 5000*0.01 + (taxable_income-5000)*0.03
    elif taxable_income <= 35000:
        return 5000*0.01 + 15000*0.03 + (taxable_income-20000)*0.08
    elif taxable_income <= 50000:
        return 5000*0.01 + 15000*0.03 + 15000*0.08 + (taxable_income-35000)*0.14
    else:
        return 5000*0.01 + 15000*0.03 + 15000*0.08 + 15000*0.14 + (taxable_income-50000)*0.21

def save_to_csv(data, filename):
    df = pd.DataFrame([data], columns=['IC', 'Income', 'Tax Relief', 'Tax Payable'])
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename):
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        return None
