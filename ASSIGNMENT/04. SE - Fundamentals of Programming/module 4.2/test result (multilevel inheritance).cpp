#include <iostream>
#include <string>
using namespace std;

class Students {
protected:
    int rollNumber;

public:
   
    Students(int roll) : rollNumber(roll) {}

    void displayRollNumber() {
        cout << "Roll Number: " << rollNumber << endl;
    }
};

class Test : public Students {
protected:
    int subject1Marks;
    int subject2Marks;

public:   
    Test(int roll, int marks1, int marks2) : Students(roll), subject1Marks(marks1), subject2Marks(marks2) {}
   
    void displayTestMarks() {
        cout << "Subject 1 Marks: " << subject1Marks << endl;
        cout << "Subject 2 Marks: " << subject2Marks << endl;
    }
};

class Result : public Test {
public:
    Result(int roll, int marks1, int marks2) : Test(roll, marks1, marks2) {}

    void displayTotalMarks() {
        int totalMarks = subject1Marks + subject2Marks;
        cout << "Total Marks: " << totalMarks << endl;
    }
};

int main() {
   
    Result studentResult(101, 85, 92);
   
    cout << "Student Information:" << endl;
    studentResult.displayRollNumber();
    studentResult.displayTestMarks();
    studentResult.displayTotalMarks();

    return 0;
}

