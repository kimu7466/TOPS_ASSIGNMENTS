#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string depositor_name;
    string account_number;
    string account_type;
    double balance;

public:
    // Constructor to initialize the data members
    BankAccount(string name, string acc_number, string acc_type, double initial_balance) {
        depositor_name = name;
        account_number = acc_number;
        account_type = acc_type;
        balance = initial_balance;
    }

    // Member function to deposit money into the account
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << " into the account. New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount. Please enter a positive amount." << endl;
        }
    }

    // Member function to withdraw money from the account
    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn $" << amount << " from the account. New balance: $" << balance << endl;
        } else if (amount <= 0) {
            cout << "Invalid withdrawal amount. Please enter a positive amount." << endl;
        } else {
            cout << "Insufficient balance for withdrawal." << endl;
        }
    }

    // Member function to get the current balance
    double get_balance() {
        return balance;
    }

    // Member function to display account information
    void display_account_info() {
        cout << "Account Information" << endl;
        cout << "Name of Depositor: " << depositor_name << endl;
        cout << "Account Number: " << account_number << endl;
        cout << "Account Type: " << account_type << endl;
        cout << "Balance: $" << balance << endl;
    }
};

int main() {
    // Create an instance of the BankAccount class
    BankAccount account("John Doe", "1234567890", "Savings", 1000.0);

    // Example usage
    account.display_account_info();
    account.deposit(500.0);
    account.withdraw(200.0);
    cout << "Current Balance: $" << account.get_balance() << endl;

    return 0;
}

