#include <iostream>
#include <string>

class BankAccount {
public:
    BankAccount(const std::string& name, long accountNumber, const std::string& accountType, double balance) {
        depositorName = name;
        accountNum = accountNumber;
        accountTypeStr = accountType;
        accountBalance = balance;
    }

    void deposit(double amount) {
        if (amount > 0) {
            accountBalance += amount;
            std::cout << "Deposit of $" << amount << " successful." << std::endl;
        } else {
            std::cout << "Invalid deposit amount." << std::endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= accountBalance) {
            accountBalance -= amount;
            std::cout << "Withdrawal of $" << amount << " successful." << std::endl;
        } else {
            std::cout << "Invalid withdrawal amount or insufficient balance." << std::endl;
        }
    }

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
    BankAccount account1("John Doe", 1234567890, "Savings", 1000.0);

    account1.deposit(500.0);
    account1.withdraw(200.0);

    account1.displayInfo();

    return 0;
}

