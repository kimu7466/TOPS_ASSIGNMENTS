
/*
 a string is a sequence of characters stored in memory, typically used to represent text. Unlike some other programming languages, C does not have a built-in string data type like "string" in languages such as Python or Java. Instead, C uses arrays of characters to represent strings.
*/
// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>
int main() {
    
    char company[7] = {'S', 'C', 'A', 'L', 'E', 'R' , '\0'};
    char name[100] = "new";
    char name2[100] = "york";
    // printf("Name : %s\n", name);
    
    // printf("%d", strlen(name));
    
    // for(int i = 0; i<strlen(name); i++){
    //     printf("%c\n", name[i]);
    // }
    
    // string copy
    // strcpy(name2, name);
    // printf("%s", name2);
    
    // string comperision
    // int result = strcmp(name, name2);
    // printf("%d", result);
    
    strcat(name, name2);
    printf("%s", name);
    
    return 0;
}



#include <stdio.h>
#include<string.h>
void convertUpperToLower(char text[100]){
    char emptyArray[100];
    
    for (int i = 0; i< strlen(text); i++){
        if (text[i] < 97){
            emptyArray[i] = text[i]+32;
          
            
        }
        
    }
    
    printf("You entered: %s", emptyArray); // Print the user's input
}

int main() {
    char input[100]; // Assuming a maximum input length of 99 characters

    printf("Enter a line of text: ");
    fgets(input, sizeof(input), stdin); // Read input from the user
    convertUpperToLower(input);

    return 0;
}
