#include <stdio.h>
#include <string.h>

// Define the structure to store employee information
struct employee {
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main() {
    struct employee emp;

    // Input employee information
    printf("Enter Employee Number: ");
    scanf("%d", &emp.empno);

    printf("Enter Employee Name: ");
    scanf(" %[^\n]s", emp.empname);

    printf("Enter Employee Address: ");
    scanf(" %[^\n]s", emp.address);

    printf("Enter Employee Age: ");
    scanf("%d", &emp.age);

    // Display employee information
    printf("\nEmployee Information:\n");
    printf("Employee Number: %d\n", emp.empno);
    printf("Employee Name: %s\n", emp.empname);
    printf("Employee Address: %s\n", emp.address);
    printf("Employee Age: %d\n", emp.age);

    return 0;
}

