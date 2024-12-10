def print_diamond():
    n = int(input("Enter the size of the diamond: "))  # Ask the user for the size of the diamond

    for i in range(1, n + 1):  # Loop for the upper part of the diamond
        spaces = n - i  # Calculate the number of spaces
        stars = 2 * i - 1  # Calculate the number of stars
        print(" " * spaces + "*" * stars)  # Print spaces and stars

    for i in range(n - 1, 0, -1):  # Loop for the lower part of the diamond
        spaces = n - i  # Calculate the number of spaces
        stars = 2 * i - 1  # Calculate the number of stars
        print(" " * spaces + "*" * stars)  # Print spaces and stars
print_diamond()


#Example Output:
 
# Enter the size of the diamond: 10
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
#  *****************
#   ***************
#    *************
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *