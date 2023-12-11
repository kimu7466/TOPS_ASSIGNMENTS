#include <stdio.h>

int main() {
    int even_count = 0, odd_count = 0;
    int even_sum = 0, odd_sum = 0;
    int num, i;
     
    // Input 10 numbers from the user
    for (i = 0; i < 10; i++) {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &num);

        if (num % 2 == 0) {
            even_count++;
            even_sum += num;
        } else {
            odd_count++;
            odd_sum += num;
        }
    }

    // Print the results
    printf("Number of even numbers: %d\n", even_count);
    printf("Number of odd numbers: %d\n", odd_count);
    printf("Sum of even numbers: %d\n", even_sum);
    printf("Sum of odd numbers: %d\n", odd_sum);

    return 0;
}

