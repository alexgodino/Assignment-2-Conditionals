# Customer Discount Eligibility

# Ask the user for purchase amount
purchase_amount = float(input("Enter the purchase amount: $"))

# Ask the user if they are a member
is_member = input("Are you a member? (yes/no): ").strip().lower()

# Determine discount percentage
if is_member == 'yes':
    if purchase_amount >= 100:
        discount_percentage = 15
    else:
        discount_percentage = 5
else:
    if purchase_amount >= 150:
        discount_percentage = 10
    else:
        discount_percentage = 0

# Calculate final price after discount
final_price = purchase_amount * (1 - discount_percentage / 100)

# Print discount percentage and final price
print(f'Discount percentage: {discount_percentage}%')
print(f'Final price after discount: ${final_price:.2f}')
