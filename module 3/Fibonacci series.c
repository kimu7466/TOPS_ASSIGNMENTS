#include <stdio.h>

int main() {
    int n, first = 0, second = 1, next;

    // Input the number up to which you want to print the Fibonacci series
    printf("Enter the number up to which you want to print the Fibonacci series: ");
    scanf("%d", &n);

    printf("Fibonacci series up to %d terms:\n", n);

    // Special case for the first two Fibonacci numbers
    if (n >= 1) {
        printf("%d", first);
    }
    if (n >= 2) {
        printf(", %d", second);
    }

    // Calculate and print the rest of the Fibonacci series
    for (int i = 3; i <= n; i++) {
        next = first + second;
        printf(", %d", next);
        first = second;
        second = next;
    }

    printf("\n");

    return 0;
}

