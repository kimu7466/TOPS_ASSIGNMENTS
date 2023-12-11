#include <stdio.h>

// Recursive function to reverse a string
void reverseString(char str[]) {
    if (str[0] == '\0') {
        return; // Base case: when the string is empty
    } else {
        reverseString(str + 1); // Recursive call to reverse the rest of the string
        putchar(str[0]); // Print the current character
    }
}

int main() {
    char inputString[100];

    printf("Enter a string: ");
    fgets(inputString, sizeof(inputString), stdin);

    printf("Reversed string: ");
    reverseString(inputString);

    return 0;
}

