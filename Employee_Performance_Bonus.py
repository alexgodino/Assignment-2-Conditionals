# Employee Performance Bonus

# Ask the user for annual salary
annual_salary = float(input("Enter your annual salary: $"))

# Ask the user for performance score
performance_score = float(input("Enter your performance score (0-100): "))

# Determine bonus percentage
if performance_score >= 90:
    bonus_percentage = 20
elif performance_score >= 80:
    bonus_percentage = 10
elif performance_score >= 70:
    bonus_percentage = 5
else:
    bonus_percentage = 0

# Calculate bonus amount
bonus_amount = (bonus_percentage / 100) * annual_salary

# Print bonus percentage and amount
print(f'Performance Bonus: {bonus_percentage}%')
print(f'Bonus Amount: ${bonus_amount:.2f}')