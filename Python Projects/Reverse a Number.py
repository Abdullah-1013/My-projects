def reverse_number():
    num = int(input("Enter a number to reverse: "))  # Ask the user for a number
    reversed_num = 0  # Initialize the reversed number as 0
    while num > 0:  # Continue until the number becomes 0
        digit = num % 10  # Extract the last digit of the number
        reversed_num = reversed_num * 10 + digit  # Build the reversed number
        num //= 10  # Remove the last digit by integer division
    print(f"The reversed number is: {reversed_num}")  # Display the reversed number
reverse_number()

# Example Output:

# Enter a number to reverse: 54321
# The reversed number is: 12345



