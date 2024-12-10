def is_armstrong():
    num = int(input("Enter a number: "))  # Ask the user for a number
    original_num = num  # Save the original number for comparison later
    num_digits = 0  # Initialize the digit count
    temp = num  # Create a temporary variable to count digits

    while temp > 0:  # Count the number of digits
        num_digits += 1  # Increment the digit count
        temp //= 10  # Remove the last digit

    temp = num  # Reset the temporary variable to calculate the Armstrong sum
    armstrong_sum = 0  # Initialize the Armstrong sum
    while temp > 0:  # Calculate the Armstrong sum
        digit = temp % 10  # Extract the last digit
        armstrong_sum += digit ** num_digits  # Add the digit raised to the power of num_digits
        temp //= 10  # Remove the last digit

    if armstrong_sum == original_num:  # Check if the Armstrong sum equals the original number
        print(f"{original_num} is an Armstrong number.")  # Output if it's an Armstrong number
    else:
        print(f"{original_num} is not an Armstrong number.")  # Output if it's not
is_armstrong()

# Armstong numbers:

# The number is said to be armstrong, if we take their powers and then their sum will be equal to the
# origional number or the number itself then the number is said to armstrong number.e.g 153,1634,54748 etc

# Example Output:

# For 3 digits:

# The digits are: 153,370,371,407(If we take cubes of each digit of each number and then sum them answer
# will be same as number. 1^3+5^3+3^3=153)
# Enter a number: 153,370,371,407
# 153 is an Armstrong number.

# For 4 digits:

# The digits are: 1634,8208,9474(If we take 4th-root of each digit of each number and then sum them answer
# will be same as number. 1^4+6^4+3^4+4^4=1634)
# Enter a number: 1634,8208,9474
# 153 is an Armstrong number.

# For 5 digits:

# The digits are: 54748,92727,93084(If we take 5th-root of each digit of each number and then sum them answer
# will be same as number. 5^5+4^5+7^5+4^5+8^5=54748)
# Enter a number: 54748,92727,93084
# 153 is an Armstrong number.


