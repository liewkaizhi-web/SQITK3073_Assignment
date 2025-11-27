
import pandas as pd
import os

def verify_user(ic_number, password):
    if len(ic_number) == 12 and password == ic_number[-4:]:
        return True
    else:
        return False
    

def calculate_tax(income, tax_relief):

    taxable_income = max(0, income - tax_relief)
    
    tax = 0
    brackets = [(5000, 0), (20000, 0.01), (35000, 0.03), (50000, 0.06), (70000, 0.11), (100000, 0.19), (400000, 0.25),(600000, 0.26),(2000000, 0.28),(float('inf'), 0.30)]
    lower = 0
    for upper, rate in brackets:
        if taxable_income > upper:
            tax += (upper - lower) * rate
            lower = upper
        else:
            tax += (taxable_income - lower) * rate
            break
    return round(tax, 2)

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