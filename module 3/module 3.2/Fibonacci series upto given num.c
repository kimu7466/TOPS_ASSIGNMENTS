#include <stdio.h>

int main() {
    int n, i;
    long long int a = 0, b = 1, next;

    printf("Enter the number of terms you want in the Fibonacci series: ");
    scanf("%d", &n);

    printf("Fibonacci Series up to %d terms:\n", n);

    for (i = 0; i < n; i++) {
        if (i <= 1) {
            next = i;
        } else {
            next = a + b;
            a = b;
            b = next;
        }
        printf("%lld ", next);
    }

    printf("\n");

    return 0;
}

