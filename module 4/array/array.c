# 4
// single dim
#include <stdio.h>

int main() {
    int students[] = { 34, 45, 56, 67, 78, 89, 90 };
    // printf("%d", students[5]);
    
    int length = sizeof(students)/sizeof(students[0]);
    // printf("Length : %d", length);
    
    for( int i = 0; i<length; i += 1){
        printf("%d\n", students[i]);
    }
}

// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int students[] = { 34, 45, 56, 67, 78, 89, 90 };
    // printf("%d", students[5]);
    students[5] = 111;
    int length = sizeof(students)/sizeof(students[0]);
    // printf("Length : %d", length);
    
    for( int i = 0; i<length; i += 1){
        printf("%d\n", students[i]);
    }
}




// Online C compiler to run C program online
#include <stdio.h>

int main() {
    
    int total, score;
    printf("Enter a num: ");
    scanf("%d", &total);
    
     int students[total];
    for( int i = 0; i<total; i += 1){
        printf("Enter a score for #000%d : ", i);
        scanf("%d", &score);
        students[i] = score;
    }
    
    for( int i = 0; i<total; i += 1){
        printf("#000%d : score - %d\n", i, students[i]);
    }
}




# // Online C compiler to run C program online
#include <stdio.h>

int main() {
    
    int total, score;
    printf("Enter a num: ");
    scanf("%d", &total);
    
     int students[total];
    for( int i = 0; i<total; i += 1){
        printf("Enter a score for #000%d : ", i);
        scanf("%d", &score);
        students[i] = score;
    }
    
    for( int i = 0; i<total; i += 1){
        printf("#000%d : score - %d\n", i, students[i]);
    }
}

