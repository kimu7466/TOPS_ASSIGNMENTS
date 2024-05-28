#include <stdio.h>

struct StructExample {
    int x;
    double y;
    char z;
};

union UnionExample {
    int x;
    double y;
    char z;
};

int main() {
    struct StructExample s;
    union UnionExample u;

    printf("Size of Structure: %lu bytes\n", sizeof(s)); 
    printf("Size of Union: %lu bytes\n", sizeof(u));     

    s.x = 10;
    u.x = 10;

    printf("Value of x in Structure: %d\n", s.x); 
    printf("Value of x in Union: %d\n", u.x);     

    s.y = 3.14;
    u.y = 3.14;

    printf("Value of y in Structure: %.2lf\n", s.y); 
    printf("Value of y in Union: %.2lf\n", u.y);     

    return 0;
}

