monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
monthly_saving = monthly_income - monthly_expenses
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print   (f"your monthly savings are:${monthly_saving}")
print (f"Projected savings after one year, with interest, is: ${projected_savings}")
