#include <stdio.h>

int main() {
    int num, i;

 // Input for the table
    printf("Enter a number to print its table: ");
    scanf("%d", &num);

    // Print the table up to 10 multiples
    printf("Table of %d:\n", num);
    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
    }
return 0;
}
