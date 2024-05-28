#include <stdio.h>

int main() {
    double num1, num2, result;
    char operator;

    
    printf("Enter first number: ");
    scanf("%lf", &num1);

    printf("Enter operator (+, -, *, /, %%): ");
    scanf(" %c", &operator); 

    printf("Enter second number: ");
    scanf("%lf", &num2);
    
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
            if (num2 == 0) {
                printf("Error! Division by zero is not allowed.\n");
                return 1; 
            }
            result = num1 / num2;
            break;
        case '%':            
            if (num2 == 0) {
                printf("Error! Modulo by zero is not allowed.\n");
                return 1; 
            }
            result = fmod(num1, num2); 
            break;
        default:
            printf("Error! Invalid operator.\n");
            return 1; 
    }

    printf("Result: %lf\n", result);

    return 0;
}

