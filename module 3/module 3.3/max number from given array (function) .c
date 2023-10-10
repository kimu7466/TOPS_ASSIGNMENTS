#include <stdio.h>

// Function to find the maximum number in an array
int findMax(int arr[], int n) {
    int max = arr[0];  // Initialize max with the first element of the array

    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    return max;
}

int main() {
    int n;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max = findMax(arr, n);

    printf("The maximum number in the array is: %d\n", max);

    return 0;
}

