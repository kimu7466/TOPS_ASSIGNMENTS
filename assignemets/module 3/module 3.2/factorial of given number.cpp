#include <stdio.h>

int main() {
    int num;
    unsigned long long factorial = 1; // To handle large factorials

    // Input a non-negative integer
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    // Check if the input is negative
    if (num < 0) {
        printf("Factorial is undefined for negative numbers.\n");
    } else {
        // Calculate the factorial
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        // Display the factorial
        printf("The factorial of %d is %llu\n", num, factorial);
    }

    return 0;
}

