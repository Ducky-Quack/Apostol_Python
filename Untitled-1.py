# Initialize an empty list to store the purchase amounts
purchases = []

# Use a loop to get the purchase amounts
for i in range(1, 4):  # Adjust the range for more purchases
    amount = float(input(f"Enter the amount for purchase {i}: "))
    purchases.append(amount)

# Calculate the total of all purchases
a = sum(purchases)
print(f"Total purchase amount: {a}")
