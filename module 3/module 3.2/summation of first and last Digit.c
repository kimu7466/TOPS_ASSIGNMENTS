#include <stdio.h>

int main() {
    long long int number;
    int firstDigit, lastDigit, sum;

    printf("Enter a number: ");
    scanf("%lld", &number);

    // Ensure the number is positive by taking its absolute value
    number = (number < 0) ? -number : number;

    // Extract the last digit
    lastDigit = number % 10;

    // Extract the first digit
    while (number >= 10) {
        number /= 10;
    }
    firstDigit = number;

    // Calculate the sum of the first and last digits
    sum = firstDigit + lastDigit;

    printf("Sum of the first and last digits: %d\n", sum);

    return 0;
}

