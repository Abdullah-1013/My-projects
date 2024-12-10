def factorial(n):
    result = 1  # Initialize the factorial result as 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by the current number
    return result  # Return the factorial

def sum_of_factorials():
    num = int(input("Enter a number: "))  # Ask the user for a number
    total = 0  # Initialize the total sum of factorials
    while num > 0:  # Continue until the number becomes 0
        digit = num % 10  # Extract the last digit of the number
        total += factorial(digit)  # Add the factorial of the digit to the total
        num //= 10  # Remove the last digit by integer division
    print(f"The sum of the factorials of the digits is: {total}")  # Display the total
sum_of_factorials()

# Example Output: 

# Enter a number: 124
# The sum of the factorials of the digits is: 27