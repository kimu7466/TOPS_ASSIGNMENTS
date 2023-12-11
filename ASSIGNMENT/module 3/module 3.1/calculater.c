#include <stdio.h>

int main() {
    double num1, num2, result;
    char operator;

    // Input from the user
    printf("Enter first number: ");
    scanf("%lf", &num1);

    printf("Enter operator (+, -, *, /, %%): ");
    scanf(" %c", &operator); // Note the space before %c to consume any whitespace

    printf("Enter second number: ");
    scanf("%lf", &num2);

    // Perform the calculation based on the operator
    switch (operator) {
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
            // Check for division by zero
            if (num2 == 0) {
                printf("Error! Division by zero is not allowed.\n");
                return 1; // Exit with an error code
            }
            result = num1 / num2;
            break;
        case '%':
            // Check for modulo by zero
            if (num2 == 0) {
                printf("Error! Modulo by zero is not allowed.\n");
                return 1; // Exit with an error code
            }
            result = fmod(num1, num2); // Using fmod for floating-point modulo
            break;
        default:
            printf("Error! Invalid operator.\n");
            return 1; // Exit with an error code
    }

    // Display the result
    printf("Result: %.2f\n", result);

    return 0;
}



