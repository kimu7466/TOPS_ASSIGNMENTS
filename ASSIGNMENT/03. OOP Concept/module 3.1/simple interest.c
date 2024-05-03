#include <stdio.h>

int main() {
    double principalAmount, rateOfInterest, time, simpleInterest;

    // Input principal amount
    printf("Enter the principal amount: ");
    scanf("%lf", &principalAmount);

    // Input rate of interest
    printf("Enter the rate of interest (in percentage): ");
    scanf("%lf", &rateOfInterest);

    // Input time period in years
    printf("Enter the time period (in years): ");
    scanf("%lf", &time);

    // Calculate simple interest
    simpleInterest = (principalAmount * rateOfInterest * time) / 100;

    // Display the result
    printf("Simple Interest: %.2lf\n", simpleInterest);

    return 0;
}

