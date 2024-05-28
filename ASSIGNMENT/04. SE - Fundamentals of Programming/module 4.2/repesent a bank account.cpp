#include <iostream>
#include <string>
using namespace std;

class BankAccount {
public:
    BankAccount(const string& name, long accountNumber, const string& accountType, double balance) {
        depositorName = name;
        accountNum = accountNumber;
        accountTypeStr = accountType;
        accountBalance = balance;
    }

    void deposit(double amount) {
        if (amount > 0) {
            accountBalance += amount;
            cout << "Deposit of $" << amount << " successful." << endl;
        } else {
            cout << "Invalid deposit amount." << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= accountBalance) {
            accountBalance -= amount;
            cout << "Withdrawal of $" << amount << " successful." << endl;
        } else {
            cout << "Invalid withdrawal amount or insufficient balance." << endl;
        }
    }

    void displayInfo() {
        cout << "Account Information" << endl;
        cout << "Depositor Name: " << depositorName << endl;
        cout << "Account Number: " << accountNum << endl;
        cout << "Account Type: " << accountTypeStr << endl;
        cout << "Account Balance: $" << accountBalance << endl;
    }

private:
    string depositorName;
    long accountNum;
    string accountTypeStr;
    double accountBalance;
};

int main() {
    BankAccount account1("John Doe", 1234567890, "Savings", 1000.0);

    account1.deposit(500.0);
    account1.withdraw(200.0);

    account1.displayInfo();

    return 0;
}

