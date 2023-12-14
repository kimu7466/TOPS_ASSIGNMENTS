#include <iostream>
#include <string>

class BankAccount {
public:
    // Constructor to initialize account details
    BankAccount(const std::string& name, long accountNumber, const std::string& accountType, double balance) {
        depositorName = name;
        accountNum = accountNumber;
        accountTypeStr = accountType;
        accountBalance = balance;
    }

    // Member function to deposit an amount
    void deposit(double amount) {
        if (amount > 0) {
            accountBalance += amount;
            std::cout << "Deposit of $" << amount << " successful." << std::endl;
        } else {
            std::cout << "Invalid deposit amount." << std::endl;
        }
    }

    // Member function to withdraw an amount
    void withdraw(double amount) {
        if (amount > 0 && amount <= accountBalance) {
            accountBalance -= amount;
            std::cout << "Withdrawal of $" << amount << " successful." << std::endl;
        } else {
            std::cout << "Invalid withdrawal amount or insufficient balance." << std::endl;
        }
    }

    // Member function to display name and balance
    void displayInfo() {
        std::cout << "Account Information" << std::endl;
        std::cout << "Depositor Name: " << depositorName << std::endl;
        std::cout << "Account Number: " << accountNum << std::endl;
        std::cout << "Account Type: " << accountTypeStr << std::endl;
        std::cout << "Account Balance: $" << accountBalance << std::endl;
    }

private:
    std::string depositorName;
    long accountNum;
    std::string accountTypeStr;
    double accountBalance;
};

int main() {
    // Create a BankAccount object and initialize it
    BankAccount account1("John Doe", 1234567890, "Savings", 1000.0);

    // Deposit and withdraw some amount
    account1.deposit(500.0);
    account1.withdraw(200.0);

    // Display account information
    account1.displayInfo();

    return 0;
}

