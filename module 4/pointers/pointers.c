a pointer is a variable that is used to store the memory address of another variable. Pointers are a fundamental concept in C and are widely used for tasks like dynamic memory allocation, data manipulation, and working with complex data structures.

Declaration: To declare a pointer, you use an asterisk (*) before the variable name. 

data_type *var_name; // Declares a pointer to an integer

Initialization: Pointers should be initialized with the address of a valid variable before they are used. 

int x = 10;
int z;
int *y = &x;
z = *y;

NULL Pointer: A pointer that does not point to any valid memory location is often set to NULL, which is a special constant representing a null pointer.

int *ptr = NULL; // Initializing ptr to a null pointer

Example :
#include <stdio.h>

int main() {
    int x = 10;
    int *y;
    y = &x;
    printf("%d", *y);

    return 0;
}


Example :
#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;

    printf("Value of x: %d\n", x);
    printf("Value of x using pointer: %d\n", *ptr);

    *ptr = 20; // Modifying the value of x using the pointer

    printf("New value of x: %d\n", x);

    return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int size = 5;

    // Allocate memory for an array of integers
    arr = (int *)malloc(size * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Now you can use arr as an array
    for (int i = 0; i < size; i++) {
        arr[i] = i * 2;
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Don't forget to free the allocated memory when done
    free(arr);

    return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int size = 5;

    // Allocate memory for an array of integers
    arr = (int *)calloc(size, sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Now you can use arr as an array
    for (int i = 0; i < size; i++) {
        arr[i] = i * 2;
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Don't forget to free the allocated memory when done
    free(arr);

    return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int size = 5;

    // Allocate memory for an array of integers
    arr = (int *)calloc(size, sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Now you can use arr as an array
    // for (int i = 0; i < size; i++) {
    //     arr[i] = i * 2;
    //     // printf("arr[%d] = %d\n", i, arr[i]);
    // }
    
    size = 10;
    arr = (int *)realloc(arr, size * sizeof(int));
    
    for (int i = 0; i < size; i++) {
        arr[i] = i * 2;
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Don't forget to free the allocated memory when done
    free(arr);

    return 0;
}

