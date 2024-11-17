# Function to calculate the average of 5 numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Input: Prompt the user for 5 numbers
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(num)

# Calculate the average
average = calculate_average(numbers)

# Output the result
print(f"The average of the numbers {numbers} is: {average}")
