#include <stdio.h>

int main() {
    long long int number;
    int sum = 0;

    printf("Enter a number: ");
    scanf("%lld", &number);

    number = (number < 0) ? -number : number;

    while (number != 0) {
        int digit = number % 10;
        sum += digit;
        number /= 10;
    }

    printf("Sum of digits: %d\n", sum);

    return 0;
}

