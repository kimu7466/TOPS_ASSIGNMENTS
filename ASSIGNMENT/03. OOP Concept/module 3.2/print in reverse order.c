#include <stdio.h>

int main() {
    long long int number, reversedNumber = 0;

    printf("Enter a number: ");
    scanf("%lld", &number);

    while (number != 0) {
        int digit = number % 10;
        reversedNumber = reversedNumber * 10 + digit;
        number /= 10;
    }

    printf("Reversed number: %lld\n", reversedNumber);

    return 0;
}

