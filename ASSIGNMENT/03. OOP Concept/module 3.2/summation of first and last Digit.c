#include <stdio.h>

int main() {
    long long int number;
    int firstDigit, lastDigit, sum;

    printf("Enter a number: ");
    scanf("%lld", &number);

    number = (number < 0) ? -number : number;

    lastDigit = number % 10;

    while (number >= 10) {
        number /= 10;
    }
    firstDigit = number;

    sum = firstDigit + lastDigit;

    printf("Sum of the first and last digits: %d\n", sum);

    return 0;
}

