def is_prime(num):
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of the number
        if num % i == 0:  # If divisible, it's not prime
            return False
    return True  # Return true if no divisors are found

def sum_of_primes():
    start = int(input("Enter the starting number: "))  # Ask the user for the starting number
    end = int(input("Enter the ending number: "))  # Ask the user for the ending number
    total = 0  # Initialize the sum of primes
    for num in range(start, end + 1):  # Loop through the range
        if is_prime(num):  # Check if the number is prime
            total += num  # Add the prime number to the total
    print(f"The sum of all prime numbers between {start} and {end} is: {total}")  # Display the sum
sum_of_primes()


# Possible Output
# Enter the starting value: 1
# Enter the last Value:11
# Answer: 28