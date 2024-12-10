def count_unique_elements():
    n = int(input("Enter the number of elements in the list: "))  # Ask the user for the number of elements
    numbers = []  # Initialize an empty list to store the numbers
    for _ in range(n):  # Loop to get the numbers from the user
        num = int(input("Enter a number: "))  # Ask for a number
        numbers.append(num)  # Add the number to the list

    unique_count = 0  # Initialize the count of unique elements
    for i in range(len(numbers)):  # Loop through each number in the list
        is_unique = True  # Assume the number is unique
        for j in range(len(numbers)):  # Check against all other numbers
            if i != j and numbers[i] == numbers[j]:  # If a duplicate is found
                is_unique = False  # Mark as not unique
                break  # Exit the inner loop
        if is_unique:  # If the number is unique
            unique_count += 1  # Increment the unique count
    print(f"The number of unique elements is: {unique_count}")  # Display the count
count_unique_elements()


# Example Output:
# Enter the number of elements in the list: 6
# Enter a number: 10
# Enter a number: 10
# Enter a number: 20
# Enter a number: 20
# Enter a number: 3
# Enter a number: 2
# The number of unique elements is: 2