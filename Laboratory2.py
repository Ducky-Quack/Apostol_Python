# Consumer's purchases and its sum
first = float((input("Enter the first amount of your purchase: ")))
second = float((input("Enter the second amount of your purchase: ")))
third = float((input("Enter the third amount of your purchase: ")))
sum_purchase = (first, second, third)

a = sum(sum_purchase)
print(f"Total purchase amount: {a}")


# Check for "discount" condition
if a > 100:
    # Apply discount (10%)
    print("You are qualified for a discount!")
    new_total = a * 0.9
    
    print(f"New Total: {new_total}")
else:
    new_total = a

# Loyalty points calculation (if a is at least 10)
if a >= 10:
    print("You will receive loyalty points!")
    
    # Get point for each 10.00
    loyalty_point = new_total // 10
    print(f"Loyalty points: {loyalty_point}")


# Payment of customer
payment = float(input("Enter your payment: "))

while payment < new_total:
    print(f"Insufficient payment. You still need to pay at least {new_total}.")
    payment = float(input("Enter your payment: "))

print("Transaction is complete! Thank you for the payment!")

if payment > new_total:
    change = payment - new_total
    print(f"Change: {change}")
