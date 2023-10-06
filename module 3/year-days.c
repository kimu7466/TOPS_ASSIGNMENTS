#include <stdio.h>

int main() {
    int choice;
    double years, days;

    printf("Choose the conversion:\n");
    printf("1. Years to Days\n");
    printf("2. Days to Years\n");
    printf("Enter your choice (1/2): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            // Convert years to days
            printf("Enter the number of years: ");
            scanf("%lf", &years);
            days = years * 365.0; // Assuming all years have 365 days
            printf("%.2lf years is equal to %.2lf days.\n", years, days);
            break;

        case 2:
            // Convert days to years
            printf("Enter the number of days: ");
            scanf("%lf", &days);
            years = days / 365.0; // Assuming all years have 365 days
            printf("%.2lf days is equal to %.2lf years.\n", days, years);
            break;

        default:
            printf("Invalid choice! Please select 1 or 2.\n");
            break;
    }

    return 0;
}

