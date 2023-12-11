#include <stdio.h>

int main() {
    int rows;
    int currentNumber = 1;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", currentNumber);
            currentNumber++;
        }
        printf("\n");
    }

    return 0;
}

