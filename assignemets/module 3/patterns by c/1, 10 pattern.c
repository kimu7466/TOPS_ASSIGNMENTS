#include <stdio.h>

int main() {
    int rows;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    for (int i = 1; i <= rows; i++) { 
        int num = 1;  // Initialize the first number as 1
        for (int j = 1; j <= i; j++) {
            printf("%d ", num);
            num = 1 - num;  // Toggle between 0 and 1
        }
        printf("\n");
    }

    return 0;
}

