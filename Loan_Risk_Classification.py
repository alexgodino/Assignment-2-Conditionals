# Loan Risk Classification

# Ask the user for inputs
credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your annual income: "))

# Determine loan risk category
if credit_score >= 720 and income >= 60000:
    risk = "Low Risk"
elif credit_score >= 650 and income >= 40000:
    risk = "Medium Risk"
else:
    risk = "High Risk"

# Print result
print(f"Loan Risk Category: {risk}")
