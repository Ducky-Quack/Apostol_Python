print("You are requesting a loan...")

monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter your request loan amount: "))

# Check if eligible for a loan
if monthly_salary < 30000:
    print("You are not eligible for a loan request. Reason: Low salary")
    print("You need to have at least 30,000 monthly salary.")

elif loan_amount > monthly_salary * 10:
    print("You are not eligible for a loan request. Reason: High loan request")
    print("You may only request up to 10 times your monthly salary.")

