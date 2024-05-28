#include <stdio.h>

int main() {
    double principalAmount, rateOfInterest, time, simpleInterest;

        printf("Enter the principal amount: ");
    scanf("%lf", &principalAmount);

        printf("Enter the rate of interest (in percentage): ");
    scanf("%lf", &rateOfInterest);

        printf("Enter the time period (in years): ");
    scanf("%lf", &time);

        simpleInterest = (principalAmount * rateOfInterest * time) / 100;

        printf("Simple Interest: %.2lf\n", simpleInterest);

    return 0;
}

