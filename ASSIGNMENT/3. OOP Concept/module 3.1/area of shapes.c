#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    double area;

    printf("Choose a shape to calculate its area:\n");
    printf("1. Circle\n");
    printf("2. Rectangle\n");
    printf("3. Triangle\n");
    printf("Enter your choice (1/2/3): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: {
            double radius;
            printf("Enter the radius of the circle: ");
            scanf("%lf", &radius);

            if (radius < 0) {
                printf("Error: Radius cannot be negative.\n");
                return 1;
            }

            area = M_PI * radius * radius;
            printf("The area of the circle is: %.2lf square units\n", area);
            break;
        }

        case 2: {
            double length, width;
            printf("Enter the length of the rectangle: ");
            scanf("%lf", &length);
            printf("Enter the width of the rectangle: ");
            scanf("%lf", &width);

            if (length < 0 || width < 0) {
                printf("Error: Length and width cannot be negative.\n");
                return 1;
            }

            area = length * width;
            printf("The area of the rectangle is: %.2lf square units\n", area);
            break;
        }

        case 3: {
            double base, height;
            printf("Enter the base length of the triangle: ");
            scanf("%lf", &base);
            printf("Enter the height of the triangle: ");
            scanf("%lf", &height);

            if (base < 0 || height < 0) {
                printf("Error: Base and height cannot be negative.\n");
                return 1;
            }

            area = 0.5 * base * height;
            printf("The area of the triangle is: %.2lf square units\n", area);
            break;
        }

        default:
            printf("Error: Invalid choice! Please select 1, 2, or 3.\n");
            return 1;
    }

    return 0;
}

