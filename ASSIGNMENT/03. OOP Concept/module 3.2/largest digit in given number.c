#include <stdio.h>

int main() {
    long long int number, maxDigit = -1;

    printf("Enter a number: ");
    scanf("%lld", &number);

    number = (number < 0) ? -number : number;

    while (number != 0) {
        int digit = number % 10;
        if (digit > maxDigit) {
            maxDigit = digit;
        }
        number /= 10;
    }

    printf("Maximum digit: %d\n", maxDigit);

    return 0;
}

