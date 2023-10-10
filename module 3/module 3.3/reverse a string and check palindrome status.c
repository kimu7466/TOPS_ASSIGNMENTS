//palindrom words means reverseing them doesn't make any changes like alala/ lilil/ zozoz/ radar etc.
#include <stdio.h>
#include <string.h>

// Function to reverse a string
void reverseString(char str[]) {
    int length = strlen(str);
    for (int i = 0, j = length - 1; i < j; i++, j--) {
        char temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

// Function to check if a string is a palindrome
int isPalindrome(char str[]) {
    int length = strlen(str);
    for (int i = 0, j = length - 1; i < j; i++, j--) {
        if (str[i] != str[j]) {
            return 0; // Not a palindrome
        }
    }
    return 1; // It is a palindrome
}

int main() {
    char str[100];

    printf("Enter a string: ");
    gets(str);  // You can also use scanf or fgets for string input.

    // Reverse the string
    reverseString(str);

    printf("Reversed string: %s\n", str);

    if (isPalindrome(str)) {
        printf("The string is a palindrome.\n");
    } else {
        printf("The string is not a palindrome.\n");
    }

    return 0;
}


