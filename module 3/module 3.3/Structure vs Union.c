#include <stdio.h>

// Define a structure
struct StructExample {
    int x;
    double y;
    char z;
};

// Define a union
union UnionExample {
    int x;
    double y;
    char z;
};

int main() {
    struct StructExample s;
    union UnionExample u;

    printf("Size of Structure: %lu bytes\n", sizeof(s)); // Size is 16 bytes (4 + 8 + 1 + padding)
    printf("Size of Union: %lu bytes\n", sizeof(u));     // Size is 8 bytes (largest member is double)

    s.x = 10;
    u.x = 10;

    printf("Value of x in Structure: %d\n", s.x); // 10
    printf("Value of x in Union: %d\n", u.x);     // 10

    s.y = 3.14;
    u.y = 3.14;

    printf("Value of y in Structure: %.2lf\n", s.y); // 3.14
    printf("Value of y in Union: %.2lf\n", u.y);     // 3.14

    return 0;
}

