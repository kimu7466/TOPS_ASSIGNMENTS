// Online C compiler to run C program online
#include <stdio.h>

// return_type function_name(para1, para2 ....paran){
    // block of code
// }

// function_name(v1, v2....vn);

int add(int num1, int num2){
    int total = num1 + num2;
    // printf("%d\n", total);
    return total;
}


int main() {
    int z = add(10, 20);
    // printf("%d", z);
    printf("%d", add(30, 40) + z);
    // add(30, 40);
    // add(300, 400);
    return 0;
}



// Online C compiler to run C program online
#include <stdio.h>

void mul(){
    int num1 =10, num2 = 2;
    printf("%d", num1 * num2);
}

int main() {
   mul();

}

// with return_type and with para
// int mul(int num1, int num2){
//     return num1 * num2;
// }


// with return_type and without para
// int mul(){
//     int num1 =10, num2 = 2;
//     return num1 * num2;
// }

// without return_type and with para
// void mul(int num1, int num2){
//     printf("%d", num1 * num2);
// }


// without return_type and without para
// void mul(){
//     int num1 =10, num2 = 2;
//     printf("%d", num1 * num2);
// }

#include <stdio.h>

int fibbo(int num){
    int first = 0, second = 1, next;
    printf("Fibonacci Series: ");
    for (int i = 0; i < num; i++) {
        if (i <= 1)
            next = i;
        else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d ", next);
    }
}

int main() {
    
    int num;
    printf("Enter the number of terms: ");
    scanf("%d", &num);
    
    fibbo(num);
    return 0;
}


#include <stdio.h>

int fibbo(int num) {
    if (num <= 1)
        return num;
    else
        printf("---------");
        printf("=%d\n", num);
        printf("%d + %d\n", fibbo(num - 1), fibbo(num - 2));
        return fibbo(num - 1) + fibbo(num - 2);
}

int main() {
    int num;
    printf("Enter the number of terms: ");
    scanf("%d", &num);

    printf("Fibonacci Series: ");
    for (int i = 0; i < num; i++) {
        // printf("%d===", i);
        printf("%d \n", fibbo(i));
    }

    return 0;
}


#include <stdio.h>

// Function to calculate factorial using recursion
int factorial(int num) {
    if (num == 0 || num == 1)
        return 1;
    else
        return num * factorial(num - 1);
}

int main() {
    int num;

    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    if (num < 0)
        printf("Factorial is not defined for negative numbers.\n");
    else
        printf("Factorial of %d is %d\n", num, factorial(num));

    return 0;
}

* * * * * * * 
*   *   *   *
* * *   *   *
*       *   *
* * * * *   *
*           *
* * * * * * *

NUM  = 7
for (row){
    IF (row = EVEN){
        for (column){
            if (column == 1){
                printf("*")
                continue;
            }
            else {
                printf(" ")
            }
        }
    (EVEN)
    } ELSE{
        (row = ODD)
        for (column){

        }
    }
}
