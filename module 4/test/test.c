structures (structs) and unions are composite data types used to group multiple variables of different data types under a single name. Both structures and unions allow you to create custom data types to represent complex data structures, but they differ in how they organize and use memory.


Structure (struct):

A structure, often referred to as a "struct," is a composite data type that allows you to group variables of different data types together under a single name. Each member of the struct has its own memory location, and the total memory size of a struct is the sum of the sizes of its individual members. Structs are typically used when you want to represent a collection of related data with different attributes.


Example :
#include <stdio.h>

struct book{
  char name[100];
  float price;
  int page;
};

int main() {
    struct book b1;
    
    strcpy(b1.name, "c programming");
    b1.price = 39.47;
    b1.page = 34;
    
    printf("Book information of %s\n", b1.name);
    printf("Price : %f\n", b1.price);
    printf("Page : %d\n", b1.page);
    
    struct book b2;
    
    strcpy(b2.name, "python programming");
    b2.price = 399.47;
    b2.page = 344;
    
    printf("Book information of %s\n", b2.name);
    printf("Price : %f\n", b2.price);
    printf("Page : %d\n", b2.page);
    

    return 0;
}


Example :
struct Person {
    char name[50];
    int age;
    float height;
};

struct Person person1;
strcpy(person1.name, "John");
person1.age = 30;
person1.height = 175.5;


Union:

A union, often simply called a "union," is another composite data type that allows you to group variables of different data types together under a single name, just like a struct. However, unlike a struct, a union shares the same memory location for all its members. This means that a union can only hold one value at a time, and the memory size of a union is determined by its largest member.


#include <stdio.h>

union book{
  char name[100];
  float price;
  int page;
};


int main() {
    union book b1;
    
    strcpy(b1.name, "c programming");
    b1.price = 39.47;
    b1.page = 34;
    
    printf("Book information of %s\n", b1.name);
    printf("Price : %f\n", b1.price);
    printf("Page : %d\n", b1.page);
    
    union book b2;
    
    strcpy(b2.name, "python programming");
    b2.price = 399.47;
    b2.page = 344;
    
    printf("Book information of %s\n", b2.name);
    printf("Price : %f\n", b2.price);
    printf("Page : %d\n", b2.page);
    

    return 0;
}
