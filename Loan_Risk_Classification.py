def classify_loan_risk(credit_score, annual_income):
    """Return risk category string based on credit score and annual income."""
    try:
        cs = float(credit_score)
        inc = float(annual_income)
    except Exception:
        raise ValueError("Credit score and annual income must be numbers")

    if cs >= 720 and inc >= 60000:
        return "Low Risk"
    elif cs >= 650 and inc >= 40000:
        return "Medium Risk"
    else:
        return "High Risk"


if __name__ == "__main__":
    try:
        credit_score = float(input("Enter credit score: "))
        annual_income = float(input("Enter annual income: $"))
    except ValueError:
        print("Invalid input. Please enter numeric values for credit score and income.")
    else:
        category = classify_loan_risk(credit_score, annual_income)
        print(f"Loan Risk Category: {category}")
