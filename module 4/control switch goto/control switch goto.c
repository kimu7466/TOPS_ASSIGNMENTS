# 1
// Control statments
#include <stdio.h>

int main() {
    int num = 20;
    for (int i =  1; i<=num; i++){
        if ((i == 6 ) || (i == 8)){
            continue;
        }
        if (i == 11){
            break;
        }
        printf("%d\n", i);
    }
    return 0;
}




# 2
// switch case
// Online C compiler to run C program online
#include <stdio.h>

int main() {
    while(1){
        int day;
        printf("Enter a num : ");
        scanf("%d", &day);
        switch (day){
        case 1:
            printf("Today is Sun");
            break;
        case 2:
            printf("Today is Mon");
            break;
        case 3:
            printf("Today is Tue");
            break;
        case 4:
            printf("Today is Wed");
            break;
        case 5:
            printf("Today is Thu");
            break;
        case 6:
            printf("Today is Fri");
            break;
        case 7:
            printf("Today is Sat");
            break;
        default:
            printf("Invalid num");
        }
    }
    return 0;
}



# 3
// go to statement
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 2 == 0) {
        goto even;
    }

    if (num % 2 != 0) {
        goto odd;
    }

even:
    printf("%d is Even\n", num);
    return 0;

odd:
    printf("%d is Odd\n", num);
    return 0;
}


// Single dim
#include <stdio.h>

int main() {
    int score[8] = {
        34,56,67,57,68,79,90, 86
    };
    
    int start = 0;
    int length = sizeof(score)/sizeof(score[0]);
    printf("Len of array is : %d\n\n", length);
    while(start < length){
        printf("scoree #000%d - score = %d\n", start + 1, score[start]);
        start += 1;
    }
    
    return 0;
}




// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int matrix1[2][3] = {
        {1,2,3}, {4,5,6}
    };
    
    int matrix2[2][3] = {
        {11,22,33}, {44,55,66}
    };
    
    printf("Matrix : 1\n");
    for (int r = 0; r<2; r++){
        for(int c = 0; c < 3; c++){
            printf("%d\t", matrix1[r][c]);
        }
        printf("\n");
    }
    
    printf("Matrix : 2\n");
    for (int r = 0; r<2; r++){
        for(int c = 0; c < 3; c++){
            printf("%d\t", matrix2[r][c]);
        }
        printf("\n");
    }
    
    printf("Matrix : 1 + Matrix : 2  = final_matrix\n");
    
    for (int r = 0; r<2; r++){
        for(int c = 0; c < 3; c++){
            printf("%d\t", matrix1[r][c] * matrix2[r][c]);
        }
        printf("\n");
    }
    
    return 0;
}

