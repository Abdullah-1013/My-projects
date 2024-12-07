#include <stdio.h>

int main() {
    char operator;
    double num1, num2, result;

    printf("Enter the first number: ");
    scanf("%lf", &num1);

    printf("Enter the second number: ");
    scanf("%lf", &num2);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator); // Added a space before %c to consume any whitespace or newline character

    switch(operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if(num2 != 0) {
                result = num1 / num2;
            } else {
                printf("Error! Division by zero.\n");
                return 1; // Exit the program with an error code
            }
            break;
        default:
            printf("Error! Invalid operator.\n");
            return 1; // Exit the program with an error code
    }

    printf("Result: %lf\n", result);

    return 0;
}
