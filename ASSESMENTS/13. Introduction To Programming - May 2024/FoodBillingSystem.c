#include <stdio.h>

int main() {
    int choice, quantity;
    char moreOrders;
    int totalAmount = 0;
    
    printf("1. Pizza       - 180 Rs/pcs\n");
    printf("2. Burger      - 100 Rs/pcs\n");
    printf("3. Dosa        - 120 Rs/pcs\n");
    printf("4. Idli        - 50 Rs/pcs\n");
    
    do {
        printf("\nPlease enter your choice: ");
        scanf("%d", &choice);
        
        printf("Enter the quantity: ");
        scanf("%d", &quantity);
        
        switch(choice) {
            case 1:
                printf("You have selected Pizza.\n");
                totalAmount += 180 * quantity;
                break;
            case 2:
                printf("You have selected Burger.\n");
                totalAmount += 100 * quantity;
                break;
            case 3:
                printf("You have selected Dosa.\n");
                totalAmount += 120 * quantity;
                break;
            case 4:
                printf("You have selected Idli.\n");
                totalAmount += 50 * quantity;
                break;
            default:
                printf("Invalid choice. Please select a valid option.\n");
                continue;
        }
        
        printf("Total Amount = %d Rs\n", totalAmount);
        printf("Do you want to place more orders? (y/n): ");
        scanf(" %c", &moreOrders);
        
    } while (moreOrders == 'y' || moreOrders == 'Y');
    
    printf("\nFinal Bill: %d Rs\n", totalAmount);
    printf("Thank you for your order!\n");
    
    return 0;
}
