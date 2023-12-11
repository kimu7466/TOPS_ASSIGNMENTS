#include <stdio.h>

int main() {
    char ch;

    // Input a character
    printf("Enter a character: ");
    scanf(" %c", &ch); // Note the space before %c to consume any whitespace

    // Convert the character to lowercase (if it's an uppercase letter)
    if (ch >= 'A' && ch <= 'Z') {
        ch = ch + 32; // Convert to lowercase
    }

    // Check if the character is a vowel or a consonant using a switch statement
    switch (ch) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            printf("%c is a vowel.\n", ch);
            break;
        default:
            if (ch >= 'a' && ch <= 'z') {
                printf("%c is a consonant.\n", ch);
            } else {
                printf("Invalid input! Please enter a valid lowercase letter.\n");
            }
            break;
    }

    return 0;
}

