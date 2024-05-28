#include <stdio.h>


void reverseString(char str[]) {
    if (str[0] == '\0') {
        return; 
    } else {
        reverseString(str + 1); 
        putchar(str[0]); 
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

