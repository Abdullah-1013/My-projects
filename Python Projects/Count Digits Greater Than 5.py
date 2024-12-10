def count_digits_greater_than_five():
    count = 0  # Initialize a counter to count digits greater than 5
    n = int(input("Enter how many numbers you want to check: "))  # Ask the user for the number of inputs
    for _ in range(n):  # Loop to process each number
        num = int(input("Enter a number: "))  # Ask the user for a number
        while num > 0:  # Continue processing digits until the number becomes 0
            digit = num % 10  # Extract the last digit of the number
            if digit > 5:  # Check if the digit is greater than 5
                count += 1  # Increment the count
            num //= 10  # Remove the last digit by integer division
    print(f"The total count of digits greater than 5 is: {count}")  # Display the result
count_digits_greater_than_five()

# Example Output:
# Enter how many numbers you want to check: 3
# Enter a number: 67890
# Enter a number: 98760
# Enter a number: 78906
# The total count of digits greater than 5 is: 12